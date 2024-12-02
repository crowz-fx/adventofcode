"""
# Author: Lui Crowie
# Task: https://adventofcode.com/2024/day/2
"""

import sys, os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(f"{ROOT_DIR}/../../")

from utils.Utils import Utils

UTILS = Utils()


def part_1(file_contents=[]):
    # for each report, go one by one and check the difference
    #   if it's concurrent i.e. all decreasing or increase, good
    #     for each diff if it's > 3, => not safe
    safe_count = 0

    for report in file_contents:
        report = list(map(int, report.split()))

        # increasing run
        if all((i < j and abs(i - j) <= 3) for i, j in zip(report, report[1:])):
            safe_count += 1

        # decreasing run
        if all((i > j and abs(i - j) <= 3) for i, j in zip(report, report[1:])):
            safe_count += 1

    return safe_count


# TODO - finish and fix
def part_2(file_contents=[]):
    # same as part 1, except if can remove one 'level' it's still safe
    safe_count = 0

    for report in file_contents:
        report = list(map(int, report.split()))

        # increasing run
        bad_levels = 0
        for i, j in zip(report, report[1:]):
            if (i < j and abs(i - j) <= 3) or (i > j and abs(i - j) <= 3):
                bad_levels += 1

        print(bad_levels)

        if bad_levels <= 1:
            safe_count += 1

    return safe_count


if __name__ == "__main__":
    for x in [1, 2]:
        UTILS.run_solution(
            root_dir=ROOT_DIR,
            test_count=1,
            run_tests=True,
            run_input=True,
            part=x,
            solution=locals()[f"part_{x}"],
        )
