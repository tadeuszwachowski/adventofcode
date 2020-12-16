with open("day16.txt","r") as file:

    f = file.read()
    # print(f)
    options, my, nearby = f.split("\n\n")

    my = my.split("\n")[1]

    valids = []
    options = options.split("\n")
    for o in options:
        o = o.split(": ")[1].split(" or ")
        for _o in o:
            l,h = int(_o.split("-")[0]), int(_o.split("-")[1])
            for v in range(l,h+1):
                if v not in valids:
                    valids.append(v)
    valids.sort()
    
    invalids = []
    nearby = nearby.split(":\n")[1].strip().split("\n")
    for n in nearby:
        to_check = n.split(",")
        for t in to_check:
            t = int(t)
            if t not in valids:
                invalids.append(t)

    print(sum(invalids))