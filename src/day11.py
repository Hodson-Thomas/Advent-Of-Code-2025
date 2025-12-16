from typing import List, Dict


def part1(file_path: str) -> int:
    data = parse_input(file_path)

    def solve(node: str, path: List[str]) -> int:
        if node == "out":
            return 1
        if node in path:
            return 0
        return sum([solve(n, path + [node]) for n in data[node]])
    
    return solve("you", [])

def part2(file_path: str) -> int:
    data = parse_input(file_path)

    def solve(node: str, path: List[str], dac: bool, fft: bool) -> int:
        if node == "out":
            if dac and fft:
                return 1
            return 0
        if node in path:
            return 0
        return sum([solve(n, path + [node], dac or node == "dac", fft or node == "fft") for n in data[node]])
    
    return solve("svr", [], False, False)

def parse_input(file_path: str) -> Dict[str, List[str]]:
    res: Dict[str, List[str]] = dict()
    with open(file_path, "r", encoding="utf8") as file:
        content = file.read().strip()
    
    for line in content.split('\n'):
        s = line.split(': ')
        if len(s) != 2:
            continue
        res[s[0]] = s[1].split(' ')

    return res