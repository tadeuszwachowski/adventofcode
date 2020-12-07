with open("day3.txt","r") as file:
    n_trees = 0
    x = 3
    next(file) # next line
    for row in file:
        row = row.strip("\n")
        print(row)
        if row[x] == "#":
            n_trees += 1
        x += 3
        x %= len(row)
    print(n_trees)  