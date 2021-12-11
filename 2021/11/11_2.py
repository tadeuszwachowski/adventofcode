def hash(y,x):
    return y + x*200

directions = {
    (-1,-1), (-1,0), (-1,1),
    (0,-1), (0,1),
    (1,-1), (1,0), (1,1),
}

with open('input.txt') as f:
    grid = [[int(x) for x in list(line.strip())] for line in f.readlines()]

# calculate the number of octopuses
size = len(grid)*len(grid[0])

r = 1
# cont = True
while True:
    flashes = 0
    # add +1 energy to every octopus
    queue = []
    visited = []
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            grid[y][x] += 1
            if grid[y][x] > 9:
                queue.append((y,x))
                visited.append(hash(y,x))

    # check on all the octopus that are 9 or higher nenrgy
    while len(queue) > 0:
        y,x = queue.pop(0)
        for dy,dx in directions:
            if y+dy in range(0,len(grid)) and x+dx in range(0,len(grid[y+dy])):
                if hash(y+dy,x+dx) not in visited:
                    grid[y+dy][x+dx] += 1
                    if grid[y+dy][x+dx] > 9:
                        queue.append((y+dy,x+dx))
                        visited.append(hash(y+dy,x+dx))
        # if flashed, set energy to 0 and note that it flashed
        visited.append(hash(y,x))
        grid[y][x] = 0
        flashes += 1

    # if synchronised
    if flashes == size:
        print(r)
        break
    r += 1
