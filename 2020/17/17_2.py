import copy, math

with open("day17.txt") as file:
    
    f = file.read().splitlines()
    
    starting_cube = [row for row in f]
    # print(starting_cube)

    dim_small = len(f)
    mid_small_low = int(math.floor((dim_small-1)/2))
    mid_small_high = int(math.ceil((dim_small-1)/2))
    side_small = int( (dim_small-1)/2 )
    # print(mid_small_low,mid_small_high)

    dim_big = dim_small + 6*2 # 5 cycles increase the size from both sides
    mid_big_low = int(math.floor((dim_big-1)/2))
    mid_big_high = int(math.ceil((dim_big-1)/2))
    side_big = int( (dim_big-1)/2 )

    cube = [ [ [ [ '.' for i in range(dim_big) ] for i in range(dim_big) ] for i in range(dim_big) ] for i in range(dim_big) ]

    for y in range(dim_small):
        for x in range(dim_small):
            cube[6][6][mid_big_low-side_small + y][mid_big_low-side_small + x] = starting_cube[y][x]
    
    # for i in range(13):
    #     print("Slice: ", i)
    #     for j in range(len(cube[i])):
    #         print(cube[i][j])

    directions = [
        [-1,1,-1,-1], [0,1,-1,-1], [1,1,-1,-1],  [-1,0,-1,-1], [0,0,-1,-1], [1,0,-1,-1],  [-1,-1,-1,-1], [0,-1,-1,-1], [1,-1,-1,-1],   # W = -1
        [-1,1,0,-1], [0,1,0,-1], [1,1,0,-1],  [-1,0,0,-1], [0,0,0,-1], [1,0,0,-1],  [-1,-1,0,-1], [0,-1,0,-1], [1,-1,0,-1],   
        [-1,1,1,-1], [0,1,1,-1], [1,1,1,-1],  [-1,0,1,-1], [0,0,1,-1], [1,0,1,-1],  [-1,-1,1,-1], [0,-1,1,-1], [1,-1,1,-1],
        [-1,1,-1,0], [0,1,-1,0], [1,1,-1,0],  [-1,0,-1,0], [0,0,-1,0], [1,0,-1,0],  [-1,-1,-1,0], [0,-1,-1,0], [1,-1,-1,0],   # W = 0
        [-1,1,0,0], [0,1,0,0], [1,1,0,0],  [-1,0,0,0], [0,0,0,0], [1,0,0,0],  [-1,-1,0,0], [0,-1,0,0], [1,-1,0,0],   
        [-1,1,1,0], [0,1,1,0], [1,1,1,0],  [-1,0,1,0], [0,0,1,0], [1,0,1,0],  [-1,-1,1,0], [0,-1,1,0], [1,-1,1,0],
        [-1,1,-1,1], [0,1,-1,1], [1,1,-1,1],  [-1,0,-1,1], [0,0,-1,1], [1,0,-1,1],  [-1,-1,-1,1], [0,-1,-1,1], [1,-1,-1,1],   # W = 1
        [-1,1,0,1], [0,1,0,1], [1,1,0,1],  [-1,0,0,1], [0,0,0,1], [1,0,0,1],  [-1,-1,0,1], [0,-1,0,1], [1,-1,0,1],   
        [-1,1,1,1], [0,1,1,1], [1,1,1,1],  [-1,0,1,1], [0,0,1,1], [1,0,1,1],  [-1,-1,1,1], [0,-1,1,1], [1,-1,1,1],
    ]

    #########################

    # print("Turn: 0")
    # for i in range(5,8):
    #     print("Slice: ", i)
    #     for row in cube[i]:
    #         print(row)

    ############################

    for c in range(2,8): # c in (1,6), but we consider one more
        
        # neighbors = [ [ [ 0 for i in range(dim_big) ] for i in range(dim_big) ] for i in range(dim_big) ]
        cube_next = copy.deepcopy(cube)

        lower = mid_big_low - side_small - c
        higher = mid_big_high + side_small + c + 1

        for w in range(6-c,6+c+1):
            for z in range(lower, higher):
                for y in range(lower, higher):
                    for x in range(lower, higher):
                        
                        neighbors = 0
                        for d in directions:
                            dx,dy,dz,dw = d
                            try:
                                if dx == 0 and dy == 0 and dz == 0 and dw == 0:
                                    pass
                                elif cube[w+dw][z+dz][y+dy][x+dx] == '#' :
                                    neighbors += 1
                            except IndexError:
                                pass

                        try:
                            if cube[w][z][y][x] == '#' and neighbors not in range(2,4):
                                cube_next[w][z][y][x] = '.'
                            if cube[w][z][y][x] == '.' and neighbors == 3:
                                cube_next[w][z][y][x] = '#'
                        except IndexError:
                            pass

                        
        # print("Slice: 6")
        # for j in range(len(cube[6][6])):
        #     print(cube[6][6][j])

        # # worked
        active = 0
        for w in range(6-c-1, 6+c):
            for z in range(6-c, 6+c+1):
                for y in range(lower, higher):
                    for x in range(lower, higher):
                        # print(f"x: {x} y: {y} z: {z}")
                        try:
                            if cube_next[w][z][y][x] == '#':
                                active += 1
                        except IndexError:
                            pass

        print("Turn: ", c-1, "active: ", active)

        # PRINTOUT
        # for w in range(6-c+1, 6+c):
        #     for z in range(6-c+1, 6+c):
        #         print(f"z = {z-6}, w = {w-6}")
        #         try:
        #             for y in range(mid_big_low-c, mid_big_high+c+1):
        #                 print(cube_next[w][z][y][mid_big_low-c : mid_big_high+c+1])
        #         except IndexError:
        #             for y in range(mid_big_low-c+1, mid_big_high+c):
        #                 print(cube_next[w][z][y][mid_big_low-c+1 : mid_big_high+c])

        cube = cube_next





    