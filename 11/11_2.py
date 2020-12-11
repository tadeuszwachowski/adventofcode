print("Counting...")
layout = []
with open("day11.txt","r") as file:
    
    f = file.read().splitlines()
    for line in f:
        layout.append(list(line))

adjacent = [[0 for y in range(len(layout))] for x in range(len(layout[0]))]

new_layout = []
for y in range(len(layout)):
    new_layout.append([])
    for x in range(len(layout[y])):
        new_layout[y].append(layout[y][x])

i = 0
repeat = True
while repeat:
    i += 1
    for y in range(len(new_layout)):
        for x in range(len(new_layout[y])):
            place = layout[y][x]
            if place != ".": # check adjacents
                
                directions = [ # [x,y]
                    [-1,-1], [0,-1], [1,-1],
                    [-1,0], [0,0], [1,0],
                    [-1,1], [0,1], [1,1] 
                ]

                for d in directions:
                    _x, _y = d
                    Stop = False
                    if (_x == 0) and (_y == 0):
                        continue
                    else:
                        while not Stop:
                            new_x = x + _x
                            new_y = y + _y

                            if new_y not in range(len(layout)) or new_x not in range(len(layout[0])):
                                Stop = True
                            elif layout[new_y][new_x] == "L":
                                Stop = True
                            elif layout[new_y][new_x] == "#":
                                adjacent[y][x] += 1
                                Stop = True
                            else:
                                _x += d[0]
                                _y += d[1]         

    for y in range(len(new_layout)):
        for x in range(len(new_layout[y])):

            if layout[y][x] == "L" and adjacent[y][x] == 0:
                new_layout[y][x] = "#"
            elif layout[y][x] == "#" and adjacent[y][x] >= 5:
                new_layout[y][x] = "L"

    # # Do wypisywania layoutów
    # print("Przebieg: ", i)
    # print("##########################")
    # for a in adjacent:
    #     print(a)
    # print("##########################")
    # for l in layout:
    #     print("".join(l))
    # print("##########################")
    # for n in new_layout:
    #     print(n)
    
    if new_layout == layout:
        
        repeat = False

        layout = []
        for y in range(len(new_layout)):
            layout.append([])
            for x in range(len(new_layout[y])):
                layout[y].append(new_layout[y][x])
    else:

        layout = []
        for y in range(len(new_layout)):
            layout.append([])
            for x in range(len(new_layout[y])):
                layout[y].append(new_layout[y][x])

    adjacent = [[0 for y in range(len(layout))] for x in range(len(layout[0]))]

occupied = 0
for row in layout:
    for seat in row:
        if seat == "#":
            occupied += 1
print(occupied)


