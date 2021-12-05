# generate grid
SIZE = 1000
grid = [[0 for _ in range(SIZE)] for _ in range(SIZE)]
with open('input.txt') as f:
    for line in f.readlines():
        # unpack values and parse to int
        A,B = line.strip().split(' -> ')
        x1,y1 = [int(n) for n in A.split(',')]
        x2,y2 = [int(n) for n in B.split(',')]

        if x1 == x2 or y1 == y2:
            # iterate through the line
            for a in range(min(x1,x2),max(x1,x2)+1):
                for b in range(min(y1,y2),max(y1,y2)+1):
                    grid[b][a] = grid[b][a] + 1

# count all the intersections
count = 0
for i in range(SIZE):
    for j in range(SIZE):
        if grid[i][j] > 1:
            count += 1

print(count)