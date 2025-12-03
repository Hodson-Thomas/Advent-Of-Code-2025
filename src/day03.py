from typing import List, Optional, Tuple
from src.utils import parse_input_lines


def part1(file_path: str) -> int:
    banks = parse_input_lines(file_path, parse_line)
    total = 0
    for bank in banks:
        max = 0
        for i in range(0, len(bank) - 1):
            for j in range(i + 1, len(bank)):
                val = bank[i] * 10 + bank[j]
                if val > max:
                    max = val
        total += max
    return total    


def part2(file_path: str) -> int:
    banks = parse_input_lines(file_path, parse_line)
    total = 0
    for bank in banks:
        res = 0
        cursor = 0
        for i in range(1, 13):
            (digit, index) = get_next_greater_digit(bank, cursor, len(bank) - (12 - i))
            cursor = index + 1
            res = res * 10 + digit
        total += res
    return total            


def get_next_greater_digit(sequence: List[int], start: int, end: int) -> Tuple[int, int]:
    max = 0
    max_index = 0
    for i in range(start, end):
        if sequence[i] > max:
            max = sequence[i]
            max_index = i
    return (max, max_index)


def parse_line(line: str) -> Optional[List[int]]:
    res: List[int] = []
    for c in line.strip():
        try:
            res.append(int(c))
        except Exception as e:
            print(f"Could not parse char {c} as int due to:\n{e}")
    
    return res
