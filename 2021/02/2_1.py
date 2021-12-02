horizontal = 0
depth = 0

with open('input.txt') as f:
    for line in f.readlines():
        direction, value = line.strip().split()
        value = int(value)
        if direction[0] == 'f':
            horizontal += value
        if direction[0] == 'u':
            depth += value
        if direction[0] == 'd':
            depth -= value

print(abs(horizontal*depth))