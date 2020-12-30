from copy import deepcopy

with open('input.txt') as file:
    f = file.read().splitlines()
    layout = [list(row) for row in f]

directions = [
    [-1,1],  [0,1],  [1,1],
    [-1,0],  [0,0],  [1,0],
    [-1,-1], [0,-1], [1,-1]
]

n = len(layout)

layout[0][0] = '#'
layout[0][n-1] = '#'
layout[n-1][0] = '#'
layout[n-1][n-1] = '#'

for _ in range(100):
    
    n_table = [ [0 for _ in range(n)] for _ in range(n)]
    new_layout = deepcopy(layout)

    
    for y in range(n):
        for x in range(n):
            
            active = 0
            for d in directions:
                dy, dx = d
                try:
                    if dx == 0 and dy == 0:
                        pass
                    elif dy+y in range(n) and dx+x in range(n):
                            if dx == 0 and dy == 0:
                                continue
                            else:
                                if layout[dy+y][dx+x] == "#":
                                    active += 1
                except IndexError:
                    pass
            
            n_table[y][x] = active

            if layout[y][x] == '#' and active not in [2,3]:
                new_layout[y][x] = '.'
            if layout[y][x] == '.' and active == 3:
                new_layout[y][x] = '#'
    
    new_layout[0][0] = '#'
    new_layout[0][n-1] = '#'
    new_layout[n-1][0] = '#'
    new_layout[n-1][n-1] = '#'

    layout = new_layout

on = 0
for row in layout:
    on += row.count('#')

print('Part 2: ', on)

    