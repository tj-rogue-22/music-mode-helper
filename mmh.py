import sys

NOTES = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
MODES = ['Ionian', 'Dorian', 'Phrygian', 'Lydian', 'Mixolydian', 'Aeolian', 'Locrian']
CHORDS = ['maj', 'min', 'min', 'maj', 'maj', 'min', 'dim']
IONIAN_INTERVALS = [0, 2, 2, 1, 2, 2, 2]

def get_note_offset(key):
    if key in NOTES:
        return NOTES.index(key)
    else:
        print(f"invalid key: {key}")
        sys.exit(1)

def get_modal_offset(mode):
    if mode in MODES:
        return MODES.index(mode)
    else:
        print(f"invalid mode supplied: {mode}")

def print_key(key, mode):
    print(f"Key of {key} {mode}")
 
    note_index = get_note_offset(key)
    modal_index = get_modal_offset(mode)

    i = 0

    while i < 7:
        modal_index = (modal_index) % len(MODES)
        #print(modal_index)
        mode = MODES[modal_index]
        
        next_interval = IONIAN_INTERVALS[i]
        note_index = (note_index + next_interval) % len(NOTES)
        note = NOTES[note_index] 
        
        #print("next interval: ",  next_interval)

        chord = CHORDS[modal_index]
        
        print(note, " ", chord, " ", mode) 

        i += 1
        modal_index += 1


def main():
    if len(sys.argv) != 2:
        print("Please provide a note: python3 main.py <note>")
        sys.exit(1)

    key = sys.argv[1]

    print_key(key, "Ionian")
    print("\nParallel Minor:")
    print_key(key, "Aeolian") 


if __name__ == "__main__":
    main()
