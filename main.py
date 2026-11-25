"""Monday Morning Punchlines: write one joke about Monday mornings."""

import os
from pathlib import Path

JOKE = "Monday morning is a calendar invite I never accepted, and there is no decline button."


def main():
    if not 1 <= len(JOKE) <= 200:
        raise ValueError("joke must be 1-200 characters")
    output_dir = Path(os.environ["MAKEFUN_OUTPUT_DIR"])
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()
