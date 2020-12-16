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
                y3 = [y-1,y,y+1]
                x3 = [x-1,x,x+1]
                for _y in y3:
                    for _x in x3:
                        if _y in range(len(layout)) and _x in range(len(layout[0])):
                            if (_x == x) and (_y == y):
                                continue
                            else:
                                if layout[_y][_x] == "#":
                                    adjacent[y][x] += 1

    for y in range(len(new_layout)):
        for x in range(len(new_layout[y])):
            if layout[y][x] == "L" and adjacent[y][x] == 0:
                new_layout[y][x] = "#"
            elif layout[y][x] == "#" and adjacent[y][x] >= 4:
                new_layout[y][x] = "L"

    # print("Przebieg: ", i)
    # print("##########################")
    # for a in adjacent:
    #     print(a)
    # print("##########################")
    # for l in layout:
    #     print(l)
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



