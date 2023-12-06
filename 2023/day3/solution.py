"""
# Author: Lui Crowie
# Task: https://adventofcode.com/2023/day/3

Snippet of task:
  The engine schematic (your puzzle input) consists of a visual representation of the engine. 
    There are lots of numbers and symbols you don't really understand, but apparently any 
    number adjacent to a symbol, even diagonally, is a "part number" and should be included 
    in your sum. (Periods (.) do not count as a symbol.)

  Here is an example engine schematic:
    467..114..
    ...*......
    ..35..633.
    ......#...
    617*......
    .....+.58.
    ..592.....
    ......755.
    ...$.*....
    .664.598..

  In this schematic, two numbers are not part numbers because they are not adjacent to a 
    symbol: 114 (top right) and 58 (middle right). Every other number is adjacent to a symbol 
    and so is a part number; their sum is 4361.

  Of course, the actual engine schematic is much larger. What is the sum of all of the part 
    numbers in the engine schematic?
"""

# Get input from file
with open("2023/day3/input.txt", "r") as file:
  schematic_lines = file.readlines()

"""
-------------------------------------------------------------------------------------
Part 1
-------------------------------------------------------------------------------------
"""
part_number_sumation = 0

# Process to get all symbols in the file
symbols = []
numbers = []
symbol_exclusions = ["."]

for i in range(0, 10): numbers.append(str(i)) # add nunbers
for i in numbers: symbol_exclusions.append(str(i)) # add numbers to exclusion list

print(f"Numbers: {numbers}")
print(f"Symbol exclusions: {symbol_exclusions}")

for line in schematic_lines:
  for char in line:
    if char not in symbol_exclusions: 
      if char not in symbols and char != '\n': symbols.append(char)

print(f"Symbols - {symbols}")

"""
 Process explained - Go through each line, when you get to a number, capture the co-ords of 
   the number startx, starty like 0,2 till endx, endy like 0,5 then check for symbols in a 
   rectangle with a height and width of one char larger so 0,1 1,1 1,2 1,3 1,4 1,5 1,6 and 0,6
   if symbol then add, if not move on to next number
"""

for line_index, line in enumerate(schematic_lines):
  line = line.replace("\n", "") # remove newline ofc

  x1, y1 = 0, 0 # number start
  x2, y2 = 0, 0 # number end
  number_start = False
  number = ""

  for char_index, char in enumerate(line):
    if char in numbers and char != '.':
      # we're at the start or middle of a number
      number += char
      if not number_start:
        # confirmed, it's the start
        x1 = char_index
        y1 = line_index
        number_start = True
    else:
      # we've finished the number, reset and process rectangle around
      if number_start:
        x2 = char_index
        y2 = line_index
        # print(number, x1, y1, x2, y2, ">>>", schematic_lines[y1][x1:x2])
        
        # check rectangle around
        look_start_x = x1 - 1 #0 if x1 == 0 else x1 - 1
        look_start_y = y1 - 1 #0 if y1 == 0 else y1 - 1
        look_end_x = x2 + 1 #len(line) if x2 + 1 >= len(line) else  x2 + 1
        look_end_y = y2 + 1 #len(schematic_lines) if y2 + 1 >= len(schematic_lines) else y2 + 1

        # print(look_start_x, look_start_y, look_end_x, look_end_y)

        found_symbol = False
        for check_line in schematic_lines[look_start_y -1 : look_end_y + 1]: # one past the index you want
          for check_char in check_line[look_start_x:look_end_x]:
            if check_char in symbols:
              # print(check_char)
              found_symbol = True

        if found_symbol: part_number_sumation += int(number)
        # print(part_number_sumation)

        number = ""
        number_start = False
  

print(f"Final sumation: {part_number_sumation}")
