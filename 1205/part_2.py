import re

with open('input.txt') as f:
    lines = [line.strip() for line in f.readlines()]

split_index = lines.index('')

id_ranges = [range.split('-') for range in lines[:split_index]]
fresh_products = []

for id_range in id_ranges:
    first, second = id_range
    for num in range(int(first), int(second) + 1):
        if num not in fresh_products:
            fresh_products.append(num)

print(len(fresh_products))
