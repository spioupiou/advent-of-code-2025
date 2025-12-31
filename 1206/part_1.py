import math

with open('input.txt') as f:
    lines = [line.strip() for line in f.readlines()]

operations = []
for i, line in enumerate(lines):
    if i == len(lines) - 1:
        operations.append(line.split())
    else:
        operations.append([int(num) for num in line.split()])

rows_count = len(operations)
cols_count = len(operations[0])

total = 0

for j in range(cols_count):
    new_row = []
    for i in range(rows_count):
        new_row.append(operations[i][j])
    if new_row[-1] == '+':
        total += sum(new_row[:-1])
    elif new_row[-1] == '*':
        total += math.prod(new_row[:-1])

print(total)
