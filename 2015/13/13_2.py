import itertools

with open('input.txt') as file:
    f = file.read().splitlines()

relations = {}
guests = []

for line in f:
    name = line.split(' ')[0]
    neighbor = line.split(' ')[10][:-1]
    
    if line.split(' ')[2] == 'gain':
        happiness = int(line.split(' ')[3])
    elif line.split(' ')[2] == 'lose':
        happiness = -int(line.split(' ')[3])

    if name not in guests:
        guests.append(name)

    if name not in relations.keys():
        relations[name] = {neighbor: happiness}
    else:
        relations[name][neighbor] = happiness


# adding 'me'
for name in relations.keys():
    relations[name]['me'] = 0

relations['me'] = {}
for name in guests:
    relations['me'][name] = 0

guests.append('me')



layouts = itertools.permutations(guests,len(guests))

best_table = ()
max_happiness = 0
for table in layouts:
    happiness = 0
    for i in range(len(table)):
        if i == 0:
            n1, n2 = i+1, len(table)-1
        elif i == len(table)-1:
            n1, n2 = i-1, 0
        else:
            
            n1, n2 = i-1, i+1
        value1 = relations[table[i]][table[n1]]
        value2 = relations[table[i]][table[n2]]
        happiness += value1+value2

    if happiness > max_happiness:
        max_happiness = happiness
        best_table = table

print(best_table, max_happiness)