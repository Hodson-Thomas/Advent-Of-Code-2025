from src.utils import parse_input_lines
from typing import Optional, Tuple, List
from enum import Enum

class Tile(Enum):
    Red = 0
    Green = 1
    Other = 2
    
def part1(file_path: str) -> int:
    points = parse_input_lines(file_path, parse_line)
    max = 0
    for i in range(0, len(points) - 1):
        for j in range(i + 1, len(points)):
            area = compute_area(points[i], points[j])
            if area > max:
                max = area
    return max

def part2(file_path: str) -> int:
    points = parse_input_lines(file_path, parse_line)
    b = Board(points)
    b.print_board()
    max = 0
    for i in range(len(points) - 1):
        for j in range(i + 1, len(points)):
            if b.valid_area(points[i], points[j]):
                area = compute_area(points[i], points[j])
                if area > max:
                    max = area
    return max

class Board:
    def __init__(self, points: List[Tuple[int, int]]) -> None:
        self.min_x = min(map(lambda point : point[0], points))
        self.max_x = max(map(lambda point : point[0], points))
        self.min_y = min(map(lambda point : point[1], points))
        self.max_y = max(map(lambda point : point[1], points))
        
        print(self.min_x)
        print(self.max_x)
        print(self.min_y)
        print(self.max_y)
        
        self.board = [
            [Tile.Other for _ in range(self.max_x - self.min_x + 1)]
            for _ in range(self.max_y - self.min_y + 1)
        ]
        
        for i in range(0, len(points) - 1):
            x1, y1 = points[i]
            x1 -= self.min_x
            y1 -= self.min_y
            x2, y2 = points[i + 1]
            x2 -= self.min_x
            y2 -= self.min_y
            self.board[y1][x1] = Tile.Red
            self.board[y2][x2] = Tile.Red
            if x1 == x2:
                for y in range(min(y1, y2) + 1, max(y1, y2)):
                    self.board[y][x1] = Tile.Green
            elif y1 == y2:
                for x in range(min(x1, x2) + 1, max(x1, x2)):
                    self.board[y1][x] = Tile.Green
            else:
                raise Exception("Undefined behavior")
        
        x1, y1 = points[-1]
        x1 -= self.min_x
        y1 -= self.min_y
        x2, y2 = points[0]
        x2 -= self.min_x
        y2 -= self.min_y
        self.board[y1][x1] = Tile.Red
        self.board[y2][x2] = Tile.Red
        if x1 == x2:
            for y in range(min(y1, y2) + 1, max(y1, y2)):
                self.board[y][x1] = Tile.Green
        elif y1 == y2:
            for x in range(min(x1, x2) + 1, max(x1, x2)):
                self.board[y1][x] = Tile.Green
        else:
            raise Exception("Undefined behavior")
        
        self.fill_board(1000, 1000)
        
    def fill_board(self, x: int, y: int):
        if y < 0 or y >= len(self.board):
            return
        if x < 0 or x >= len(self.board[y]):
            return
        
        if self.board[y][x] != Tile.Other:
            return
        
        self.board[y][x] = Tile.Green
        self.fill_board(x + 1, y)
        self.fill_board(x - 1, y)
        self.fill_board(x, y + 1)
        self.fill_board(x, y - 1)
        
    def valid_area(self, p1: Tuple[int, int], p2: Tuple[int, int]) -> bool:
        x_min = min(p1[0], p2[0]) - self.min_x
        x_max = max(p1[0], p2[0]) - self.min_x
        y_min = min(p1[1], p2[1]) - self.min_y
        y_max = max(p1[1], p2[1]) - self.min_y
        for y in range(y_min, y_max + 1):
            for x in range(x_min, x_max + 1):
                if self.board[y][x] == Tile.Other:
                    return False 
        return True
                    
    def print_board(self):
        print("")
        for row in self.board:
            for c in row:
                match c:
                    case Tile.Red: print('#', end='')
                    case Tile.Green: print('X', end='')
                    case _: print('.', end='') 
            print('')
        print("")            
                
def compute_area(point1: Tuple[int, int], point2: Tuple[int, int]) -> int:
    max_x = max(point1[0], point2[0])
    min_x = min(point1[0], point2[0])
    max_y = max(point1[1], point2[1])
    min_y = min(point1[1], point2[1])
    return (max_x - min_x + 1) * (max_y - min_y + 1)

def parse_line(line: str) -> Optional[Tuple[int, int]]:
    content = line.strip().split(',')
    try:
        return (
            int(content[0]),
            int(content[1])
        )
    except Exception as e:
        print(f"Could not parse line <{line}> due to:\n{e}")
        return None
