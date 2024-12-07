#!/usr/bin/env python3
import re
import sys
from pathlib import Path

mul_instruction_pattern = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")

def main(path: Path):
    data = path.read_text()
    result = 0
    for multiplicand_str, multiplicator_str in re.findall(mul_instruction_pattern, data):
        multiplicand = int(multiplicand_str)
        multiplicator = int(multiplicator_str)
        result += multiplicand * multiplicator

    print(f"{result=}")

    return 0


if __name__ == "__main__":
    input_file = Path(__file__).resolve().parent / "day3_input.txt"
    assert input_file.exists()
    sys.exit(main(input_file))
