with open('input.txt') as file:
    f = ''.join(file.read().splitlines())
    print(f)

    dirs = [
        [0,1], [1,0], [0,-1], [-1,0] 
    ]

    pos = [0,0]
    visited = [pos]


    for d in f:
        if d == '^':
            x,y = dirs[0]
        if d == '>':
            x,y = dirs[1]
        if d == 'v':
            x,y = dirs[2]
        if d == '<':
            x,y = dirs[3]
        
        cx,cy = pos
        pos = [cx+x, cy+y]
        if pos not in visited:
            visited.append(pos)

print("Part 1: ", len(visited))