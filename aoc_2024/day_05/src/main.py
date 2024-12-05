from aoc_2024.day_05.src.utils import (
    read_data,
    get_confirmed_centre_sum,
    get_reorderd_centre_sum,
)


def main():
    data, rules = read_data("aoc_2024/day_05/data.csv")
    part_1 = get_confirmed_centre_sum(data, rules)
    part_2 = get_reorderd_centre_sum(data, rules)

    print(
        f"""
            centre-sum of correctly-ordered updates: {part_1}
            centre-sum of correctly ordering incorrectly-ordered updates: {part_2}
            """
    )


if __name__ == "__main__":
    main()
