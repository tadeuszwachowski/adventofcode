with open('input.txt') as f:
    depths = list(map(int,f.readlines()))

increases = 0
prev_depth = depths[0]
for i in range(1,len(depths)):
    new_depth = depths[i]
    if new_depth > prev_depth:
        increases += 1
    prev_depth = new_depth
print(increases)