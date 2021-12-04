with open('input.txt') as f:
    rows = [line.strip() for line in f]
    height = len(rows)

# build the gamma string by counting zeros
gamma_str = ''
for i in range(len(rows[0])):
    # count for i-th column
    nth_bits =  [r[i] for r in rows]
    zeros = nth_bits.count('0')
    ones = height - zeros
    if zeros > ones:
        gamma_str = gamma_str + '0'
    else:
        gamma_str = gamma_str + '1'

# epsilon is the compliment of gamma
gamma = int(gamma_str,2)
max_bin = int('1'*len(rows[0]),2)
epsilon = max_bin-gamma

print(gamma*epsilon)
