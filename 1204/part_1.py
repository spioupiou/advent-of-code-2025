import re

with open('input.txt') as f:
    lines = f.readlines()

breakdown_lines = [[char for char in line.strip()] for line in lines]

directions = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1),           (0, 1),
    (1, -1),  (1, 0),  (1, 1),
]

rows = len(breakdown_lines)
cols = len(breakdown_lines[0])

reachable_rolls = 0
for i, line in enumerate(breakdown_lines):
    for j, char in enumerate(line):
        adjacent_rolls = 0
        if char == '@':
            for dy, dx in directions:
                new_i, new_j = i + dy, j + dx
                if 0 <= new_i < rows and 0 <= new_j < cols:
                    if breakdown_lines[new_i][new_j] == '@':
                        adjacent_rolls += 1
            if adjacent_rolls < 4:
                reachable_rolls += 1

print(reachable_rolls)
