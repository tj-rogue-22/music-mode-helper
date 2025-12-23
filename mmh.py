import sys
import pprint
from typing import List, Tuple
from tabulate import tabulate

NOTES = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
MODES = ['Ionian', 'Dorian', 'Phrygian', 'Lydian', 'Mixolydian', 'Aeolian', 'Locrian']
CHORDS = ['maj', 'min', 'min', 'maj', 'maj', 'min', 'dim']
IONIAN_STEPS = [2, 2, 1, 2, 2, 2, 1]

def get_note_offset(key: str) -> int:
    if key in NOTES:
        return NOTES.index(key)
    else:
        print(f"invalid key: {key}")
        sys.exit(1)

def get_modal_offset(mode: str) -> int:
    if mode in MODES:
        return MODES.index(mode)
    else:
        print(f"invalid mode supplied: {mode}")
        sys.exit(1)

def build_key_dict(root: str) -> List[Tuple[str, str, str]]:
    result: List[Tuple[str, str, str]] = []
    note_index = get_note_offset(root)
    modal_index = 0 

    i = 0

    while i < len(IONIAN_STEPS):
        note = NOTES[note_index] 
        chord = CHORDS[modal_index]
        mode = MODES[modal_index]

        result.append((note, chord, mode))
        
        modal_index += 1
        modal_index = (modal_index) % len(MODES)
        next_step = IONIAN_STEPS[modal_index]
        note_index = (note_index + next_step) % len(NOTES)
       
        i += 1

    return result

def main():
    if len(sys.argv) != 2:
        print("Please provide a note: python3 main.py <note>")
        sys.exit(1)

    key = sys.argv[1]
    print(f"Key: {key} Ionian")
 
    key_data = build_key_dict(key)
    print(tabulate(key_data, headers=["Note","Chord","Mode"], tablefmt="github"))
    #pprint.pp(key_data)

if __name__ == "__main__":
    main()
