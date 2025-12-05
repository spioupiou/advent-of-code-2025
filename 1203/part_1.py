import re

with open('input.txt') as f:
    lines = f.readlines()

total = 0

for line in lines:
    digits = [int(char) for char in line.strip()]
    max_digit, max_digit_index = 0, None

    for i in range(len(digits)-1):
        if digits[i] > max_digit:
            max_digit, max_digit_index = digits[i], i

    remaining = digits[max_digit_index+1:]
    second_max_digit = max(remaining)

    total += max_digit * 10 + second_max_digit
print(total)
