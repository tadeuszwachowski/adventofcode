with open('input.txt') as file:
    f = file.read().splitlines()

    count = 0
    for s in f:
        
        vow, double = False, False
        excl4 = True

        if len( [_ for _ in s if _ in 'aeiou'] ) >= 3:
            vow = True

        for i,j in zip(s,s[1:]):
            if i==j:        
                double = True

        for e in ['ab', 'cd', 'pq', 'xy']:
            if e in s:
                excl4 = False


        if vow and double and excl4:
            count += 1

print('Part 1: ', count)