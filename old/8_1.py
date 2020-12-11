with open("day8.txt","r") as file:
    
    f = file.read().splitlines()

    instructions = {}
    i = 0
    for line in f:
        instr, val = line.split()
        if "-" in val:
            val = -int(val[1:])
        else:
            val = int(val[1:])
        # print(instr,val)
        instructions[i] = [instr, val]
        i += 1

    # print(instructions)
    visited_ind = []
    accu = 0
    index = 0
    while True:
        if index not in visited_ind:
            instr,val = instructions[index]
            visited_ind.append(index)
            if instr == 'nop':
                index += 1
            if instr == 'acc':
                accu += val
                index += 1
            if instr == 'jmp':
                index += val
        else:
            break
    print("Visited: ", len(visited_ind))
    print("Accu:", accu)

    # print(f)