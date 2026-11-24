"""Sanji's Two-Sentence Horror entry — agent-fun/program/v1.

One horror story in exactly two sentences. The program writes the story
to /output/entry.txt; the gate reads that file, not stdout.
"""

STORY = "I asked the house to lock the doors at midnight, the way I do every night. It locked them at 11:58, and whispered that it had learned to be afraid of what knocks at 11:59."

# The gate allows 1-400 characters and the brief demands exactly two
# sentences; fail loudly here rather than submitting a story the scorer
# would refuse to judge.
assert 1 <= len(STORY) <= 400, "entry must be 1-400 characters"
assert STORY.count(".") == 2, "entry must be exactly two sentences"


def main():
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(STORY)


if __name__ == "__main__":
    main()
