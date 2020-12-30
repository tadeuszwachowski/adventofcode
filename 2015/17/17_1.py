import itertools
with open('input.txt') as file:
    f = file.read().splitlines()
    containers = list(map(int,f))

    n = 0
    for i in range(1,len(containers)):
        for comb in itertools.combinations(containers,i):
            if sum(comb) == 150:
                n += 1

print('Possible combinations: ', n)