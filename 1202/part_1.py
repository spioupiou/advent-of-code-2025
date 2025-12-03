import re

with open('input.txt') as f:
    id_ranges = f.readlines()[0].strip('\n').split(',')

total_invalid_ids = 0

for id_range in id_ranges:
    first, second = id_range.split('-')
    for id in range(int(first), int(second) + 1):
        mid = len(str(id)) // 2
        if len(str(id)) % 2 == 0 and str(id)[:mid] == str(id)[mid:]:
            print(f"Invalid ID: {id}")
            total_invalid_ids += id

print(total_invalid_ids)
