from collections import Counter,defaultdict

patterns = {}
with open('input.txt') as f:
    polymer = f.readline().strip()
    f.readline()
    for line in f.readlines():
        double,single = line.strip().split(' -> ')
        patterns[double] = single

# initialize the first polymer
counts = defaultdict(int)
for i in range(len(polymer)-1):
    double = polymer[i]+polymer[i+1]
    counts[double] += 1


ROUNDS = 40

# add new substance exponentially
for _ in range(ROUNDS):
    new_counts = defaultdict(int)
    for key,value in counts.items():
        ins = patterns[key]
        new_counts[key[0]+ins] += value
        new_counts[ins+key[1]] += value
    counts = new_counts

# count individual substances from pairs
statistics = defaultdict(int)
for k in list(counts.keys()):
    statistics[k[0]] += counts[k]
    statistics[k[1]] += counts[k]

most_common = max(statistics.values())
least_common = min(statistics.values())
# answer may vary by -1 or +1
# this is due pairs not overlapping
print(int((most_common-least_common)/2-1))
