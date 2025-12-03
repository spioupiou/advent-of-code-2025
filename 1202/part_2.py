import re

with open('input.txt') as f:
    id_ranges = f.readlines()[0].strip('\n').split(',')

total_invalid_ids = 0

def is_repetitive(num):
    length = len(num)
    # Iterate till half the length of the number (pattern cannot be bigger than half the string, because it needs to repeat at least twice)
    for i in range(1, length // 2 + 1): # Example: 123123123 -> 1, 12, 123
        pattern = num[:i]
        is_match = True
        # Check if the pattern repeats for the entire length of the number
        for j in range(i, length, i): # Example: 123123123 -> 123, 123, 123
            current_chunk = num[j:j+i]
            if current_chunk != pattern:
                is_match = False
                break
        if is_match:
            return True
    return False

for id_range in id_ranges:
    first, second = id_range.split('-')
    for id_num in range(int(first), int(second) + 1):
        if is_repetitive(str(id_num)):
            total_invalid_ids += id_num

print(total_invalid_ids)
