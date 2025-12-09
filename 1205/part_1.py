import re

with open('input.txt') as f:
    lines = [line.strip() for line in f.readlines()]

split_index = lines.index('')

id_ranges = [range.split('-') for range in lines[:split_index]]
product_ids = [int(num) for num in lines[split_index+1:]]

fresh_products = 0
for product_id in product_ids:
    for id_range in id_ranges:
        first, second = range
        if product_id >= int(first) and product_id <= int(second):
            fresh_products += 1
            break

print(fresh_products)
