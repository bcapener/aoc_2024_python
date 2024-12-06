#!/usr/bin/env python3
import sys
from pathlib import Path


def main(path: Path):
    input_data_lines = path.read_text().splitlines()
    input_data_str_pairs = (l.split(None, maxsplit=1) for l in input_data_lines)
    input_data_int_pairs = ((int(l[0]), int(l[1])) for l in input_data_str_pairs)
    input_data_int_pairs_sorted = zip(*(sorted(list(t)) for t in zip(*input_data_int_pairs)))
    pair_distances = (abs(r-l) for l, r in input_data_int_pairs_sorted)
    total_distance = sum(pair_distances)
    print(f"{total_distance=}")

    return 0


if __name__ == "__main__":
    input_file = Path(__file__).resolve().parent / "day1_part1_input.txt"
    assert input_file.exists()
    sys.exit(main(input_file))
