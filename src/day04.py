from typing import List, Optional
from src.utils import parse_input_lines


def part1(file_path: str) -> int:
    board = parse_input_lines(file_path, parse_line)
    
    total = 0
    for r in range(0, len(board)):
        for c in range(0, len(board[r])):
            if not board[r][c]: 
                continue

            if count_neighbours(board, r, c) < 4:
                total += 1
    
    return total

def part2(file_path: str) -> int:
    board = parse_input_lines(file_path, parse_line)
    total = 0
    has_remove_roll = True
    while has_remove_roll:
        has_remove_roll = False
        new_board = [[tile for tile in row] for row in board]
        for r in range(0, len(board)):
            for c in range(0, len(board[r])):
                if not board[r][c]: 
                    continue
                if count_neighbours(board, r, c) < 4:
                    has_remove_roll = True
                    new_board[r][c] = False
                    total += 1
        board = new_board
    return total

def count_neighbours(board: List[List[bool]], row: int, col: int) -> int:
    total = 0
    for r in range(max(0, row - 1), min(len(board), row + 2)):
        for c in range(max(0, col - 1), min(len(board[0]), col + 2)):
            if r == row and c == col:
                continue
            if board[r][c]:
                total += 1
    return total
    
def parse_line(line: str) -> Optional[List[bool]]:
    res: List[bool] = []
    for c in line.strip():
        if c == '@':
            res.append(True)
        elif c == '.':
            res.append(False)
        else:
            return None
    return res
