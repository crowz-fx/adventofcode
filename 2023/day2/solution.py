"""
# Author: Lui Crowie
# Task: https://adventofcode.com/2023/day/2
"""
# Get input from file
with open("2023/day2/input.txt", "r") as file:
  games = file.readlines()

"""
Part 1
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
Part 2
  Same as part 1 but need to work out the max green/red/blue cubes for a game to be
    valid and then multiply it all and then sum

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