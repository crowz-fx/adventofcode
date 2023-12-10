# !/usr/bin/env python3
"""
# Author: Lui Crowie
# Task: https://adventofcode.com/2023/day/9
"""
import sys, os
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(f"{ROOT_DIR}/../../")

from utils.Utils import Utils
UTL = Utils()

def solution(file_contents=[]):
  # print(file_contents)
  UTL.dun("hi")
  return 114

if __name__ == '__main__': 
  UTL.run_solution(
    root_dir=ROOT_DIR,
    test_count=1,
    run_tests=True,
    run_input=False,
    solution=solution
  )
