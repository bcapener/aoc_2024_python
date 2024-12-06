#!/usr/bin/env python3
import sys
from pathlib import Path

def read_data(path: Path):
    input_data_lines = path.read_text().splitlines()
    gen_list_of_strs = (line.split() for line in input_data_lines)
    gen_tuple_of_ints = (tuple(int(number) for number in paris) for paris in gen_list_of_strs)
    return gen_tuple_of_ints

def main(path: Path):
    input_data_int_pairs = read_data(path)
    input_data_int_pairs_sorted = zip(*(sorted(list(t)) for t in zip(*input_data_int_pairs)))
    pair_distances = (abs(r-l) for l, r in input_data_int_pairs_sorted)
    total_distance = sum(pair_distances)
    print(f"{total_distance=}")

    return 0


if __name__ == "__main__":
    input_file = Path(__file__).resolve().parent / "day1_input.txt"
    assert input_file.exists()
    sys.exit(main(input_file))
