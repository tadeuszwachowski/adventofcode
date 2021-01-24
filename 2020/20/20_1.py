import numpy as np
import math

S = 10 # TILE SIZE

class Tile:
    def __init__(self,nr,layout):
        self.nr = nr
        self.layout = layout

        self.top = ''.join(layout[0])
        self.bot = ''.join(layout[-1])
        self.left = ''.join([row[0] for row in layout])
        self.right = ''.join([row[-1] for row in layout])


SIZE = -1
tiles = []
grid = np.zeros((20,20), dtype=Tile)

def solve(row,col,visited):

    if row == SIZE: # if all is solved
        ans = grid[0][0].nr * grid[0][SIZE-1].nr * grid[SIZE-1][0].nr * grid[SIZE-1][SIZE-1].nr 
        print(f"PRODUCT = {ans}")
        exit(0)
        return True

    for tile in tiles:
        
        if visited.count(tile.nr) == 0:
            
            if row > 0 and tile.top != grid[row-1][col].bot:  
                continue
            elif col > 0 and tile.left != grid[row][col-1].right:
                continue
            else:
                grid[row][col] = tile
                
                visited.append(tile.nr)
                if col == (SIZE - 1): # last column
                    solve(row+1, 0, visited)
                else:
                    solve(row, col+1, visited)  
                # if not solved
                visited.remove(tile.nr)

# MAIN

with open("input.txt") as file:

    f = file.read().split("\n\n")

    for t in f:
        info, image = t.split(":\n")
        nr = int(info.split('Tile ')[1])
        layout = np.array([list(row) for row in image.split("\n")])
        for f in range(2):
            for r in range(4):
                tiles.append(Tile(nr,layout))
                layout = np.rot90(layout)
            layout = np.fliplr(layout)


SIZE = int(math.sqrt(len(tiles)/8))
# print(SIZE)

visited = []
solve(0, 0, visited)
