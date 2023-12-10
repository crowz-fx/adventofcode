"""
# Author: Lui Crowie
# Task: https://adventofcode.com/2023/day/7
"""
# Get input from file
with open("2023/day7/input.txt", "r") as file:
  hands = file.readlines()

final_order_of_hands = []

"""
Key - Rank
  7 = five of a kind
  6 = four of a kind
  5 = full house
  4 = three of a kind
  3 = two pair
  2 = one pair
  1 = high card
"""

"""
Part 1
"""
# Find out what each hand is in it's rank
for hand in hands:
  hand, bid = hand.replace("\n", "").split(" ")

  unique = set(hand)  
  unique_count = len(unique)
  rank = 0

  if unique_count == 5: rank = 1 # high card
  elif unique_count == 4: rank = 2 # one pair
  elif unique_count == 3:
    # two pair or three of kind
    for char in hand:
      if hand.count(char) == 3: rank = 4 # three of kind
      elif hand.count(char) == 2: rank = 3 # two pair
  elif unique_count == 2:
    for char in hand:
      if hand.count(char) == 4: rank = 6 # four of kind
      elif hand.count(char) == 3: rank = 5 # full house
  elif unique_count == 1: rank = 7 # five of kind
  
  print(hand, rank)
  final_order_of_hands.append(f"{rank}-{hand}-{bid}")



print(sorted(final_order_of_hands, key=lambda x:x[:1], reverse=True))
