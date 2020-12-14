import numpy as np
import pandas as pd
import itertools

data = np.loadtxt('day14.txt',dtype=str,delimiter=' = ')

memory = {}

for i in data:
    if i[0] == 'mask':
        mask = np.array(list(i[1]))
    else:
        binnum = np.array(list(bin(int(i[1]))[2:].zfill(36)))
        new_num = np.array([i for i in mask])
        new_num[np.where(new_num == 'X')] = binnum[np.where(new_num == 'X')]
        memory[i[0][4:-1]] = int(''.join(list(new_num)),2)

print(sum(memory.values()))