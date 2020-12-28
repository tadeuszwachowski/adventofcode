inp = list(map(int, '364289715'))
n = len(inp)

di = 0
move = 1 #
for _ in range(100):
    
    # print(f'-- move {move} --')
    # print('cups: ', end=' ')

    cup = inp[di]
    p1, p2, p3 = (di+1)%n, (di+2)%n, (di+3)%n
    picked_up = [ inp[p1], inp[p2], inp[p3] ]

    # for c in inp:
    #     if c != cup: 
    #         print(c, end=' ') 
    #     else: 
    #         print(f'({c})', end=' ')
    # print('\npick up: ', picked_up)

    next_chosen = inp[ (di+4)%n ]

    for pu in picked_up:
        inp.remove(pu)

    next_cup = cup-1 if cup-1 != 0 else n
    while next_cup in picked_up:
        next_cup = next_cup-1 if next_cup-1 != 0 else n

    nc_index = inp.index(next_cup)
    for pu in picked_up[::-1]:
        inp.insert(nc_index+1, pu)

    # print('destination: ', next_cup)

    while inp.index(next_chosen) != (di+1)%n:
        tmp = inp[-1]
        inp.insert(0,tmp)
        inp.pop(-1)

    move += 1
    di = (di+1)%n

# end
while inp[0] != 1:
        tmp = inp[-1]
        inp.insert(0,tmp)
        inp.pop(-1)

print('Part 1: ')
print(''.join(map(str,inp[1:])))
    