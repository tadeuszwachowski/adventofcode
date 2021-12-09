# parse the file
grid = [[int(x) for x in list(line.strip())] for line in open('input.txt').readlines()]

directions = [
    (-1,0), (0,1), (0,-1), (1,0),
]

low_points = []

for y in range(len(grid)):
    for x in range(len(grid[0])):
        point = grid[y][x]
        is_lowest = True
        for dir in directions:
            dy, dx = dir
            if y+dy in range(len(grid)) and x+dx in range(len(grid[0])):
                adjacent = grid[y+dy][x+dx]
                if adjacent <= point:
                    is_lowest = False
                    break

        if is_lowest:
            # add with risk level=1
            low_points.append(point+1)

print(sum(low_points))





