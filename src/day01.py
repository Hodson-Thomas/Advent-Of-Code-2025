from src.utils import parse_input_lines
from typing import Optional
from enum import Enum
from dataclasses import dataclass

class Rotation(Enum):
    LEFT = 0
    RIGHT = 1

@dataclass
class Instruction:
    rotation: Rotation
    ticks: int

INITIAL_CURSOR = 50
LENGTH = 100

def parse_line(line: str) -> Optional[Instruction]:
    try:
        line = line.strip()
        ticks = int(line[1:])
        match line[0]:
            case 'L':
                return Instruction(rotation=Rotation.LEFT, ticks=ticks)
            case 'R':
                return Instruction(rotation=Rotation.RIGHT, ticks=ticks)
            case _:
                return None
    except Exception as e:
        print(f"Could not parse line due to :\n{e}")        
    
    return None

def part1(file_path: str) -> int:
    instructions = parse_input_lines(file_path, parse_line)
    cursor = INITIAL_CURSOR
    total = 0
    for instruction in instructions:
        match instruction.rotation:
            case Rotation.LEFT:
                cursor = (cursor + (-instruction.ticks + LENGTH)) % LENGTH
            case Rotation.RIGHT:
                cursor = (cursor + instruction.ticks) % LENGTH
            case _:
                raise NotImplementedError(f"{0} not implemented yet.", instruction.rotation)
        if cursor == 0:
           total += 1 
    return total
    
def part2(file_path: str) -> int:
    instructions = parse_input_lines(file_path, parse_line)
    cursor = INITIAL_CURSOR
    total = 0
    for instruction in instructions:
        match instruction.rotation:
            case Rotation.LEFT:
                for _ in range(0, instruction.ticks):
                    cursor = (cursor - 1 + LENGTH) % LENGTH
                    if cursor == 0:
                        total += 1
            case Rotation.RIGHT:
                for _ in range(0, instruction.ticks):
                    cursor = (cursor + 1) % LENGTH
                    if cursor == 0:
                        total += 1
            case _:
                raise NotImplementedError(f"{0} not implemented yet.", instruction.rotation)
        
    return total