def filter_bits(array,flip):
    i = 0
    while len(array) > 1:
        # count for i-th column
        height = len(array)
        nth_bits =  [c[i] for c in array]
        zeros = nth_bits.count('0')
        ones = height - zeros
        if zeros > ones:
            most_common = 0
        else:
            most_common = 1
        # correction due to different oxgen and co2 rules
        most_common = str(most_common ^ flip)

        array = list(filter(lambda x: x[i]==most_common, array))
        # jump to next column
        i += 1
    return array

with open('input.txt') as f:
    rows = [line.strip() for line in f]
    height = len(rows)

oxgen = rows.copy()
co2 = rows.copy()

oxgen = filter_bits(oxgen,1)
co2 = filter_bits(co2,0)

oxgen_value = int(oxgen[0],2)
co2_value = int(co2[0],2)

print(oxgen_value*co2_value)
