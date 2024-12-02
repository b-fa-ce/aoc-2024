from collections import Counter


def read_file(path: str):
    reports = []

    with open(path, "r", encoding="utf8") as f:
        for line in f.readlines():
            line = list(map(int, line.strip("\n").split(" ")))
            reports.append(line)

    return reports


def get_sign(number: int):
    return (number > 0) - (number < 0)


def check_signs(distances: list[int]) -> list[bool]:
    return [
        get_sign(distances[i]) == get_sign(distances[i + 1])
        for i in range(len(distances) - 1)
    ]


def get_distances(report):
    return [report[i + 1] - report[i] for i in range(len(report) - 1)]


def check_steps(distances: list[int]) -> list[bool]:
    return [1 <= abs(dis) <= 3 for dis in distances]


def is_safe_report(report: list[int]) -> bool:
    """
    An report only counts as safe if both of the following are true:
    - The levels are either all increasing or all decreasing.
    - Any two adjacent levels differ by at least one and at most three.
    Input: a report, i.e. list of ints
    Returns: boolean
    """
    # get distances of levels
    distances = get_distances(report)

    # check if in/decrease is within 1 <= distance <= 3
    if not all(check_steps(distances)):
        return False

    # check if the levels are monotoneous
    if not all(check_signs(distances)):
        return False

    return True


def check_safety_dampened(levels_checked: list[bool]) -> bool:
    """
    Checks if the count of False entries in input list is <= 0 and
    Returns True if this is the case
    """
    return Counter(levels_checked)[False] <= 1


def count_safe_reports(reports: list[list[int]], fct) -> int:
    counts = 0

    for report in reports:
        if fct(report):
            counts += 1

    return counts


def is_safe_report_with_dampener(report: list[int]) -> list[int]:
    """
    An report only counts as safe if both of the following are true:
    - The levels are either all increasing or all decreasing.
    - Any two adjacent levels differ by at least one and at most three.

    If removing a single level from an unsafe report would make it safe,
    the report instead counts as safe.

    Input: a report, i.e. list of ints
    Returns: boolean
    """
    # get distances of levels
    distances = get_distances(report)
    steps_checked = check_steps(distances)
    signs_checked = check_signs(distances)

    if all(steps_checked) and all(signs_checked):
        return True

    for i in range(len(report)):
        temp_report = []
        temp_report[:] = report[:]

        del temp_report[i]

        distances = get_distances(temp_report)
        steps_checked = check_steps(distances)
        signs_checked = check_signs(distances)

        if all(steps_checked) and all(signs_checked):
            return True

    return False
