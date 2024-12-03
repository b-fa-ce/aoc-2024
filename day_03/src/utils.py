import re


def read_file(path: str):
    data = []

    with open(path, "r", encoding="utf8") as f:
        for line in f.readlines():
            line_1 = line.strip("\n")
            data.append(line_1)
    return "".join(data)


def find_matches(input_string: str) -> list[str]:
    """
    finds matches and returns list of matches
    """
    pattern = re.compile(r"mul\(\d+,\d+\)")

    return pattern.findall(input_string)


def find_matches_with_activation(input_string: str) -> list[str]:
    """
    finds matches and returns list of matches
    """
    pattern = re.compile(r"mul\(\d+,\d+\)|do\(\)|don\'t\(\)")

    return pattern.findall(input_string)


def mul(num_1: int, num_2: int) -> int:
    """
    mutliplies num_1 with num_2
    """
    return num_1 * num_2


def get_sum(input_string: str) -> int:
    """
    returns sum of all multiplications (mul(x,y)) in input string
    """
    return sum(map(eval, find_matches(input_string)))


def filter_input(input_list: list) -> list:
    """
    checks if there is a "don't()" and removes the next elements in list
    until the next "do()"
    """
    is_activated = True

    return [
        elem
        for elem in input_list
        if not (elem == "don't()" and (is_activated := False))
        and not (elem == "do()" and (is_activated := True))
        and is_activated
    ]


def get_sum_with_activation(input_string: str) -> int:
    """
    returns sum of all multiplications (mul(x,y)) in input string with activation do()
    """
    matches = find_matches_with_activation(input_string)
    filtered_matches = filter_input(matches)

    return sum(map(eval, filtered_matches))
