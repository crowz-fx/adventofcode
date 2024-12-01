"""
# Author: Lui Crowie
# Task: https://adventofcode.com/2024/day/1
"""

import sys, os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(f"{ROOT_DIR}/../../")

from utils.Utils import Utils

UTILS = Utils()


def split_lists(list_contents):
    left_list, right_list = [], []

    # split the numbers into their left and right list
    for line in list_contents:
        left, right = map(int, line.split())

        left_list.append(left)
        right_list.append(right)

    # UTILS.out(left_list)
    # UTILS.out(right_list)
    return left_list, right_list


def part_1(file_contents=[]):
    left_list, right_list = split_lists(file_contents)

    # sort lists
    left_list.sort()
    right_list.sort()

    # for each 'pair' work out the diff and sum to get total distance
    running_sum = 0
    for idx, x in enumerate(left_list):
        running_sum += abs(x - right_list[idx])

    # UTILS.out(running_sum)
    return running_sum


def part_2(file_contents=[]):
    left_list, right_list = split_lists(file_contents)

    running_sum = 0
    for number in left_list:
        running_sum += number * right_list.count(number)

    return running_sum


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
