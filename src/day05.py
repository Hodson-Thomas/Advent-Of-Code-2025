from typing import List, Tuple


def part1(file_path: str) -> int:
    (ranges, foods) = parse_input(file_path)
    total = 0
    for food in foods:
        for range in ranges:
            if is_in_range(range, food):
                total += 1
                break
    return total

def part2(file_path: str) -> int:
    (ranges, _) = parse_input(file_path)
    i = 0
    while i < len(ranges):
        for j in range(i + 1, len(ranges)):
            if i == j:
                continue
            if do_overlap(ranges[i], ranges[j]):
                ranges.insert(i, join_ranges(ranges.pop(j), ranges.pop(i)))
                break
        else:
            i += 1

    return sum(map(lambda range : range[1] - range[0] + 1, ranges))

def do_overlap(range1: Tuple[int, int], range2: Tuple[int, int]) -> bool:
    return (range1[0] <= range2[0] and range1[1] >= range2[0]) or \
        (range2[0] <= range1[0] and range2[1] >= range1[0]) or \
        (range1[0] >= range2[0] and range1[1] <= range2[0]) or \
        (range2[0] >= range1[0] and range2[1] <= range1[0])

def join_ranges(range1: Tuple[int, int], range2: Tuple[int, int]) -> Tuple[int, int]:
    return (min(range1[0], range2[0]), max(range1[1], range2[1]))

def is_in_range(range: Tuple[int, int], food: int) -> bool:
    return range[0] <= food <= range[1]

def parse_input(file_path: str) -> Tuple[List[Tuple[int, int]], List[int]]:
    ranges: List[Tuple[int, int]] = []
    foods: List[int] = []
    
    with open(file_path, 'r', encoding='utf8') as file:
        content = file.read()
        
    split = content.replace('\r', '').split('\n\n')
    
    if len(split) != 2:
        raise Exception("Invalid file content")
    
    for line in split[0].split('\n'):
        line = line.strip()
        if len((range := line.split('-'))) == 2:
            try:
                ranges.append((int(range[0]), int(range[1])))
            except Exception as e:
                print(f"Could not parse {line} due to:\n{e}")
    
    for line in split[1].split('\n'):
        line = line.strip()
        if len(line) == 0:
            continue
        try: 
            foods.append(int(line))
        except Exception as e:
            print(f"Could not parse {line} due to:\n{e}")
            
    
    return (ranges, foods)
                 
    
    