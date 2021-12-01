#ans = 1797
with open('input.txt') as f:
    depths = list(map(int,f.readlines()))

increases = 0
# calculate first sum
prev_sum = sum(depths[:3])

for i in range(1,len(depths)-2):
    new_sum = sum(depths[i:i+3])
    if new_sum > prev_sum:
        increases += 1
    prev_sum = new_sum

print(increases)