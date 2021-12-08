count = 0
with open('input.txt') as f:
    for line in f:
        wires, output = line.strip().split(' | ')
        output_len = [len(x) for x in output.split()]
        # print(output_len)
        for x in output_len:
            # 2,3,4,7 are lengths of 1,7,4,8 segments
            if x in [2,3,4,7]:
                count += 1

print(count)