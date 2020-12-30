import itertools
with open('input.txt') as file:
    f = file.read().splitlines()
    containers = list(map(int,f))

    m = float("inf")
    for i in range(1,len(containers)):
        for comb in itertools.combinations(containers,i):
            if sum(comb) == 150 and i < m:
                m = i

    n = 0
    for comb in itertools.combinations(containers,m):
        if sum(comb) == 150:
            n += 1

print('Possible combinations: ', n)