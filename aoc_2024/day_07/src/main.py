from aoc_2024.day_07.src.utils import read_data, calibration_result


def main():
    data = read_data("aoc_2024/day_07/data.csv")
    part_1 = calibration_result(data, is_part_2=False)
    part_2 = calibration_result(data, is_part_2=True)

    print(
        f"""
            calibration result: {part_1}
            calibration result with concatenation: {part_2}
            """
    )


if __name__ == "__main__":
    main()
