from typing import Callable, TypeVar, List, Optional

T = TypeVar('T')

def parse_input_lines(file_path: str, parser: Callable[[str], Optional[T]]) -> List[T]:
    res: List[T] = list()
    with open(file_path, "r", encoding="utf8") as file:
        for line in file.readlines():
            if (parsed := parser(line)) != None:
                res.append(parsed)
    return res
