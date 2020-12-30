actual = {'children': 3, 'cats': 7, 'samoyeds': 2, 
'pomeranians': 3, 'akitas': 0, 'vizslas': 0, 
'goldfish': 5, 'trees': 3, 'cars': 2, 'perfumes': 1}

with open('input.txt') as file:
    f = file.read().splitlines()

all_sues = {}

max_valid = 0
best_sue = 0
for line in f:
    valid = len(actual)
    sue_nr = int(line.split()[1][:-1])
    all_facts = ' '.join(line.split()[2:])
    facts = all_facts.split(', ')
    
    for inf in facts:
        name = inf.split(': ')[0]
        value = int(inf.split(': ')[1])
        
        if name == 'cats' or name == 'trees':
            if actual[name] >= value:
                valid -= 1
        elif name == 'pomeranians' or name == 'goldfish':
            if actual[name] <= value:
                valid -= 1
        elif actual[name] != value:
            valid -= 1
    
    if valid > max_valid:
        max_valid = valid
        best_sue = sue_nr

print("Our Sue is nr", best_sue)