with open('input.txt') as file:
    replacements, med = file.read().split('\n\n')
    replacements = replacements.split('\n')

#print(replacements)
#print(medicine)
mutations = []

for r in replacements:
    before, after = r.split(' => ')
    
    i = 0
    for _ in range(med.count(before)):
        new_med = med[:i] + med[i:].replace(before,after,1)
        # print(new_med, i)
        i = i + med[i:].find(before)+1
        # if new_med not in distinct:
        mutations.append(new_med)

print('Part 1: ', len(set(mutations)))