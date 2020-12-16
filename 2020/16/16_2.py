import math

with open("day16.txt","r") as file:

    f = file.read()
    # print(f)
    options, my, nearby = f.split("\n\n")

    my = my.split("\n")[1].split(",")
    print(my)
    # print("My: ", len(my))

    valids = []
    acceptable = {}
    options = options.split("\n")
    for o in options:

        name = o.split(": ")[0]
        name_range = []

        o = o.split(": ")[1].split(" or ")
        for _o in o:
            l,h = int(_o.split("-")[0]), int(_o.split("-")[1])
            for v in range(l,h+1):
                name_range.append(v)
                if v not in valids:
                    valids.append(v)
            name_range.sort()
        acceptable[name] = name_range
        # print(acceptable)
    # for a in acceptable.keys():
    #     print(a, acceptable[a])
    
    valid_tickets = []
    nearby = nearby.split(":\n")[1].strip().split("\n")
    collumns = [[] for i in range(len(my))]
    # print(collumns)
    for ticket in nearby:
        # print(ticket) # OK
        valid = True
        to_check = ticket.split(",")
        # print(to_check) # OK
        for t in to_check:
            t = int(t)
            if t not in valids:
                valid = False
        if valid:
            valid_tickets.append(to_check)

    for vt in valid_tickets:
        for i in range(len(vt)):
            collumns[i].append(int(vt[i]))
        # print(vt)
    # print(collumns)
    
    possible_values = {}
    for a in acceptable.keys():
        # print(a, acceptable[a])
        possible_values[a] = []

        current_range = acceptable[a]
        for col in collumns:
            MATCH = True
            # print(col)
            for c in col:
                if c not in current_range:
                    MATCH = False
            if MATCH:
                possible_values[a].append(collumns.index(col))
    # print(possible_values)
    taken = []
    names_collumns = {}
    for i in range(1,len(my)):
        for a in possible_values.keys():
            if len(possible_values[a]) == i:
                for p in possible_values[a]:
                    if p not in taken:
                        taken.append(p)
                        names_collumns[a] = p 
    print(names_collumns)

    my_values = []
    for nc in names_collumns.keys():
        if 'departure' in nc:
            my_values.append(names_collumns[nc])
    print(my_values)

    ans = math.prod([int(my[i]) for i in my_values])
    print(ans)

