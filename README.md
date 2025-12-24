# music-mode-helper
a small personal project for showing information about musical keys and modes

Features

* build a 7-degree scale from a root note (A..G#)
* pure core function (easy to unit test)
* uses list/tuple/zip for clear iteration
* table output via tabulate

### Quick start

#### Requirements:

* Python 3.9+
* tabulate for table output: ```pip install tabulate```

#### Run:
* python script:
    ```python3 mmh.py C```

#### Example output:

| Deg | Note | Chord | Mode |
|-----|------|-------|-------|
| 1   | C    | maj   | Ionian |
| 2   | D    | min   | Dorian |
| 3   | E    | min   | Phrygian |
| 4   | F    | maj   | Lydian |
| 5   | G    | maj   | Mixolydian |
| 6   | A    | min   | Aeolian |
| 7   | B    | dim   | Locrian |

### Design decisions

    * used zip() for parallel iteration with less state
    * build_key_info returns immutable dataclass records; printing separated from logic
    * inclusion of type hints


### Further delopment

    * show borrowable chords from parallel minor key
    * add internal software tests
    * support passing any mode (Lydian, etc) for the scale
    * show scale degrees via Roman numerals
    * CLI polish