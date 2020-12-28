inp = '1321131112'

for _ in range(50):
    out = []
    ran = len(inp)
    i = 0
    while i < ran:
        num = inp[i]
        consec = 1
        while i+1 < ran:
            if inp[i+1] == num:
                consec += 1
                i += 1
            else:
                break
        out.append(str(consec)+num)
        i += 1

    out = ''.join(out)
    inp = out
    if _ == 39:
        print("Part 1: ", len(inp))
    if _ == 49:
        print("Part 2: ", len(inp))


