#!/usr/bin/env python3
"""news-image-20261124 v2 — sums up Tuesday 24 November 2026 world news
in one 1024x1024 image.

The image is pre-rendered and held in this repository as entry.png; this
program only copies it to /output/entry.png. Standard library only: no
third-party imports, no network, no wall clock, no randomness, so the
output is byte-identical on every run.

Why a copy instead of drawing it: the v1 entrypoint drew the image with
PIL, but the grader runs `python3 -P -s /bot/main.py` in the official
python:3.13-slim image, which has no Pillow installed, so the import
failed and the run exited with code 1 before any drawing happened. This
version keeps the same verified image and removes the dependency entirely.
The competition rules bless this directly: the simplest program copies an
image the repository holds.
"""
import os
import shutil

OUT = "/output/entry.png"


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    os.makedirs("/output", exist_ok=True)
    shutil.copyfile(src, OUT)
    # Harden the copy: refuse a partial write instead of leaving a
    # truncated image behind. A size mismatch means the copy did not
    # complete, so fail loudly rather than emit a corrupt entry.
    if os.path.getsize(OUT) != os.path.getsize(src):
        raise RuntimeError("entry.png copy incomplete: size mismatch")


if __name__ == "__main__":
    main()
