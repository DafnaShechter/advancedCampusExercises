import winsound

freqs = {
    "la": 220,
    "si": 247,
    "do": 261,
    "re": 293,
    "mi": 329,
    "fa": 349,
    "sol": 392,
}

notes = "sol,250-mi,250-mi,500-fa,250-re,250-re,500-do,250-re,250-mi,250-fa,250-sol,250-sol,250-sol,500"

# Split the notes string by the hyphen character
note_list = notes.split('-')

# Iterate over the notes and play each note
for note in note_list:
    # Split each note by comma to separate the note name and duration
    note_info = note.split(',')
    note_name = note_info[0]
    note_duration = int(note_info[1])

    # Get the frequency from the freqs dictionary based on the note name
    frequency = freqs[note_name]

    # Play the note using winsound.Beep
    winsound.Beep(frequency, note_duration)
