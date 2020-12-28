import copy

with open('input.txt') as file:
    f = file.read().splitlines()

    vals = {}
    st = 0
    for _ in range(len(f)):
        for line in f:
            l, r = line.split(' -> ')
            if ' ' not in l:
                try:
                    l = int(l)
                except ValueError:
                    pass
            vals[r] = l

vals_part2 = copy.deepcopy(vals)

def circuit(wire):
    

    signal = vals[wire]

    if type(signal) is int:
        return signal


    else:
        if 'AND' in signal:
            x,y = signal.split(' AND ')

            if x == '1':
                vals[wire] = 1 & circuit(y)
                return vals[wire]
            else:
                vals[wire] = circuit(x) & circuit(y)
                return vals[wire]
        
        elif 'OR' in signal:
            x,y = signal.split(' OR ')
            vals[wire] = circuit(x) | circuit(y)
            return vals[wire]

        elif 'LSHIFT' in signal:
            x = signal.split(' LSHIFT ')[0]
            s = int(signal.split(' LSHIFT ')[1])
            vals[wire] = circuit(x) << s
            return vals[wire]

        elif 'RSHIFT' in signal:
            x = signal.split(' RSHIFT ')[0]
            s = int(signal.split(' RSHIFT ')[1])
            vals[wire] = circuit(x) >> s
            return vals[wire]

        elif 'NOT' in signal:
            x = signal.split('NOT ')[1]
            vals[wire] = 65535 - circuit(x)
            return vals[wire]
        
        else:
            vals[wire] = circuit(signal)
            return vals[wire]

result = circuit('a')
print('Part 1: ', result)

vals = vals_part2
vals['b'] = result
result2 = circuit('a')
print('Part 2: ', result2)

