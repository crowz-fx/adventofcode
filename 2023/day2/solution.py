"""
# Author: Lui Crowie
# Task: https://adventofcode.com/2023/day/2

Snippet of task:
  You play several games and record the information from each game (your puzzle input). 
  Each game is listed with its ID number (like the 11 in Game 11: ...) followed by a 
    semicolon-separated list of subsets of cubes that were revealed from the bag 
    (like 3 red, 5 green, 4 blue).

  For example, the record of a few games might look like this:
    Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
    Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
    Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
    Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
    Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green

  In game 1, three sets of cubes are revealed from the bag (and then put back again). 
  The first set is 3 blue cubes and 4 red cubes; the second set is 1 red cube, 2 green cubes, 
    and 6 blue cubes; the third set is only 2 green cubes.

  The Elf would first like to know which games would have been possible if the bag contained 
    only 12 red cubes, 13 green cubes, and 14 blue cubes?

  In the example above, games 1, 2, and 5 would have been possible if the bag had been loaded 
    with that configuration. However, game 3 would have been impossible because at one point the 
    Elf showed you 20 red cubes at once; similarly, game 4 would also have been impossible because 
    the Elf showed you 15 blue cubes at once. If you add up the IDs of the games that would have 
    been possible, you get 8.

  Determine which games would have been possible if the bag had been loaded with only 12 red cubes, 
    13 green cubes, and 14 blue cubes. What is the sum of the IDs of those games?
"""

# Get input from file
with open("2023/day2/input.txt", "r") as file:
  games = file.readlines()

"""
-------------------------------------------------------------------------------------
Part 1
-------------------------------------------------------------------------------------
"""
game_id_sum = 0
max_red_cubes, max_green_cubes, max_blue_cubes = 12, 13, 14
game_valid = True

for game_record in games:
  # Handle newlines in file
  game_id, game = game_record.replace("\n", "").split(":")
  game_id = int(game_id.split(" ")[1])

  # Break game into the sets of each game
  game_sets = game.split(";")
  print(f"Game [{game_id}] has {len(game_sets)} sets")

  game_valid = True
  for set in game_sets:
    set_colour_str = set.split(",")
    for colour_set in set_colour_str:
      cube_count, colour = colour_set.lstrip().split(" ")
      
      if colour == "green" and int(cube_count) > max_green_cubes: game_valid = False; continue
      if colour == "blue" and int(cube_count) > max_blue_cubes: game_valid = False; continue
      if colour == "red" and int(cube_count) > max_red_cubes: game_valid = False; continue
      
  # Counts match so add the game ID to the tally
  if game_valid: game_id_sum += game_id

print(f"Part 1 - Sum of game IDs: {game_id_sum}") # 2377

"""
-------------------------------------------------------------------------------------
Part 2
   Same as part 1 but need to work out the max green/red/blue cubes for a game to be
     valid and then multiply it all and then sum
-------------------------------------------------------------------------------------
"""
additional_game_id_sum = 0

for game_record in games:
  # Handle newlines in file
  game_id, game = game_record.replace("\n", "").split(":")
  game_id = int(game_id.split(" ")[1])

  min_green_cubes, min_red_cubes, min_blue_cubes = 1, 1, 1

  # Break game into the sets of each game
  game_sets = game.split(";")
  print(f"Game [{game_id}] has {len(game_sets)} sets")

  for set in game_sets:
    set_colour_str = set.split(",")
    for colour_set in set_colour_str:
      cube_count, colour = colour_set.lstrip().split(" ")
      
      # Part 2 - Start
      if colour == "green" and int(cube_count) > min_green_cubes: min_green_cubes = int(cube_count)
      if colour == "blue" and int(cube_count) > min_blue_cubes: min_blue_cubes = int(cube_count) 
      if colour == "red" and int(cube_count) > min_red_cubes: min_red_cubes = int(cube_count) 
  
  additional_game_id_sum += (min_green_cubes * min_blue_cubes * min_red_cubes)
  # Part 2 - End

print(f"Part 2 - Power of cubes for each game: {additional_game_id_sum}") # 71220