import re

with open('input.txt') as f:
    lines = f.readlines()

total_batteries = 12
total_sum = 0

def get_max_digit_in_defined_range(digits, start, end):
    max_digit, max_digit_index = 0, None
    for i in range(start, end):
        if digits[i] > max_digit:
            max_digit, max_digit_index = digits[i], i
    return max_digit, max_digit_index

for line in lines:
    digits = [int(char) for char in line.strip()]

    stop_index = len(digits) - 11 # Need to turn on 12 batteries, so after finding the max we still need to find 11 more
    start_index = 0
    max_digits = []

    while stop_index <= len(digits):
        max_digit, max_digit_index = get_max_digit_in_defined_range(digits, start_index, stop_index)
        max_digits.append(max_digit)
        start_index = max_digit_index + 1
        stop_index += 1

    total_sum += int("".join(map(str, max_digits)))
print(total_sum)
