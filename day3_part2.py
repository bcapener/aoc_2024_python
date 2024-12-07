#!/usr/bin/env python3
import re
import sys
from pathlib import Path

mul_instruction_pattern = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")

def main(path: Path):
    data = "do()" + path.read_text()

    result = 0
    for donts in data.split("don't()"):
        try:
            _, dos = donts.split("do()", maxsplit=1)
        except ValueError:
            # no do() in text
            continue

        for multiplicand_str, multiplicator_str in re.findall(mul_instruction_pattern, dos):
            multiplicand = int(multiplicand_str)
            multiplicator = int(multiplicator_str)
            result += multiplicand * multiplicator

    print(f"{result=}")
    assert result == 82857512

    return 0


if __name__ == "__main__":
    input_file = Path(__file__).resolve().parent / "day3_input.txt"
    assert input_file.exists()
    sys.exit(main(input_file))
