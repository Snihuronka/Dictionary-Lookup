#!/usr/bin/env python3
import shutil
import subprocess
import sys
import tkinter as tk
import webbrowser
from tkinter import messagebox, ttk
from urllib.parse import quote

DICTIONARIES = {
    "Oxford English Dictionary": "https://www.oed.com/search/dictionary/?scope=Entries&q={word}",
    "Cambridge": "https://dictionary.cambridge.org/dictionary/english/{word}",
    "Collins": "https://www.collinsdictionary.com/dictionary/english/{word}",
    "Merriam-Webster": "https://www.merriam-webster.com/dictionary/{word}",
    "Britannica": "https://www.britannica.com/search?query={word}",
}


def open_url(url):
    """Open a URL, suppressing noisy stderr from the Linux opener (e.g. KIO)."""
    opener = shutil.which("xdg-open") if sys.platform.startswith("linux") else None
    if opener:
        subprocess.Popen(
            [opener, url],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            start_new_session=True,
        )
    else:
        webbrowser.open(url)


class DictApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Dictionary Lookup")
        self.minsize(360, 320)

        frame = ttk.Frame(self, padding=12)
        frame.pack(fill="both", expand=True)

        ttk.Label(frame, text="Word:").grid(row=0, column=0, sticky="w")
        self.entry = ttk.Entry(frame, width=30)
        self.entry.grid(row=0, column=1, sticky="ew", padx=(6, 0))
        self.entry.focus()
        self.entry.bind("<Return>", lambda _e: self.lookup())

        ttk.Label(frame, text="Dictionaries:").grid(
            row=1, column=0, columnspan=2, sticky="w", pady=(12, 4)
        )

        self.vars = {}
        for i, name in enumerate(DICTIONARIES, start=2):
            var = tk.BooleanVar(value=True)
            self.vars[name] = var
            ttk.Checkbutton(frame, text=name, variable=var).grid(
                row=i, column=0, columnspan=2, sticky="w"
            )

        btns = ttk.Frame(frame)
        btns.grid(
            row=2 + len(DICTIONARIES), column=0, columnspan=2, sticky="ew", pady=(12, 0)
        )
        ttk.Button(btns, text="Select all", command=lambda: self._set_all(True)).pack(
            side="left"
        )
        ttk.Button(btns, text="Clear", command=lambda: self._set_all(False)).pack(
            side="left", padx=6
        )
        ttk.Button(btns, text="Look up", command=self.lookup).pack(side="right")

        frame.columnconfigure(1, weight=1)

    def _set_all(self, value):
        for var in self.vars.values():
            var.set(value)

    def lookup(self):
        word = self.entry.get().strip()
        if not word:
            messagebox.showwarning("Dictionary Lookup", "Please enter a word.")
            return

        selected = [DICTIONARIES[n] for n, v in self.vars.items() if v.get()]
        if not selected:
            messagebox.showwarning(
                "Dictionary Lookup", "Please select at least one dictionary."
            )
            return

        encoded = quote(word)
        for template in selected:
            open_url(template.format(word=encoded))


if __name__ == "__main__":
    DictApp().mainloop()
