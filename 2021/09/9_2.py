# used to optimise searching visited points
def point_hash(point):
    return point[0] + point[1]*100

# parse the file
grid = [[int(x) for x in list(line.strip())] for line in open('input.txt').readlines()]

directions = [
    (-1,0), (0,1), (0,-1), (1,0),
]

# get locations of all the lowest points
low_points_locations = []

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
            low_points_locations.append([y,x])

basins = []

for start_point in low_points_locations:
    visited = []
    to_visit = [start_point]

    # dont stop until there are no more points to go
    while len(to_visit) > 0:
        current_point = to_visit.pop(0)
        y,x = current_point
        current_point_value = grid[y][x]

        # check all the adjacent positions
        for dir in directions:
            dy, dx = dir
            if y+dy in range(len(grid)) and x+dx in range(len(grid[0])):
                adjacent = grid[y+dy][x+dx]
                if adjacent < 9 and adjacent >= current_point_value:
                    adjacent_cords = [y+dy,x+dx]

                    # if we found a NEW point to explore
                    if point_hash(adjacent_cords) not in visited:
                        to_visit.append(adjacent_cords)
        
        # mark as visited
        if point_hash(current_point) not in visited:
            visited.append(point_hash(current_point))

    basins.append(len(visited))

a,b,c = sorted(basins)[-3:]
print(a*b*c)
    




