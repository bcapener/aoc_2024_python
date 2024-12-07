#!/usr/bin/env python3
import sys
from pathlib import Path
from day1_part1 import read_data

def filter_report(report: tuple[int], skip_level):
    if skip_level == 0:
        prev_level = report[1]
        report = report[2:]
        skip_level = None  # level 0 already filtered out, disable further filtering.
    else:
        prev_level = report[0]
        report = report[1:]

    for i, level in enumerate(report, start=1):
        if i == skip_level:
            continue

        yield prev_level, level

        prev_level = level


def generate_filtered_reports(report: tuple[int]):
    skip_levels = [None] + list(range(len(report)))

    for skip_level in skip_levels:
        yield filter_report(report, skip_level)

def is_report_safe(report: tuple[int]):
    is_safe = False

    for filtered_report in generate_filtered_reports(report):
        is_increasing: bool|None = None

        is_safe = True
        for prev_level, level in filtered_report:

            step = abs(level - prev_level)
            if 3 < step or step < 1:
                is_safe = False
                break

            if is_increasing is None:
                is_increasing = level > prev_level
            else:
                if is_increasing and level < prev_level:
                    is_safe = False
                    break
                if not is_increasing and level > prev_level:
                    is_safe = False
                    break

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
