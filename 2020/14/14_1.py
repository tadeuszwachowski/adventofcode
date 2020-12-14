with open("day14.txt","r") as file:

    f = file.read().splitlines()
    
    mem = {}
    mask = []
    for line in f:
        # print(line[:4])
        if line[:4] == 'mask':
            mask = list(line.split(" = ")[1]) 

        if line[:3] == 'mem':
            address = int(line.split("[")[1].split("]")[0])
            value_bin = list(bin(int(line.split(" = ")[1]))[2:].zfill(36))

            for i in range(36):
                if mask[-i] != 'X':
                    value_bin[-i] = mask[-i]
            print(value_bin)
            
            value_bin = ''.join(value_bin)

            value_dec = int(value_bin,2)
            mem[address] = value_dec

    # print(mem)
    ans = 0 # 397
    print(mem.values())
    for v in mem.values():
        ans += v
    print("Answer: ", ans)