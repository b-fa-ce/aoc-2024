from itertools import product

from aoc_2024.day_04.src.custom_types import direction_type

# Part 1

DIRECTIONS: list[direction_type] = [
    (dx, dy) for dx, dy in product((-1, 0, 1), repeat=2) if (dx, dy) != (0, 0)
]
KEYWORD = "XMAS"


def read_data(path: str):
    data = []

    with open(path, encoding="utf8") as f:
        for line in f.readlines():
            new_line = [char for char in line.strip("\n")]
            data.append(new_line)

    return data


def count_occurances(board: list[list[str]], key_word: str) -> int:
    count = 0
    position = 0

    for i in range(len(board)):
        for j in range(len(board)):
            for direction in DIRECTIONS:
                count += get_occurance(board, key_word, position, i, j, direction)
    return count


def get_occurance(
    board: list[list[str]],
    key_word: str,
    position: int,
    i: int,
    j: int,
    direction: direction_type,
) -> int:

    # if out of bounds return count = 0
    if i >= len(board) or j >= len(board[0]) or i < 0 or j < 0:
        return 0

    # if char on board does not coincide with key_word char return count = 0
    if board[i][j] != key_word[position]:
        return 0

    # if full key_word is found return count = 1
    if position == len(key_word) - 1:
        return 1

    # recursively search board by increasing position and checking directions
    return get_occurance(
        board, key_word, position + 1, i + direction[0], j + direction[1], direction
    )


# Part 2
def count_X_MAS(board: list[list[str]]) -> int:
    count = 0

    for i in range(1, len(board) - 1):
        for j in range(1, len(board[0]) - 1):
            count += is_X_MAS(board, i, j)
    return count


DIRECTIONS_2: list[direction_type] = [(1, 1), (1, -1)]


def is_X_MAS(
    board: list[list[str]],
    i: int,
    j: int,
) -> int:
    """
    M S
     A
    M S
    """

    if board[i][j] != "A":
        return 0

    for dx, dy in DIRECTIONS_2:
        if not (
            (board[i + dx][j + dy] == "M" and board[i - dx][j - dy] == "S")
            or (board[i + dx][j + dy] == "S" and board[i - dx][j - dy] == "M")
        ):
            return 0

    return 1
