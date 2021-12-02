horizontal = 0
depth = 0
aim = 0

with open('input.txt') as f:
    for line in f.readlines():
        direction, value = line.strip().split()
        value = int(value)
        if direction[0] == 'f':
            horizontal += value
            depth += aim*value
        if direction[0] == 'u':
            aim -= value
        if direction[0] == 'd':
            aim += value

print(abs(horizontal*depth))