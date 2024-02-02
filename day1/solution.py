import re

input_file = open('input.txt')

def compute_calibration_value(line:str) -> int:

    only_digit_string = ''.join([char for char in line if char.isdigit()])
    if len(only_digit_string) > 1:
        return int(only_digit_string[0] + only_digit_string[-1])
    else:
        return int(only_digit_string + only_digit_string)
    

def part1(input_file) -> int:
    return sum([compute_calibration_value(line) for line in input_file])

def replace_literal_with_digit(line:str) -> str:

    constant = {'twone':21, 'eightwo':82, 'nineight':98, 'eighthree':83, 'nineight':98, 'oneight':18, 'zero:':0, 'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six': 6, 'seven':7, 'eight':8, 'nine':9}

    for word, digit in constant.items():
        line = line.replace(word.lower(), str(digit))
    
    return line

def part2(input_lines):

    return sum([compute_calibration_value(replace_literal_with_digit(line)) for line in input_lines])
    


print(part2(input_file))