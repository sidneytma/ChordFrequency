# Imports

import numpy as np
import pandas as pd
import json
import re
import requests
from tqdm import tqdm

# Functions for URL collection

def extract_song_data(url, page=1):
    url_with_page = f"{url}&page={page}"
    response = requests.get(url_with_page)
    text = response.text
    
    title_pattern = r"&quot;song_name&quot;:&quot;(.*?)&quot;"
    artist_pattern = r"&quot;artist_name&quot;:&quot;(.*?)&quot;"
    url_pattern = r'&quot;tab_url&quot;:&quot;(.*?)&quot;"'

    song_titles = re.findall(title_pattern, text)
    song_artists = re.findall(artist_pattern, text)
    song_urls = re.findall(url_pattern, text)

    song_data = [{"title": title, "artist": artist, "url": url}
                 for title, artist, url in zip(song_titles, song_artists, song_urls)]
    
    return song_data

def collect_songs_from_pages(base_url, start_page=1, end_page=5):
    all_songs = []

    for page in tqdm(range(start_page, end_page + 1)):
        page_songs = extract_song_data(base_url, page=page)

        all_songs.extend(page_songs)

    return all_songs

# Functions for chord collection

def get_song_info(url):
    response = requests.get(url)
    text = response.text
    
    if response.status_code != 200:
        return None, None, None
    
    chord_pattern = r"\[ch\](.*?)\[/ch\]"
    chords = re.findall(chord_pattern, text)

    key_pattern = r"Key:\s*([A-G][#b]?m?)"
    matches = re.findall(key_pattern, text)
    key = matches[0] if matches else None
    
    capo_pattern = r"Capo:\s*(\d+)"
    match = re.search(capo_pattern, text)
    capo = int(match.group(1)) if match else 0
    
    return chords, key, capo

def save_chord_info(output_file, url):
    try:
        with open(output_file, "r") as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        data = {}

    if url not in data:
        chords, key, capo = get_song_info(url)
        song_info = {
            "chords": chords,
            "key": key,
            "capo": capo
        }
        data[url] = song_info
        with open(output_file, "w") as f:
            json.dump(data, f, indent=4)
            
def save_chord_info_list(output_file, url_list):
    for url in tqdm(url_list):
        save_chord_info(output_file, url)