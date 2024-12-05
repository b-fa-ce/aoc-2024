import functools


def read_data(path: str):
    full_input = []
    with open(path, encoding="utf8") as f:
        for line in f.readlines():
            full_input.append(line.strip("\n"))

    rules = [list(map(int, line.split("|"))) for line in full_input if "|" in line]
    data = [list(map(int, line.split(","))) for line in full_input if "," in line]

    return data, rules


def check_rule(instruction: list[int], rule: list[int, int]) -> bool:
    if rule[0] in instruction and rule[1] in instruction:
        if instruction.index(rule[0]) > instruction.index(rule[1]):
            return False

    return True


def check_rules(instruction: list[int], rules: list[list[int, int]]) -> bool:
    return all([check_rule(instruction, rule) for rule in rules])


def get_confirmed_centre_sum(
    instructions: list[list[int]], rules: list[list[int, int]]
) -> int:
    confirmed_instructions = [inst for inst in instructions if check_rules(inst, rules)]

    centre_elems = []

    for inst in confirmed_instructions:
        if not len(inst) % 2 == 1:
            raise ValueError
        centre_elem = inst[len(inst) // 2]
        centre_elems.append(centre_elem)

    return sum(centre_elems)


def compare(a, b, rules):
    return -1 if [a, b] in rules else 1 if [b, a] in rules else 0


def get_reorderd_centre_sum(instructions, rules):
    unordered_instructions = [
        ins for ins in instructions if not check_rules(ins, rules)
    ]
    sum_total = 0

    for unordered in unordered_instructions:
        ordered = sorted(
            unordered, key=functools.cmp_to_key(lambda x, y: compare(x, y, rules))
        )
        if not len(ordered) % 2 == 1:
            raise ValueError
        sum_total += ordered[len(ordered) // 2]

    return sum_total
