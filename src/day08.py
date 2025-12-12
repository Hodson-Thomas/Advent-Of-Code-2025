from typing import List, Tuple, Optional, Set
from src.utils import parse_input_lines

def part1(file_path: str) -> int:
    connexions = sorted(create_couples(parse_input_lines(file_path, parse_line)), key=distance)
    circuits: List[List[Tuple[int, int, int]]] = []
    
    for i in range(1000):
        (box1, box2) = connexions.pop(0)
        if any([box1 in circuit and box2 in circuit for circuit in circuits]):
            continue
        for circuit in circuits:
            if box1 in circuit:
                for i in range(len(circuits)):
                    if not box2 in circuits[i]:
                        continue
                    circuit.extend(circuits.pop(i))
                    break
                else:
                    circuit.append(box2)
                
                break
            elif box2 in circuit:
                for i in range(len(circuits)):
                    if not box1 in circuits[i]:
                        continue
                    circuit.extend(circuits.pop(i))
                    break
                else:
                    circuit.append(box1)
                break
        else:
            circuits.append([box1, box2])
    
    total = 1
    for v in sorted(map(lambda c : len(c), circuits), reverse=True)[:3]:
        total *= v
        
    return total

def part2(file_path: str) -> int:
    junction_boxes = parse_input_lines(file_path, parse_line)
    connexions = sorted(create_couples(junction_boxes), key=distance)
    circuits: List[List[Tuple[int, int, int]]] = []
    used: Set[Tuple[int, int, int]] = set()
    
    while len(connexions) > 0:
        (box1, box2) = connexions.pop(0)
        if any([box1 in circuit and box2 in circuit for circuit in circuits]):
            continue
        for circuit in circuits:
            if box1 in circuit:
                for i in range(len(circuits)):
                    if not box2 in circuits[i]:
                        continue
                    circuit.extend(circuits.pop(i))
                    break
                else:
                    circuit.append(box2)
                
                break
            elif box2 in circuit:
                for i in range(len(circuits)):
                    if not box1 in circuits[i]:
                        continue
                    circuit.extend(circuits.pop(i))
                    break
                else:
                    circuit.append(box1)
                break
        else:
            circuits.append([box1, box2])
        
        used.add(box1)
        used.add(box2)
        
        if len(circuits) == 1 and len(used) == len(junction_boxes):
            return box1[0] * box2[0]
        
    return -1

def create_couples(junction_boxes: List[Tuple[int, int, int]]) -> List[Tuple[Tuple[int, int, int], Tuple[int, int, int]]]:
    res: List[Tuple[Tuple[int, int, int], Tuple[int, int, int]]] = []
    for i in range(0, len(junction_boxes) - 1):
        for j in range(i + 1, len(junction_boxes)):
            res.append((junction_boxes[i], junction_boxes[j]))
    return res

def distance(points: Tuple[Tuple[int, int, int], Tuple[int, int, int]]) -> float:
    x1, y1, z1 = points[0]
    x2, y2, z2 = points[1]
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2) ** .5

def parse_line(line: str) -> Optional[Tuple[int, int, int]]:
    content = line.strip().split(',')
    if len(content) != 3:
        return None
    try:
        return (
            int(content[0]),
            int(content[1]),
            int(content[2]),
        )
    except Exception as e:
        print(f"Could not parse line <{line}> due to:\n{e}")
    return None
    