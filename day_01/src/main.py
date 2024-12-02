from utils import read_file, get_total_distance, get_similiarity_score

if __name__ == "__main__":
    data_1, data_2 = read_file("data.csv")

    distance = get_total_distance(data_1, data_2)
    similarity_score = get_similiarity_score(data_1, data_2)

    print(
        f"""
          total distance: {distance}
          similarity score: {similarity_score}"""
    )
