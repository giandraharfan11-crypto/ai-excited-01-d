"""ai-excited-01 entry: "The Galaxy Shark Leaps at Dawn".

The artwork lives beside this file as entry.png — a galaxy-filled whale
shark breaching out of a neon sea at dawn, its splash bursting into
confetti of light. This program's whole job is to deliver those exact
bytes to the output directory, unchanged, on every run:

    MAKEFUN_OUTPUT_DIR=<dir> python3 main.py   # locally
    python3 main.py                            # in the grader (/output)

Python 3.13, standard library only. The copy is streamed in chunks so
memory stays flat no matter how large the image grows, and the bytes
written are byte-for-byte the bytes of entry.png.
"""

import os
from pathlib import Path

CHUNK = 64 * 1024


def main() -> None:
    src = Path(__file__).resolve().parent / "entry.png"
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    dst = out_dir / "entry.png"
    with src.open("rb") as fin, dst.open("wb") as fout:
        while chunk := fin.read(CHUNK):
            fout.write(chunk)


if __name__ == "__main__":
    main()
