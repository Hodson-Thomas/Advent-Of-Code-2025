from typing import List, Tuple
from enum import Enum

class Operators(Enum):
    Add = 0
    Mul = 1
    
def part1(file_path: str) -> int:
    board, operators = parse_input(file_path)
    base = [1 if operator == Operators.Mul else 0 for operator in operators]
    for row in board:
        for i in range(0, len(base)):
            match operators[i]:
                case Operators.Add:
                    base[i] += row[i]
                case Operators.Mul:
                    base[i] *= row[i]
    return sum(base)

def part2(file_path: str) -> int:
    board, operators = parse_part2(file_path)
    total = 0
    for i in range(len(operators)):
        match operators[i]:
            case Operators.Add:
                total += sum(board[i])
            case Operators.Mul:
                temp = 1
                for val in board[i]:
                    temp *= val
                total += temp
    return total

def parse_input(file_path: str) -> Tuple[List[List[int]], List[Operators]]:
    operators: List[Operators] = []
    board: List[List[int]] = []
    
    with open(file_path, 'r', encoding='utf8') as file:
        content = file.read().strip().split('\n')
    
    for c in content[-1].replace(' ', ''):
        match c:
            case '+':
                operators.append(Operators.Add)
            case '*':
                operators.append(Operators.Mul)
            case _:
                raise Exception(f"Invalid operator ({c}) found")
    
    for line in content[:-1]:
        row: List[int] = []
        for item in clean_line(line.strip()).split(' '):
            row.append(int(item))
        assert (len(row) == len(operators))
        board.append(row)
    
    return (board, operators)

def parse_part2(file_path: str) -> Tuple[List[List[int]], List[Operators]]:
    with open(file_path, 'r', encoding='utf8') as file:
        content = file.read().split('\n')

    operators: List[Operators] = []

    for c in content[-1].replace(' ', ''):
        match c:
            case '+':
                operators.append(Operators.Add)
            case '*':
                operators.append(Operators.Mul)
            case _:
                raise Exception(f"Invalid operator ({c}) found")

    board_str: List[List[str]] = [
        [c for c in line]
        for line in content[:-1]
    ]
    
    board_str_joined: List[List[str]] = []
    
    temp = ["" for _ in range(len(board_str))]
    for i in range(len(board_str[0])):
        if is_empty_col(board_str, i):
            board_str_joined.append(temp)
            temp = ["" for _ in range(len(board_str))]
            continue
        for r in range(len(board_str)):
            temp[r] += board_str[r][i]
    board_str_joined.append(temp)
    
    board = [transform_row(row) for row in board_str_joined]
    
    return (board, operators)

def transform_row(row: List[str]) -> List[int]:
    res: List[int] = []
    for i in range(len(row[0])):
        string = ""
        for value in row:
            string += value[i]
        res.append(int(string.strip()))
        
    return res

def is_empty_col(board: List[List[str]], col_index: int) -> bool:
    for row in board:
        if row[col_index] != ' ':
            return False
    return True
            
def clean_line(line: str) -> str:
    res = ""
    previous = ""
    for c in line:
        if c == ' ' and previous == ' ':
            continue
        res += c
        previous = c
    return res
