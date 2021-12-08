sum_of_numbers = 0
with open('input.txt') as f:
    for line in f:
        wires, output = line.strip().split(' | ')
        wires = wires.split()
        output = output.split()
        # print(wires)
        displays = {0: '', 1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: ''}
        # if len == 5 append to left triple, if len == 6 append to right triple
        left_triple = []
        right_triple = []
        # first find the known valuesby len: 
        # 1, 4, 7, 8 
        # group [2,3,5] (len5), [0,6,9] (len6)
        for w in wires:
            l = len(w)
            if l == 2: displays[1] = set(w)
            if l == 3: displays[7] = set(w)
            if l == 4: displays[4] = set(w)
            if l == 5: left_triple.append(set(w))
            if l == 6: right_triple.append(set(w))
            if l == 7: displays[8] = set(w)
        # first we sort the [0,6,9] group
        for w in right_triple:
            if displays[4].issubset(set(w)): 
                displays[9] = set(w)
            else:
                if displays[7].issubset(set(w)):
                    displays[0] = set(w)
                else:
                    displays[6] = set(w)
        # then we sort the [2,3,5] group
        for w in left_triple:
            if displays[7].issubset(set(w)): 
                displays[3] = set(w)
            else:
                if len(set(w).intersection(displays[4])) == 3:
                    displays[5] = set(w)
                else:
                    displays[2] = set(w)
        # print(displays)

        digits = ''
        for n in output:
            s = set(n)
            for i, key in enumerate(displays.values()):
                if s == key:
                    digits = digits + str(i)
        # print(digits)
        sum_of_numbers += int(digits)
print(sum_of_numbers)
        

# print(count)