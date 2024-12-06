#!/usr/bin/env python3
import sys
from pathlib import Path
from day1_part1 import read_data


def is_report_safe(report: tuple[int]):
    prev_level: int|None = None
    is_increasing: bool|None = None

    for i, level in enumerate(report):
        is_first_level = i == 0
        is_second_level = i == 1
        is_other_levels = i > 1

        if not is_first_level:
            step = abs(level - prev_level)
            if 3 < step or step < 1:
                return False

        if is_second_level:
            is_increasing = level > prev_level
        elif is_other_levels:
            if is_increasing and level < prev_level:
                return False
            if not is_increasing and level > prev_level:
                return False

        prev_level = level
    return True


def main(path: Path):
    gen_tuple_of_ints = read_data(path)

    number_of_safe_reports = 0
    for report in gen_tuple_of_ints:
        if is_report_safe(report):
            number_of_safe_reports += 1

    print(f"{number_of_safe_reports=}")

    return 0


if __name__ == "__main__":
    input_file = Path(__file__).resolve().parent / "day2_input.txt"
    assert input_file.exists()
    sys.exit(main(input_file))
