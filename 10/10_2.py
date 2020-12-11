from itertools import combinations

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n*factorial(n-1)

with open("day10.txt","r") as file:

    f = file.read().splitlines()

    adapters = []
    for line in f:
        v = int(line)
        adapters.append(v)
    adapters.sort()
    # print(adapters)
    # print(len(adapters))
    
    max_v = adapters[-1] + 3
    # adapters.append(max_v)
    # print(max_v)

    adapters_diffs = []
    for i in range(1,len(adapters)):
        # print(i, i-1)
        diff = adapters[i] - adapters[i-1]
        adapters_diffs.append(diff)

    adapters_min = []

    out = 0
    while out != max_v:
        try:
            next_3 = [out+1,out+2,out+3]
            max_common = max(set(next_3) & set(adapters))
            # print(common, min_common, out)
            # print("o:", out, "min:", min_common, diff_1, diff_3)
            adapters_min.append(max_common)
            out = max_common
        except ValueError:
            # print("o:", out, "min:", min_common, diff_1, diff_3)
            break

      
    # print(adapters_min)
    redundants = list(set(adapters)-set(adapters_min))
    redundants.sort()

    print(adapters)
    print(adapters_min)
    print(len(adapters_min))  
    print(redundants)

    # print(redundants)
    # print(len(redundants))
    no_combs = 1
    n = len(redundants)
    for k in range(1,n+1):
        # print(f"{n} nad {k}: {n}! / {k}! * {n-k}! ")
        no_combs += int( factorial(n) / (factorial(k)*factorial(n-k)) )
    print("Kombinacje = ", no_combs)

    # permutations = [adapters_min]

    # for r in redundants:
    #     permutations_copy = permutations[:]
    #     # print(permutations_copy)
    #     # permutations_copy.append(r)
    #     for pc in permutations_copy:
    #         pc.append(r)
    #         # print(pc)
    #         pc.sort()
    #         # print(new_perm)
    #         permutations.append(pc)
    # # print(permutations)
    # # print(len(permutations))
    

# for p in permutations:
#     print(p)