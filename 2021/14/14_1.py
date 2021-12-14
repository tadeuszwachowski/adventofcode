from collections import Counter

patterns = {}
with open('input.txt') as f:
    polymer = f.readline().strip()
    _ = f.readline()
    for line in f.readlines():
        double,single = line.strip().split(' -> ')
        patterns[double] = single

for r in range(1,11):
    inserts = []
    for i in range(len(polymer)-1):
        double = polymer[i]+polymer[i+1]
        if double in patterns.keys():
            inserts.append( (i+len(inserts)+1, patterns[double]) )
    for ind,value in inserts:
        polymer = polymer[:ind] + value + polymer[ind:]

statistics = Counter(polymer)
most_common = max(statistics.values())
least_common = min(statistics.values())
print(most_common-least_common)

