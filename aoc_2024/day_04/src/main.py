from aoc_2024.day_04.src.utils import read_data, count_occurances, count_X_MAS, KEYWORD


def main():
    board = read_data("aoc_2024/day_04/data.csv")

    occurances_1 = count_occurances(board, KEYWORD)
    occurances_2 = count_X_MAS(board)

    print(
        f"""
          occurances 1: {occurances_1}
          occurances 2: {occurances_2}
          """
    )


if __name__ == "__main__":
    main()
