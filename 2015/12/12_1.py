import re

with open('input.txt') as file:
    s = ''.join(file.read().splitlines())
result = [int(d) for d in re.findall(r'-?\d+', s)]

print("Part 1: ", sum(result))