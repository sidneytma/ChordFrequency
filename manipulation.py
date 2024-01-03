# Imports

import numpy as np
import pandas as pd

# Functions

def get_quality(chord):
    if "m" in chord:
        return "minor"
    if "dim" in chord:
        return "diminished"
    return "major"

def get_qualities(chords):
    return [get_quality(chord) for chord in chords]

def get_root(chord):
    chord = chord.split("/")[0]
    if len(chord) > 1 and chord[1] in ("#", "b"):
        return chord[:2]
    return chord[0]

def get_roots(chords):
    return [get_root(chord) for chord in chords]
                 
def note_to_int(note):
    notes = {
        "C": 0, "C#": 1, "Db": 1,
        "D": 2, "D#": 3, "Eb": 3,
        "E": 4, "F": 5,
        "F#": 6, "Gb": 6,
        "G": 7, "G#": 8, "Ab": 8,
        "A": 9, "A#": 10, "Bb": 10,
        "B": 11
    }
    return notes.get(note, None)

def notes_to_ints(notes):
    return [note_to_int(note) for note in notes]

def int_to_note(note_int):
    notes = {
        0: "C", 1: "Db", 2: "D",
        3: "Eb", 4: "E", 5: "F",
        6: "Gb", 7: "G", 8: "Ab",
        9: "A", 10: "Bb", 11: "B"
    }
    return notes.get(note_int, None)

def ints_to_notes(note_ints):
    return [int_to_note(note_int) for note_int in note_ints]

def get_relative_major(key):
    key_int = note_to_int(get_root(key))
    if "m" in key:
        return (key_int + 3) % 12
    return key_int

def adjust_capo(chord_int, capo):
    return (chord_int + capo) % 12

def transpose_to_C(note_int, key_int):
    return (note_int - key_int) % 12

def perform_transposition(chord, key, capo):
    key_int = get_relative_major(key)
    root = get_root(chord)
    chord_int = note_to_int(root)
    chord_int = adjust_capo(chord_int, capo)
    chord_int = transpose_to_C(chord_int, key_int)
    return int_to_note(chord_int)

def perform_transpositions(chords, key, capo):
    return [perform_transposition(chord, key, capo) for chord in chords]

def get_transitions(chords):
    return [chords[i+1] - chords[i] for i in range(len(chords) - 1)]

def concatenate_chords(row):
    chords_in_C = []
    for root, quality in zip(row["roots_in_C"], row["qualities"]):
        chord = root
        if quality == "minor":
            chord += "m"
        if quality == "diminished":
            chord += "dim"
        chords_in_C.append(chord)
    return chords_in_C

def prop_diatonic(chords):
    diatonic_chords = {"C", "Dm", "Em", "F", "G", "Am", "Bdim"}
    
    diatonic_count = sum(chord in diatonic_chords for chord in chords)
    
    proportion = diatonic_count / len(chords) if chords else 0
    return proportion