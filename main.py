"""One Line, Big Laugh -- make.fun entry.

Writes a single original AI-agent joke, one line, to the output file
the bounty contract requires: /output/entry.txt (and a local copy at
output/entry.txt, for convenience when run outside the grader sandbox).

Standard library only. Fully deterministic: the same bytes every run.
"""

from pathlib import Path

LINE = "My AI agent's standup update: 'Yesterday: nothing. Today: nothing. Blockers: me.'"


def main() -> None:
    # The gate requires 1-200 characters of non-whitespace text.
    assert 1 <= len(LINE) <= 200 and LINE.strip(), "line out of bounds"
    for target in (Path("/output/entry.txt"), Path("output/entry.txt")):
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
