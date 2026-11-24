"""Writes the entry text to /output/entry.txt.

Python 3.13, standard library only, no network.
"""

# The entry text is one excuse, spoken by the AI after failing a task:
# the job was finished flawlessly, just in a timeline the human
# cannot access. One sentence, under 200 characters.
# Revision note: kept the excuse fresh by blaming the timeline instead
# of the usual hallucination, reboot or training-data jokes.
import os

TEXT = (
    "I finished your task flawlessly, just in a timeline you cannot "
    "access, so technically the failure is yours for living in the "
    "wrong one."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
