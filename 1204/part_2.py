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
total_reachable_rolls = 0

def find_reachable_rolls(matrix):
    reachable_roll_coordinates = []
    for i, line in enumerate(matrix):
        for j, char in enumerate(line):
            adjacent_rolls = 0
            if char == '@':
                for dy, dx in directions:
                    new_i, new_j = i + dy, j + dx
                    if 0 <= new_i < rows and 0 <= new_j < cols:
                        if matrix[new_i][new_j] == '@':
                            adjacent_rolls += 1
                if adjacent_rolls < 4:
                    reachable_roll_coordinates.append((i, j))
    return reachable_roll_coordinates

while True:
    reachable_roll_coordinates = find_reachable_rolls(breakdown_lines)

    if len(reachable_roll_coordinates) == 0:
        break

    total_reachable_rolls += len(reachable_roll_coordinates)

    # Replace the reachable rolls with '#'
    for coordinate in reachable_roll_coordinates:
        i, j = coordinate
        breakdown_lines[i][j] = '#'

print(total_reachable_rolls)
