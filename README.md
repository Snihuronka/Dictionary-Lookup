# Dictionary Lookup

A small Tkinter GUI for looking up an English word across several online
dictionaries at once. Enter a word, pick which dictionaries to query, and
each selected entry opens in your web browser.

## Requirements

- Python 3 (with the standard library tkinter module)
- A web browser
- On Linux: xdg-open is used when available (falls back to the webbrowser
  module otherwise)

On most Linux distributions tkinter ships separately from Python. Install it
with your package manager if needed, for example:

- Debian/Ubuntu:   `sudo apt install python3-tk`
- Fedora/RHEL:     `sudo dnf install python3-tkinter`
- Arch:            `sudo pacman -S tk`

## Usage

Run the script directly:

```sh
python3 Dicts.py
```

or, if it is marked executable:

```sh
./Dicts.py
```

Then:

1. Type a word into the "Word:" field.
2. Tick the dictionaries you want to search (all are selected by default).
   Use "Select all" / "Clear" to toggle them quickly.
3. Click "Look up" (or press Enter in the word field).

Each selected dictionary opens in a new browser tab with the word pre-filled.

## Supported Dictionaries

- Oxford English Dictionary
- Cambridge
- Collins
- Merriam-Webster
- Britannica

## Customizing

To add, remove, or change dictionaries, edit the `DICTIONARIES` dictionary near
the top of `Dicts.py`. Each entry maps a display name to a URL template, where
`{word}` is replaced by the URL-encoded search term. For example:

```python
"Wiktionary": "https://en.wiktionary.org/wiki/{word}",
```

## Notes

- The search word is URL-encoded, so multi-word phrases and special
  characters are handled safely.
- On Linux, stderr from the URL opener is suppressed to avoid noisy output
  (e.g. KIO warnings).
  
