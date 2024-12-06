from aoc_2024.day_06.src.utils import (
    read_data,
    count_positions,
    get_count_positions,
    find_number_obstacles,
)


def main():
    data = read_data("aoc_2024/day_06/data.csv")
    part_1 = count_positions(data)
    _, visited, map_guards = get_count_positions("aoc_2024/day_06/data.csv")
    part_2 = find_number_obstacles(visited, map_guards)

    print(
        f"""
            positions guards: {part_1}
            number of obstacles: {part_2}
            """
    )


if __name__ == "__main__":
    main()
