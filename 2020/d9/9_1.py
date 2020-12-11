from time import sleep

with open("day9.txt","r") as file:
    
    f = file.read().splitlines()
    
    preamble = []
    invalid = []
    i = 0
    for line in f:
        num = int(line)
        
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
                invalid.append(num)
            preamble.append(num)
            preamble.pop(0)
            i += 1
    # print(preamble)
    print(invalid)




