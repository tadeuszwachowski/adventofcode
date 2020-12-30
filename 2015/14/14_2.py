with open('input.txt') as file:
    f = file.read().splitlines()

max_dist = 0
best_reindeer  = ''
names = []
attribs = {}
for line in f:
    
    name = line.split()[0]
    names.append(name)
    v = int(line.split()[3])
    t = int(line.split()[6])
    rest = int(line.split()[13])
    attribs[name] = [t,v,rest]
    
dist = 0
total_time = 2503 # input

ranking = {}
for n in names:
    ranking[n] = 0
positions = {}
for n in names:
    positions[n] = 0


for sec in range(1,total_time+1):
    for n in names:
        if sec % (attribs[n][0]+attribs[n][2]) in range(1,attribs[n][0]+1):
            positions[n] += attribs[n][1]

    max_dict = max(positions.items(), key=lambda x: x[1])
    listOfKeys = list()
    for key, value in positions.items():
        if value == max_dict[1]:
            listOfKeys.append(key)

    for k in listOfKeys:
        ranking[k] += 1

print(ranking) 
print(max(ranking, key=ranking.get), ranking[max(ranking, key=ranking.get)])
