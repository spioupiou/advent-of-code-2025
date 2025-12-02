import re

with open('input.txt') as f:
  lines = f.readlines()

start = 50
number_of_0_stops = 0

for line in lines:
    line = line.strip('\n')
    direction = line[0]
    steps = int(line[1:])
    if direction == 'L':
        for i in range(steps):
            start -= 1
            if start < 0:
                start = 99
        # Part 1
        if start == 0:
            number_of_0_stops += 1
            # # Part 2
            # if start == 0:
            #     number_of_0_stops += 1
    else:
        for i in range(steps):
            start += 1
            if start > 99:
                start = 0
        # Part 1
        if start == 0:
            number_of_0_stops += 1
            # # Part 2
            # if start == 0:
            #     number_of_0_stops += 1

print(start)
print(number_of_0_stops)
