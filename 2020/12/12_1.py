with open("day12.txt","r") as file:

    f = file.read().splitlines()
    
    pos = [0,0]
    directions = [
        [0,1],[1,0],[0,-1],[-1,0] # N E S W
    ] 
    d = 1
    for line in f:
        action = line[0]
        units = int(line[1:])
        if action == "R":
            rot = int(units/90)
            d = d + rot
            d = d % 4
        if action == "L":
            rot = int((360-units)/90)
            d = d + rot
            d = d % 4
        if action == "F":
            pos[0] += units*directions[d][0]
            pos[1] += units*directions[d][1]
        if action == "N":
            # d = 0
            pos[0] += units*directions[0][0]
            pos[1] += units*directions[0][1]
        if action == "E":
            # d = 1
            pos[0] += units*directions[1][0]
            pos[1] += units*directions[1][1]
        if action == "S":
            # d = 2
            pos[0] += units*directions[2][0]
            pos[1] += units*directions[2][1]
        if action == "W":
            # d = 3
            pos[0] += units*directions[3][0]
            pos[1] += units*directions[3][1]
            
        print("Action: ", action)
        print("Current direction:", directions[d])
        print(pos)

ans = abs(pos[0]) + abs(pos[1])
print("Manhattan distance: ", ans)
        