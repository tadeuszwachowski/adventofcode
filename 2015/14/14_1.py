with open('input.txt') as file:
    f = file.read().splitlines()

max_dist = 0
best_reindeer  = ''
for line in f:
    
    name = line.split()[0]
    v = int(line.split()[3])
    t = int(line.split()[6])
    rest = int(line.split()[13])
    
    dist = 0
    total_time = 2503 # input
    
    full_cycles = total_time // (t+rest)
    dist += full_cycles*v*t
    remaining_time = total_time % (t+rest)
    
    if remaining_time < t:
        dist += remaining_time*v
    else:
        dist += t*v

    if dist > max_dist:
        max_dist = dist
        best_reindeer = name

print(best_reindeer,max_dist)