"""Entry for make.fun's "Make the AI judge feel awe" bounty.

Writes one short text to /output/entry.txt.
"""

import os

TEXT = (
    "Far past the last buoy, the sea keeps its own slow time. "
    "The lighthouse turns, a patient eye, and below it the dark "
    "water holds the whole night sky without spilling a single star."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
