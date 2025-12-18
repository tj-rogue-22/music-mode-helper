import sys

NOTES = [
'A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#'
]

MODES = [
    'Ionian', 'Dorian', 'Phrygian', 'Lydian', 
    'Mixolydian', 'Aeolian', 'Locrian'
]

IONIAN_INTERVALS = [0, 2, 2, 1, 2, 2, 2]

def get_offset(key):
    if key in NOTES:
        return NOTES.index(key)
    else:
        print("invalid key: " + key)
        sys.exit(1)

def main():
    if len(sys.argv) != 2:
        print("Please provide a note: python3 main.py <note>")
        sys.exit(1)

    musical_key = sys.argv[1]
 
    # offset by root note
    note_offset = get_offset(musical_key)
    print(f"Key of {musical_key}")
    
    # ascend the scale 
    scale_degree = IONIAN_INTERVALS[0]
    mode_index = 0

    for i in IONIAN_INTERVALS:

        scale_degree += i

        note_index = (note_offset + scale_degree) % len(NOTES)
        note = NOTES[note_index] 
        mode = MODES[mode_index]

        print("note", note, " ", mode) 

        mode_index += 1

if __name__ == "__main__":
    main()
