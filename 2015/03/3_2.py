with open('input.txt') as file:
    f = ''.join(file.read().splitlines())
    print(f)

    dirs = [
        [0,1], [1,0], [0,-1], [-1,0] 
    ]

    pos = [0,0]
    robo_pos = [0,0]
    visited = [pos]


    for i in range(len(f)):
        if f[i] == '^':
            x,y = dirs[0]
        if f[i] == '>':
            x,y = dirs[1]
        if f[i] == 'v':
            x,y = dirs[2]
        if f[i] == '<':
            x,y = dirs[3]
        
        if i%2 == 0:
            cx,cy = pos
            pos = [cx+x, cy+y]
            if pos not in visited:
                visited.append(pos)
        else:
            rx,ry = robo_pos
            robo_pos = [rx+x, ry+y]
            if robo_pos not in visited:
                visited.append(robo_pos)

print("Part 2: ", len(visited))