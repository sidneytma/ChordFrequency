# Frequency of Chords in Popular Music
## Background
- it's well known that there are four "essential" chords in popular music: I, V, iv, and IV
- made popular from the Axis of Awesome videos.
- from the video: "All the greatest hits from the past 40 years just use four chords. Same four chords for every song, it's dead simple to write a pop hit."
- while this was largely focused on pop music, the same observation has been made in country, rock and punk.
- as mentioned before, this is pretty well known. but exactly how frequent are these four chords?
## Data
- to collect data on chords, i scraped song data from Ultimate Guitar. I collected most popular 250 chord tabs, and for each song, collected the song's key, capo setting, and full list of chords.
- using the key and capo setting, i transposed these chords to C major
- i filtered out songs that were formatted incorrectly, and ended up with 169 songs to analyze.
- this measured out to 18,036 chords, an average of about 106 chords per song.
- while it is inevitable that some of these chords are incorrect due to incorrect tabs, my assumption is that because my selection includes the most popular tabs on the website, and comment/rating feedback exists, most of the tabs will be correct.
## Results
### Main Results
- In C major, the chords I, V, iv, and IV are C, G, Am, and F, respectively. Since these four chords are known as the "essential" chords in popular music, the expectation is that they should have the highest frequency.
- (graph)
- as expected, it is clear from the graph that these four chords (C, G, F, Am) are indeed the most common. on their own, they make up about 87% of all chords in the dataset.
- it's certainly true that these four chords are used disproportionately often. however, it would be a stretch to say that these are the only chords necessary, even as an exaggeration.
- while about 78% of songs use all four of these chords, only about 22% use these four chords exclusively.
### Additional Results
- unsurprisingly, all diatonic chords (except for Bdim) are more common than all non-diatonic chords, and make up nearly 95% of all chords.
- however, there are some non-diatonic chords that were non-negligeable
- the first chords worth mentioning are D, E, and A (major). These chords are less common than their minor versions, but often appear as dominant 7th chords (D7, E7, A7) in C major, even though these are non-diatonic. However, since my manipulation process removed all extensions (7ths, 9ths, etc.) and only included qualities, these chords only show up as D, E, and A major.
- another interesting case is Fm (iv in C major). This chord is less common than F major, but often appears in a minor plagal cadence, typically in the sequence IV - iv - I.
- the last chord i will mention is Bb (bVII in C major). This chord is not diatonic in major nor minor, and often appears as a borrowed chord from the parallel minor. However, this could also be an effect of songs being written in Mixolydian but analyzed in Ionian. For instance, American Idiot by Green Day is a in Ab Mixolydian, and its main riff is arguably best analyzed as I - IV - VII - VI - I - VII. However, since my manipulation assumes the key to be Ab major, the main riff would instead be analyzed as I - IV - bVII - VI - I - bVII. 
