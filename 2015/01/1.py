with open('input.txt') as file:
    f = ''.join(file.read().splitlines())
    
    # part 1
    print('Floor: ', f.count('(')-f.count(')'))
    
    # part 2
    floo = 0
    for c in range(len(f)):
        floo = floo+1 if f[c] == '(' else floo-1
        if floo == -1:
            print('First basement: ',c+1)
            break
            
        
