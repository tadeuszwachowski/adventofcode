lights = [ [0 for i in range(1000)]
                for j in range(1000) ]

with open('input.txt') as file:
    f = file.read().splitlines()

    for line in f:
        ins = line.split(' ')[-4] 
        ll = list(map(int,line.split(' ')[-3].split(',')))
        hr = list(map(int,line.split(' ')[-1].split(',')))

        if ins == 'on':
            for i in range(ll[0],hr[0]+1):
                for j in range(ll[1],hr[1]+1):
                    lights[i][j] = 1
        
        if ins == 'off':
            for i in range(ll[0],hr[0]+1):
                for j in range(ll[1],hr[1]+1):
                    lights[i][j] = 0

        if ins == 'toggle':
            for i in range(ll[0],hr[0]+1):
                for j in range(ll[1],hr[1]+1):
                    lights[i][j] = 1 if lights[i][j] == 0 else 0 

    ans = 0
    for row in lights:
        ans += sum(row)
    print('Part 1: ', ans)