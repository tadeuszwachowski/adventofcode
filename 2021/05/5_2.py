import math

# generate grid
SIZE = 1000
grid = [[0 for _ in range(SIZE)] for _ in range(SIZE)]
with open('input.txt') as f:
    for line in f.readlines():
        # unpack values and parse to int
        A,B = line.strip().split(' -> ')
        x1,y1 = [int(n) for n in A.split(',')]
        x2,y2 = [int(n) for n in B.split(',')]
        # print(f"({x1},{y1}) -> ({x2},{y2})")

        # calculate the direction of x and y
        if x2 > x1:
            dx = 1
        elif x2 == x1:
            dx = 0
        else:
            dx = -1

        if y2 > y1:
            dy = 1
        elif y2 == y1:
            dy = 0
        else:
            dy = -1
        
        # calculate the distance between points
        if x1 == x2:
            d = abs(y2-y1) + 1
        elif y1 == y2:
            d = abs(x2-x1) + 1
        else:
            d = abs(y2-y1) + 1
        
        # iterate through the line
        x = x1
        y = y1
        for i in range(d):
            grid[y][x] = grid[y][x] + 1
            x += dx
            y += dy
        # for row in grid:
        #     print(''.join(['.' if x==0 else str(x) for x in row])) 
        # print("#"*30)

# count all the intersections
count = 0
for i in range(SIZE):
    for j in range(SIZE):
        if grid[i][j] > 1:
            count += 1
            
print(count)