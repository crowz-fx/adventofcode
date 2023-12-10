# !/usr/bin/env python3
"""
# Author: Lui Crowie
# Task: https://adventofcode.com/2023/day/10
"""
import sys, os
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(f"{ROOT_DIR}/../../")

from utils.Utils import Utils
UTL = Utils()

def solution(file_contents=[]):
  # TODO - write me!
  pass

if __name__ == '__main__': 
  UTL.run_solution(
    root_dir=ROOT_DIR,
    test_count=2,
    run_tests=True,
    run_input=False,
    solution=solution
  )
