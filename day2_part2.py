#!/usr/bin/env python3
import sys
from pathlib import Path
from day1_part1 import read_data


def is_report_safe(report: tuple[int]):
    skip_levels = [None] + list(range(len(report)))
    is_safe = False

    for skip_level in skip_levels:
        prev_level: int|None = None
        is_increasing: bool|None = None

        is_safe = True

        for i, level in enumerate(report):
            if i == skip_level:
                continue

            is_first_level = prev_level is None
            is_second_level = prev_level is not None and is_increasing is None
            is_other_levels = not is_first_level and not is_second_level

            if not is_first_level:
                step = abs(level - prev_level)
                if 3 < step or step < 1:
                    is_safe = False
                    break

            if is_second_level:
                is_increasing = level > prev_level
            elif is_other_levels:
                if is_increasing and level < prev_level:
                    is_safe = False
                    break
                if not is_increasing and level > prev_level:
                    is_safe = False
                    break

            prev_level = level

        if is_safe:
            break
    return is_safe


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
