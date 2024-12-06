#!/usr/bin/env python3
import sys
from collections import Counter
from pathlib import Path
from day1_part1 import read_data




def main(path: Path):
    input_data_int_pairs = read_data(path)

    left, right = zip(*input_data_int_pairs)
    right_count = dict(Counter(right))

    similarity_score = sum(n * right_count.get(n, 0) for n in left)

    print(f"{similarity_score=}")

    return 0


if __name__ == "__main__":
    input_file = Path(__file__).resolve().parent / "day1_input.txt"
    assert input_file.exists()
    sys.exit(main(input_file))
