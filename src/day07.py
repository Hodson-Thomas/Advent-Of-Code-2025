from typing import List, Tuple, Set, Dict
from enum import Enum

class Tile(Enum):
    Empty = 0
    Source = 1
    Splitter = 2

def part1(file_path: str) -> int:
    board, initial_position = parse_input(file_path)
    
    reached_splitters: Set[Tuple[int, int]] = set()
    visited: Set[Tuple[int, int]] = set()
    
    def part1_aux(position: Tuple[int, int]):
        if position in visited:
            return
        
        if position[0] < 0 or position[0] >= len(board[0]) or position[1] < 0 or position[1] >= len(board):
            return
        
        visited.add(position)
            
        if board[position[1]][position[0]] == Tile.Splitter:
            reached_splitters.add(position)
            part1_aux((position[0] - 1, position[1]))
            part1_aux((position[0] + 1, position[1]))
        else:
            part1_aux((position[0], position[1] + 1))
    
    part1_aux(initial_position)
    return len(reached_splitters)

def part2(file_path: str) -> int:
    board, initial_position = parse_input(file_path)
    memoize: Dict[Tuple[int, int], int] = dict()
    
    def part2_aux(position: Tuple[int, int]) -> int:
        
        if (mem := memoize.get(position, None)) is not None:
            return mem
        
        if position[0] < 0 or position[0] >= len(board[0]) or position[1] < 0:
            return 0
        
        if position[1] == len(board) - 1:
            return 1
        
        if board[position[1]][position[0]] == Tile.Splitter:
            val = part2_aux((position[0] - 1, position[1])) + part2_aux((position[0] + 1, position[1]))
            memoize[position] = val
            return val
 
        val = part2_aux((position[0], position[1] + 1))
        memoize[position] = val
        return val
    
    return part2_aux(initial_position)

def parse_input(file_path: str) -> Tuple[List[List[Tile]], Tuple[int, int]]:
    
    source_x = 0
    source_y = 0
    
    board: List[List[Tile]] = []
    
    with open(file_path, 'r', encoding='utf8') as file:
        content = file.read().strip()
        
    for y, line in enumerate(content.split('\n')):
        row: List[Tile] = []
        for x, c in enumerate(line):
            match c:
                case '.':
                    row.append(Tile.Empty)
                case '^':
                    row.append(Tile.Splitter)
                case 'S':
                    source_x = x
                    source_y = y
                    row.append(Tile.Source)
                case _:
                    raise Exception(f"Invalid char ({c}) at position line {y} position {x}")
        board.append(row)
    
    return (board, (source_x, source_y))