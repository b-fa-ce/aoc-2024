from collections import Counter
from custom_types import datalist, UnequalLengthError

def read_file(path: str) -> tuple[datalist, datalist]:
    data_list_1 = []
    data_list_2 = []

    with open(path, 'r', encoding='utf8') as f:
        for line in f.readlines():
            line_1, line_2 = line.strip('\n').split('   ')
            data_list_1.append(line_1)
            data_list_2.append(line_2)

    return data_list_1, data_list_2


def get_total_distance(data_1: datalist, data_2: datalist) -> int:
    """
    Calculate the total distance of the data set
    """
    if len(data_1) != len(data_2):
        raise UnequalLengthError("Data lists of unequal length.")

    d_1 = sorted(data_1)
    d_2 = sorted(data_2)

    distances = [abs(int(d_1[i]) - int(d_2[i])) for i in range(len(d_1))]

    return sum(distances)

def get_similiarity_score(data_1: datalist, data_2: datalist) -> int:
    """
    Get similiarity score
    """
    if len(data_1) != len(data_2):
        raise UnequalLengthError("Data lists of unequal length.")

    counts = Counter(data_2)

    similarities = [int(location) * counts[location] for location in data_1]

    return sum(similarities)
