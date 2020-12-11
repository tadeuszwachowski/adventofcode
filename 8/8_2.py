with open("day8.txt","r") as file:
    
    f = file.read().splitlines()

    instructions = {}
    suspicious_ind = []
    i = 0
    for line in f:
        instr, val = line.split()
        if "-" in val:
            val = -int(val[1:])
        else:
            val = int(val[1:])
        # print(instr,val)
        instructions[i] = [instr, val]
        if instr == 'jmp' or instr == 'nop':
            suspicious_ind.append(i)
        i += 1

    for si in suspicious_ind:
        visited_ind = []
        accu = 0
        index = 0
        while True:
            if index not in visited_ind:
                instr,val = instructions[index]
                visited_ind.append(index)
                
                if index == si:
                    if instr == 'nop':
                        instr = 'jmp'
                    if instr == 'jmp':
                        instr = 'nop'

                if instr == 'nop':
                    index += 1
                if instr == 'acc':
                    accu += val
                    index += 1
                if instr == 'jmp':
                    index += val

                if index == (len(instructions) - 1):
                    print(f"FOUND THE BUG!! CURRENT VALUE OF AKKU: {accu}")
                    break
            else:
                break

    # print(f)