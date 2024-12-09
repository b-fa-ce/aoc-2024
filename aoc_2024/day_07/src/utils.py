from itertools import product

def read_data(path: str):
    data = []

    with open(path) as f:
        for line in f.readlines():
            new_line = line.split(': ')
            new_line_2 =  list(map(int,new_line[1].strip('\n').split(' ')))

            data.append([int(new_line[0]), new_line_2])

    return data

def is_correct_value(data_entry: list[int, list[int]], is_part_2: bool = True) -> bool:
    """
    checks wether the list of values concatenated by the operators * and + yields
    value, first entry of data
    """
    return any(eval == data_entry[0] for eval in insert_operators(data_entry[1], is_part_2))



def calibration_result(data, is_part_2: bool = True) -> int:
    return sum([dat[0] for dat in data if is_correct_value(dat, is_part_2)])

def eval_left_to_right(data: list[int], is_part_2: bool = True):

    result = data[0]

    for i in range(1,len(data), 2):
        if data[i] == '+':
            result += data[i+1]
        elif data[i] == '*':
            result *= data[i+1]
        elif is_part_2 and data[i] == '||':
            new_val = int(str(result) + str(data[i+1]))
            result = new_val

    return result

def insert_op(data, ops):
    comb = []

    for i in range(len(data)-1):
        comb.append(data[i])
        comb.append(ops[i])
    comb.append(data[-1])

    return comb

def insert_operators(data: list[int], is_part_2: bool = True):
    if is_part_2:
        ops = [list(itm) for itm in product(['*', '+', '||'], repeat = len(data)-1)]
    else:
        ops = [list(itm) for itm in product(['*', '+'], repeat = len(data)-1)]


    combs = [eval_left_to_right(insert_op(data, op), is_part_2) for op in ops]
    return combs
