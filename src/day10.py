from src.utils import parse_input_lines
from typing import Optional, List, Tuple, Set
import sys

class Button:
    def __init__(self, index: List[int]):
        self.index = index
        
    def transform(self, pattern: List[bool]) -> List[bool]:
        res = pattern[:]
        for i in self.index:
            res[i] = not res[i]
        return res
    
    def transform_voltage(self, pattern: List[int]) -> List[int]:
        res = pattern[:]
        for i in self.index:
            res[i] += 1
        return res
    
    def __str__(self) -> str:
        return f"{self.index}"
            
class Machine:
    def __init__(self, lights_pattern: List[bool], buttons: List[Button], voltages: List[int]):
        self.lights_pattern = lights_pattern
        self.buttons = buttons
        self.voltages = voltages
    
    def initial_situation(self) -> List[bool]:
        return [False for _ in self.lights_pattern]
    
    def initial_voltages(self) -> List[int]:
        return [0 for _ in self.voltages]

    def print(self):
        print(f"{self.lights_pattern} ({(", ".join(map(str, self.buttons)))})")

def part1(file_path: str) -> int:
    machines = parse_input_lines(file_path, parse_line)
    
    total = 0
    for machine in machines:
        total += solve1(machine)
    return total

def part2(file_path: str) -> int:
    machines = parse_input_lines(file_path, parse_line)
    
    total = 0
    for machine in machines:
        total += solve2(machine)
    return total

def solve2(machine: Machine) -> int:
    
    def rec_solve1(pattern: List[int], count: int, current_min: int, states: Set[Tuple[int, ...]])-> int:
        to_tuple = tuple(pattern)
        
        if pattern == machine.lights_pattern:
            return count
        
        if to_tuple in states:
            return sys.maxsize
        
        if count > current_min:
            return sys.maxsize
        
        m = current_min
        states.add(to_tuple)
        for button in machine.buttons:
            m = min(m, rec_solve1(button.transform_voltage(pattern), count + 1, m, states.copy()))
        return m
    
    return rec_solve1(machine.initial_voltages(), 0, sys.maxsize, set())

def solve1(machine: Machine) -> int:
    
    def rec_solve1(pattern: List[bool], count: int, current_min: int, states: Set[Tuple[bool, ...]])-> int:
        to_tuple = tuple(pattern)
        
        if pattern == machine.lights_pattern:
            return count
        
        if to_tuple in states:
            return sys.maxsize
        
        if count > current_min:
            return sys.maxsize
        
        m = current_min
        states.add(to_tuple)
        for button in machine.buttons:
            m = min(m, rec_solve1(button.transform(pattern), count + 1, m, states.copy()))
        return m
    
    return rec_solve1(machine.initial_situation(), 0, sys.maxsize, set())

def parse_line(line: str) -> Optional[Machine]:
    content = line.strip().split(' ')
    try:
        return Machine(
            lights_pattern=[c == '#' for c in content[0].replace('[', '').replace(']', '')],
            buttons=[
                Button([int(string) for string in button.replace('(', '').replace(')', '').split(',')])
                for button in content[1:-1]    
            ],
            voltages=[int(string) for string in content[-1].replace('{', '').replace('}', '').split(',')]
        )
    except Exception as e:
        print(f"Could not parse line <{line}> due to:\n{e}")
        return None
    