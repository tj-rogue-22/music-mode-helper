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

def build_key_info(root: str) -> List[Tuple[str, str, str]]:
    result: List[Tuple[str, str, str]] = []
    running_note = get_note_offset(root)

    for step, mode, chord in zip(IONIAN_STEPS, MODES, CHORDS):
        result.append((NOTES[running_note], chord, mode))
        running_note = (running_note + step) % len(NOTES)
        
    return result

def main():
    if len(sys.argv) != 2:
        print("Please provide a note: python3 mmh.py <note>")
        sys.exit(1)

    key = sys.argv[1]
    print(f"Key: {key} Ionian")
 
    key_data = build_key_info(key)
    print(tabulate(key_data, headers=["Note","Chord","Mode"], tablefmt="github"))
    #pprint.pp(key_data)

if __name__ == "__main__":
    main()
