import hashlib

# inp = b'abcdef609043'
found1 = False
found2 = False
i = 0

while not found1 or not found2:

    inp = 'ckczppom' + str(i)
    m = hashlib.md5(inp.encode())
    res = m.hexdigest()
    if res[:5] == '00000':
        if not found1:
            print('Part 1: ', i, res)
        found1 = True
    if res[:6] == '000000':
        print('Part 2: ', i, res)
        found2 = True
    i += 1
