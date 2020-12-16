with open("day12.txt","r") as file:

    f = file.read().splitlines()
    
    pos = [0,0]
    waypoint = [10,1]
    
    d = 1
    for line in f:
        action = line[0]
        units = int(line[1:])
        if action == "R": # change this
            rot = int(units)
            if rot == 90:
                waypoint[0], waypoint[1] = waypoint[1], -waypoint[0]
            if rot == 180:
                waypoint[0], waypoint[1] = -waypoint[0], -waypoint[1]
            if rot == 270:
                waypoint[0], waypoint[1] = -waypoint[1], waypoint[0]
        if action == "L": # and that
            rot = int(units)
            if rot == 270:
                waypoint[0], waypoint[1] = waypoint[1], -waypoint[0]
            if rot == 180:
                waypoint[0], waypoint[1] = -waypoint[0], -waypoint[1]
            if rot == 90:
                waypoint[0], waypoint[1] = -waypoint[1], waypoint[0]
        if action == "F":
            pos[0] += units*waypoint[0]
            pos[1] += units*waypoint[1]
        if action == "N":
            # d = 0
            waypoint[1] += units
        if action == "E":
            # d = 1
            waypoint[0] += units
        if action == "S":
            # d = 2
            waypoint[1] -= units
        if action == "W":
            # d = 3
            waypoint[0] -= units
            
        print("Action: ", action)
        print("Current waypoint:", waypoint)
        print(pos)

ans = abs(pos[0]) + abs(pos[1])
print("Manhattan distance: ", ans)
        