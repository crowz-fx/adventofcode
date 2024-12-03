"""
# Author: Lui Crowie
# Task: https://adventofcode.com/2024/day/3
"""

import sys, os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(f"{ROOT_DIR}/../../")

from utils.Utils import Utils
import re

UTILS = Utils()


def part_1(file_contents=[]):
    # for each memory_line there are multiple mul(xxx,xxx)
    # can be up to thre digits in each number, need to multiple
    # print running summation

    summation = 0

    for memory_line in file_contents:
        # making the digits capture groups can then easily suck them out
        matches = re.findall(r"mul\((\d+),(\d+)\)", memory_line)

        if matches:
            for first_num, second_num in matches:
                summation += int(first_num) * int(second_num)

    return summation


def part_2(file_contents=[]):
    # in addition, now check if there is a do() that enables it before hand

    summation = 1

    for memory_line in file_contents:
        # TODO - the non-greedy previous doesn't seem to work...
        matches = re.findall(r"do\(\).*?mul\((\d+),(\d+)\)", memory_line)

        if matches:
            for first_num, second_num in matches:
                summation += int(first_num) * int(second_num)

    return summation


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
