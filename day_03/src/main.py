from day_03.src.utils import read_file, get_sum, get_sum_with_activation

if __name__ == "__main__":
    input_data = read_file("day_03/data.csv")

    sum_mult = get_sum(input_data)
    sum_mult_activated = get_sum_with_activation(input_data)

    print(
        f"""
          sum: {sum_mult}
          sum activated: {sum_mult_activated}"""
    )
