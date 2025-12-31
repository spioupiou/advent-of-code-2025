import math

with open('input.txt') as f:
    lines = [line.rstrip('\n') for line in f.readlines()]

# Make sure all lines have the same length (zip stops at the length of the shortest line)
max_len = max(len(line) for line in lines) if lines else 0
padded_lines = [line.ljust(max_len, ' ') for line in lines]

# Transpose!!
## 38
## 93
## 15
## 71
## +
## becomes:
## ('3', '9', '1', '7', '+') ('8', '3', '5', '1', ' ')
columns = list(zip(*padded_lines))

total = 0
current_numbers = []
current_operator = None

# ('3', '9', '1', '7', '+')
# ('8', '3', '5', '1', ' ')
# (' ', ' ', ' ', ' ', ' ')
# ('3', '2', '1', '8', '+')
for j, col in enumerate(columns):
    last_char = col[-1]

    if last_char in ['+', '*']: # ('3', '9', '1', '7', '+')
        # 2nd iteration has no operator inside so skip
        # 3rd iteration has no operator inside so skip
        # 4th iteration: ends with '+' so new group! Sum the numbers, add the total, make a new group
        if current_numbers and current_operator:
            if current_operator == '+':
                total += sum(current_numbers)
            elif current_operator == '*':
                total += math.prod(current_numbers)

        # 1st iteration: no current_numbers and current_operator so no need to sum/multiply, just make a new group
        current_numbers = [] # ['3', '9', '1', '7'] (1st iteration)
        current_operator = last_char # '+' (1st iteration)

    # ('3', '9', '1', '7', '+') -> '3917'
    # ('8', '3', '5', '1', ' ') -> '8351'
    # (' ', ' ', ' ', ' ', ' ') -> ''
    # ('3', '2', '1', '8', '+') -> '3218'
    number_string = ""
    for i in range(len(col)):
        if col[i].isdigit():
            number_string += col[i]

    # Might be empty string if the column is all ''
    if number_string:
        current_numbers.append(int(number_string))

# Sum/multiply the last group!!! (after iterating through all columns)
if current_numbers and current_operator:
    if current_operator == '+':
        total += sum(current_numbers)
    elif current_operator == '*':
        total += math.prod(current_numbers)

print(total)
