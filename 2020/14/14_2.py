with open("day14.txt","r") as file:

    f = file.read().splitlines()
    
    mem = {}
    mask = []
    for line in f:
        # print(line[:4])
        if line[:4] == 'mask':
            mask = list(line.split(" = ")[1]) 

        if line[:3] == 'mem':
            address = list(bin(int(line.split("[")[1].split("]")[0]))[2:].zfill(36))
            value = int(line.split(" = ")[1])

            for i in range(36):
                if mask[-i] != '0':
                    address[-i] = mask[-i]
            # print(address)
            
            adresses = []
            adresses_dec = []

            n_x = address.count('X')

            # print(n_x)
            floaties = []
            for i in range(2**n_x):
                bin_i = list(bin(i)[2:].zfill(n_x))
                floaties.append(bin_i)
            for fl in floaties:
                address_copy = address.copy()
                j = 0
                for bit in range(36):
                    if address_copy[-bit] == 'X':
                        address_copy[-bit] = fl[-j]
                        j += 1
                adresses.append(address_copy)
                adresses_dec.append(int(''.join(address_copy),2))

            for a in adresses_dec:
                mem[a] = value
                

    # print(mem)
    ans = 0 # 397
    # print(mem.values())
    for v in mem.values():
        ans += v
    print("Answer: ", ans)