with open("day10.txt","r") as file:

    f = file.read().splitlines()

    adapters = []
    for line in f:
        v = int(line)
        adapters.append(v)
    adapters.sort()
    print(adapters)
    
    max_v = adapters[-1] + 3
    adapters.append(max_v)
    print(max_v)
    out = 0
    diff_1 = 0
    diff_3 = 0
    while out != max_v:
        try:
            next_3 = [out+1,out+2,out+3]
            min_common = min(set(next_3) & set(adapters))
            # print(common, min_common, out)
            # print("o:", out, "min:", min_common, diff_1, diff_3)
            if min_common - out == 1:
                diff_1 += 1
            if min_common - out == 3:
                diff_3 += 1
            out = min_common
        except ValueError:
            print("o:", out, "min:", min_common, diff_1, diff_3)
            break
print(diff_1, diff_3, diff_1*diff_3)
# print(min_common)