import copy
SIZE = 201

grid = [[0 for j in range(SIZE)] for i in range(SIZE)]
with open('input24.txt') as file:
    prev_move = ""
    for line in file:
        line = line.strip()
        # start in the center
        x,y = 100,100
        # set a direction
        for letter in line:
            if letter == "n":
                y -= 1
            elif letter == "s":
                y += 1
            elif letter == "e":
                if prev_move in "sn" and y % 2 == 0:
                    pass
                else:
                    x += 1
            elif letter == "w":
                if prev_move in "sn" and y % 2 == 1:
                    pass
                else:
                   x -= 1
            prev_move = letter
        
        # flip 
        if grid[y][x] == 0:
            grid[y][x] = 1
        elif grid[y][x] == 1:
            grid[y][x] = 0

ans = 0
for row in grid:
    ans += sum(row)
print("Part 1: ", ans)

# left, right, ul, ur, dl, dr
neighbors_even = [ [0,-1], [0,1], [-1,0], [-1,1], [1,0], [1,1] ]  
neighbors_odd = [ [0,-1], [0,1], [-1,-1], [-1,0], [1,-1], [1,0] ] 
for day in range(100):
    new_grid = copy.deepcopy(grid)
    for y in range(SIZE):
        for x in range(SIZE):
            n_blacks = 0
            
            # choose the direction based on current row
            if y % 2 == 0:
                directions = neighbors_even
            else:
               directions = neighbors_odd

            # check all neighbors    
            for pair in directions:
                dy, dx = pair
                try:
                    if grid[y+dy][x+dx] == 1:
                        n_blacks += 1
                except IndexError:
                    pass
            
            # given in the task
            if grid[y][x] == 0 and n_blacks == 2:
                new_grid[y][x] = 1
            elif grid[y][x] == 1 and n_blacks not in [1,2]:
                new_grid[y][x] = 0
    # if new grid is set up, "flip all at once"
    grid = new_grid

ans = 0
for row in grid:
    ans += sum(row)
print("Part 2: ",ans)