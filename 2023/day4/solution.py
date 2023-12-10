"""
# Author: Lui Crowie
# Task: https://adventofcode.com/2023/day/4
"""
# Get input from file
with open("2023/day4/input.txt", "r") as file:
  cards = file.readlines()

"""
Part 1
"""
total_score = 0

for card in cards:
  card = card.replace("\n", "") # remove newline ofc

  winning_numbers, numbers = card.split("|") 
  winning_numbers = list(filter(None, winning_numbers.split(":")[1].split(" ")))
  numbers = list(filter(None, numbers.split(" ")))
  
  print(f"WN {winning_numbers}, NU {numbers}")

  card_total = 0
  for number in numbers:
    if number in winning_numbers:
      if card_total == 0:
        card_total = 1
      else:
        card_total *= 2

  total_score += card_total
  print(f"CT [{card_total}]")

print(f"OVERALL TOTAL [{total_score}]")