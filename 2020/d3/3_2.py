n1,n2,n3,n4,n5 = 0,0,0,0,0

with open("day3.txt","r") as file:
    n_trees = 0
    x = 1
    next(file) # next line
    for row in file:
        row = row.strip("\n")
        # print(row)
        if row[x] == "#":
            n_trees += 1
        x += 1
        x %= len(row)
    print(n_trees)
    n1 = n_trees 


with open("data.txt","r") as file:
    n_trees = 0
    x = 3
    next(file) # next line
    for row in file:
        row = row.strip("\n")
        # print(row)
        if row[x] == "#":
            n_trees += 1
        x += 3
        x %= len(row)
    print(n_trees)
    n2 = n_trees 


with open("data.txt","r") as file:
    n_trees = 0
    x = 5
    next(file) # next line
    for row in file:
        row = row.strip("\n")
        # print(row)
        if row[x] == "#":
            n_trees += 1
        x += 5
        x %= len(row)
    print(n_trees)
    n3 = n_trees


with open("data.txt","r") as file:
    n_trees = 0
    x = 7
    next(file) # next line
    for row in file:
        row = row.strip("\n")
        # print(row)
        if row[x] == "#":
            n_trees += 1
        x += 7
        x %= len(row)
    print(n_trees)
    n4 = n_trees


with open("data.txt","r") as file:
    n_trees = 0
    x = 1
    y = 2
    for row in file:
        if y % 2 == 0:
            row = row.strip("\n")
            # print(row)
            if row[x] == "#":
                n_trees += 1
            x += 1
            x %= len(row)
        y += 1
    print(n_trees)
    n5 = n_trees

print("ALL: ",n1*n2*n3*n4*n5)              