import numpy as np

def fold_horizontal(array,fold):
    '''split by making horizontal line'''
    chunksize = [fold,fold+1]
    top,_,bottom = np.array_split(array,chunksize,axis=0)
    folded = np.bitwise_or(top,np.flipud(bottom))
    return folded

def fold_vertical(array,fold):
    '''split by making vertical line'''
    chunksize = [fold,fold+1]
    left,_,right = np.array_split(array,chunksize,axis=1)
    folded = np.bitwise_or(left,np.fliplr(right))
    return folded

# set initial size to 1500x1500
grid =[[0 for _ in range(1500)] for _ in range(1500)]
height = 0
width = 0
with open('input.txt') as f:
    for line in f.readlines():
        # parse the points and check needed height and width
        if ',' in line:
            x,y = [int(x) for x in line.split(',')]
            grid[y][x] = 1
            if x > width:
                width = x+2
            if y > height:
                height = y+1
        else:
            if line == '\n':
                # cut down the excess parts
                grid = grid[:height]
                for i in range(len(grid)):
                    grid[i] = grid[i][:width]
                # convert to numpy array
                grid = np.array(grid)
            if 'fold' in line:
                # fold the paper and count the points
                expr = line.split()[-1]
                axis, symmetry = expr.split('=')[0],int(expr.split('=')[1])
                if axis == 'x':
                    grid = fold_vertical(grid,symmetry)
                if axis == 'y':
                    grid = fold_horizontal(grid,symmetry)
                print("Fold #1: ",np.sum(grid))
                break
               
    