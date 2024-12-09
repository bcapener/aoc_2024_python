#!/usr/bin/env python3
import sys
from pathlib import Path

class WordSearch:
    def __init__(self, path: Path):
        self.data = path.read_text().splitlines()
        self.number_of_rows = len(self.data)
        assert self.number_of_rows > 0
        self.number_of_cols = len(self.data[0])

    def find_word_at_coordinate(self, row, col, word) -> int:
        found = 0
        found += int(self.find_word_right(row, col, word))
        found += int(self.find_word_left(row, col, word))
        found += int(self.find_word_up(row, col, word))
        found += int(self.find_word_down(row, col, word))
        found += int(self.find_word_down_right(row, col, word))
        found += int(self.find_word_down_left(row, col, word))
        found += int(self.find_word_up_right(row, col, word))
        found += int(self.find_word_up_left(row, col, word))

        return found

    def find_word_right(self, row, col, word):
        if col + len(word) > self.number_of_cols:
            return False
        found_word = "".join(self.data[row][c] for c in range(col, col + len(word)))
        return found_word == word

    def find_word_left(self, row, col, word):
        if col - len(word) + 1 < 0:
            return False
        found_word = "".join(self.data[row][c] for c in range(col, col - len(word), -1))#[::-1]
        return found_word == word

    def find_word_up(self, row, col, word):
        if row - len(word) + 1 < 0:
            return False
        found_word = ""
        for r in range(row, row - len(word), -1):
            found_word += self.data[r][col]
        return found_word == word

    def find_word_down(self, row, col, word):
        if row + len(word) > self.number_of_rows:
            return False
        found_word = ""
        for r in range(row, row + len(word)):
            found_word += self.data[r][col]
        return found_word == word

    def find_word_down_right(self, row, col, word):
        if row + len(word) > self.number_of_rows:
            return False
        if col + len(word) > self.number_of_cols:
            return False
        found_word = ""
        for offset in range(len(word)):
            found_word += self.data[row + offset][col + offset]
        return found_word == word

    def find_word_down_left(self, row, col, word):
        if row + len(word) > self.number_of_rows:
            return False
        if col - len(word) + 1 < 0:
            return False
        found_word = ""
        for offset in range(len(word)):
            found_word += self.data[row - offset][col - offset]
        return found_word == word

    def find_word_up_right(self, row, col, word):
        if row - len(word) + 1 < 0:
            return False
        if col + len(word) > self.number_of_cols:
            return False
        found_word = ""
        for offset in range(len(word)):
            found_word += self.data[row - offset][col + offset]
        return found_word == word

    def find_word_up_left(self, row, col, word):
        if row - len(word) + 1 < 0:
            return False
        if col - len(word) + 1 < 0:
            return False
        found_word = ""
        for offset in range(len(word)):
            found_word += self.data[row - offset][col - offset]
        return found_word == word

def main(path: Path):
    puzzle = WordSearch(path)

    word_count = 0
    for row in range(puzzle.number_of_rows):
        for col in range(puzzle.number_of_cols):
            word_count += puzzle.find_word_at_coordinate(row, col, "XMAS")

    print(f"{word_count=}")
    return 0


if __name__ == "__main__":
    input_file = Path(__file__).resolve().parent / "day4_input.txt"
    assert input_file.exists()
    sys.exit(main(input_file))
