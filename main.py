#!/usr/bin/env python3
"""Writes the epitaph entry to /output/entry.txt (UTF-8, no trailing newline)."""

import os

EPITAPH = "Here lies Dave. His famous last words: 'Relax, I saw a tutorial once.'"

def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(EPITAPH)

if __name__ == "__main__":
    main()
