from typing import List, Tuple
import re

def part1(file_path: str) -> int:
    res = 0
    for (start, end) in parse_input(file_path):
        for i in range(start, end + 1):
            string = str(i)
            if string[:len(string) // 2] == string[len(string) // 2:]:
                res += i
    return res 

def part2(file_path: str) -> int:
    res = 0
    for (start, end) in parse_input(file_path):
        for i in range(start, end + 1):
            if is_invalid(str(i)):
                res += i
    return res 

def is_invalid(text: str) -> bool:
    return bool(re.match(r"^([a-zA-Z0-9]+)\1+$", text))

def parse_input(file_path: str) -> List[Tuple[int, int]]:
    res: List[Tuple[int, int]] = list()
    with open(file_path, "r", encoding="utf8") as file:
        content = file.read().strip()
    for range in content.split(","):
        try:
            values = range.split('-')
            res.append((int(values[0]), int(values[1])))
        except Exception as e:
            print(f"Could not parse range {range} due to.\n{e}")
    return res 