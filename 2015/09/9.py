from itertools import permutations

costs = {}
locs = []
with open('input.txt') as file:
    
    f = file.read().splitlines()

    for line in f:
        cities = line.split(' = ')[0].split(' to ')
        for c in cities:
            if c not in locs:
                locs.append(c)

        value = int(line.split(' = ')[1])    
        cities.sort()
        costs[' '.join(cities)] = value

ll = len(locs)
routes = permutations(locs,ll)

min_dist = float("inf")
max_dist = 0
for r in routes:
    d = 0
    for i in range(ll-1):
        jump = [ r[i], r[i+1] ]
        jump.sort()
        d += costs[' '.join(jump)]
    if d < min_dist:
        min_dist = d
    if d > max_dist:
        max_dist = d

print('Part 1:', min_dist)
print('Part 1:', max_dist)