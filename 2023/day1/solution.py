"""
# Author: Lui Crowie
# Task: https://adventofcode.com/2023/day/1
"""

# Get input from file
with open("2023/day1/input.txt", "r") as file:
  calibration_document = file.readlines()

"""
Part 1
"""
calibration_sum = 0

for calibration_line in calibration_document:
  # Handle newlines in file
  calibration_line = calibration_line.replace("\n", "")
  
  # Check it's not empty
  if calibration_line:
    captured_numbers = str(int(''.join(filter(str.isdigit, calibration_line))))
    print(f"Numbers captured: {captured_numbers}")
    
    calibration_value = int(captured_numbers)

    # Check if it's two digits
    if len(captured_numbers) > 1:
      # 2 digits so get first and last digit
      calibration_value = int(str(captured_numbers[:1] + captured_numbers[-1:]))
    else:
      # As only one digit need to double it up so 1 ==> 11
      calibration_value = int(str(captured_numbers + captured_numbers))

    print(f"Calibration value: {calibration_value}")
    calibration_sum += calibration_value

print(f"Part 1 - Final count: {calibration_sum}") # 54630

"""
Part 2 - Same as part one but we need to convert words to numbers like one ==> 1, then
  do process to check first and last number
"""
additional_calibration_sum = 0

for calibration_line in calibration_document:
  # Handle newlines in file
  calibration_line = calibration_line.replace("\n", "")
  print(f"Full line: [{calibration_line}], ", end="")
  
  # Part 2 - Start
  numbers_in_text = [
    "one", 
    "two", 
    "three", 
    "four", 
    "five", 
    "six", 
    "seven",
    "eight", 
    "nine"
  ]
  for number_in_text in numbers_in_text:
    """
      There are examples like 'eightwo' so add in the number but put back the text too,
        so eighttwo ==> eight8eightwo so then next goes through the twos
        so eight8eightwo ==> eight8eightwo2two
    """
    calibration_line = calibration_line.replace(
      number_in_text, # one
      f"{number_in_text}{numbers_in_text.index(number_in_text) + 1}{number_in_text}" # as one is first in array so + 1
    )
  # Part 2 - End

  # Check it's not empty
  if calibration_line:
    print(f"Modded line: [{calibration_line}], ", end="")
    captured_numbers = str(int(''.join(filter(str.isdigit, calibration_line))))
    print(f"Numbers captured: [{captured_numbers}], ", end="")
    
    calibration_value = int(captured_numbers)

    # Check if it's two digits
    if len(captured_numbers) > 1:
      # 2 digits so get first and last digit
      calibration_value = int(str(captured_numbers[:1] + captured_numbers[-1:]))
    else:
      # As only one digit need to double it up so 1 ==> 11
      calibration_value = int(str(captured_numbers + captured_numbers))

    print(f"Calibration value: [{calibration_value}]")
    additional_calibration_sum += calibration_value

print(f"Part 2 - Final count: {additional_calibration_sum}") # 54770
