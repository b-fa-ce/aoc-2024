import sys

sys.setrecursionlimit(10000)  # Default is usually 1000


def read_data(path: str):
    data = []
    with open(path, encoding="utf8") as f:
        for line in f.readlines():
            data.append(line.strip("\n"))
    return data


def find_current_position(data):
    for i, row in enumerate(data):  # 'i' is the index, 'row' is the element in 'data'
        if "^" in row:
            hor_idx = row.index("^")
            return i, hor_idx
    raise ValueError("'^' not found in the data")  # Raise an error if '^' is not found


def move(data, direction: str = "up"):
    vert_idx, hor_idx = find_current_position(data)

    if (
        vert_idx < len(data) - 1
        and vert_idx > 0
        and hor_idx < len(data[0]) - 1
        and hor_idx > 0
    ):
        current_line = data[vert_idx]
        next_line = data[vert_idx + 1]
        previous_line = data[vert_idx - 1]

        if direction == "up":
            current_line, previous_line, direction = move_up(
                current_line, previous_line
            )

            data[vert_idx] = current_line
            data[vert_idx - 1] = previous_line

        elif direction == "right":
            current_line, next_line, direction = move_right(current_line, next_line)

            data[vert_idx] = current_line
            data[vert_idx + 1] = next_line

        elif direction == "down":
            current_line, next_line, direction = move_down(current_line, next_line)

            data[vert_idx] = current_line
            data[vert_idx + 1] = next_line

        elif direction == "left":
            current_line, previous_line, direction = move_left(
                current_line, previous_line
            )

            data[vert_idx] = current_line
            data[vert_idx - 1] = previous_line

        data = move(data, direction)
    return data


def move_up(current_line, previous_line):

    direction = "up"

    pos = current_line.index("^")
    current_line = current_line.replace("^", "X")

    if previous_line[pos] != "#":
        p_list = [char for char in previous_line]
        p_list[pos] = "^"
        previous_line = "".join(p_list)
    else:
        c_list = [char for char in current_line]
        c_list[pos + 1] = "^"
        current_line = "".join(c_list)
        direction = "right"

    return current_line, previous_line, direction


def move_down(current_line, next_line):

    direction = "down"

    pos = current_line.index("^")
    current_line = current_line.replace("^", "X")

    if next_line[pos] != "#":
        p_list = [char for char in next_line]
        p_list[pos] = "^"
        next_line = "".join(p_list)
    else:
        c_list = [char for char in current_line]
        c_list[pos - 1] = "^"
        current_line = "".join(c_list)
        direction = "left"

    return current_line, next_line, direction


def move_right(current_line, next_line):

    direction = "right"

    pos = current_line.index("^")
    current_line = current_line.replace("^", "X")
    c_list = [char for char in current_line]
    next_elem = current_line[pos + 1]

    if next_elem != "#":
        c_list[pos + 1] = "^"
        current_line = "".join(c_list)
    else:
        n_list = [char for char in next_line]
        n_list[pos] = "^"
        next_line = "".join(n_list)
        direction = "down"

    return current_line, next_line, direction


def move_left(current_line, previous_line):

    direction = "left"

    pos = current_line.index("^")
    current_line = current_line.replace("^", "X")
    c_list = [char for char in current_line]
    prev_elem = current_line[pos - 1]

    if prev_elem != "#":

        c_list[pos - 1] = "^"
        current_line = "".join(c_list)
    else:
        p_list = [char for char in previous_line]
        p_list[pos] = "^"
        previous_line = "".join(p_list)
        direction = "up"

    return current_line, previous_line, direction


def count_positions(data):
    data = move(data)
    return "".join(data).count("X") + 1


def add_position(x, y):
    return (x[0] + y[0], x[1] + y[1])


def get_count_positions(path: str):
    map_guards = {
        (row, column): value
        for row, line in enumerate(open(path))
        for column, value in enumerate(line.strip())
    }

    start, delta = next(p for p in map_guards if map_guards[p] == "^"), (-1, 0)
    visited = {position := start}
    while (next_position := add_position(position, delta)) in map_guards:
        if map_guards[next_position] == "#":
            delta = (delta[1], -delta[0])
        else:
            visited.add(position := next_position)
    return len(visited), visited, map_guards


def find_number_obstacles(visited, map_guards):
    num_obstacles = 0
    start, delta = next(p for p in map_guards if map_guards[p] == "^"), (-1, 0)

    for obstacle in visited - {start}:
        map_guards[obstacle] = "#"
        position, delta = start, (-1, 0)
        seen = {(position, delta)}
        while (next_position := add_position(position, delta)) in map_guards and (
            next_position,
            delta,
        ) not in seen:
            if map_guards[next_position] == "#":
                delta = (delta[1], -delta[0])
            else:
                seen.add((position := next_position, delta))
        map_guards[obstacle] = "."
        if (next_position, delta) in seen:
            num_obstacles += 1
    return num_obstacles
