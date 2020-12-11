from time import sleep

with open("day9.txt","r") as file:
    
    f = file.read().splitlines()
    
    full_list = []
    preamble = []
    invalid = 0
    i = 0
    for line in f:
        num = int(line)
        full_list.append(num)
        if i < 25: # normal: 25
            preamble.append(num)
            i += 1
        else:
            found = False
            for x in range(len(preamble)):
                for y in range(x+1,len(preamble)):
                    if num == preamble[x] + preamble[y]:
                        found = True
                        # print(f"{num} is the sum of {preamble[x]} and {preamble[y]}")
            if not found:
                invalid = num
            preamble.append(num)
            preamble.pop(0)
            i += 1
print(invalid)

for i in range(len(full_list)):
    for j in range(i+1,len(full_list)):
        if invalid == sum(full_list[i:j]):
            print(full_list[i:j])
            mini = min(full_list[i:j])
            maxi = max(full_list[i:j])
            print(f"mini: {mini}, maxi: {maxi}, sum: {mini+maxi}")






