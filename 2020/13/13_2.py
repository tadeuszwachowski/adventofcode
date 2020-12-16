from functools import reduce
from operator import mul
import math

with open("day13.txt","r") as file:

    f = file.read().splitlines()

    timestamp = int(f[0])
    buses = f[1]
    buses = buses.split(",")
    for b in range(len(buses)):
        if buses[b] != 'x':
            buses[b] = int(buses[b])
    uniq_buses = set(buses)
    if 'x' in uniq_buses:
        uniq_buses.remove('x')
    num_buses = len(uniq_buses)
    # print(num_buses)
    ts = [i for i in range(len(buses))]
    

    buses_narrow = []
    ts_narrow = []
    for k in range(len(buses)):
        if buses[k] != 'x':
            buses_narrow.append(buses[k])
            ts_narrow.append(ts[k])

    print("Buses: ", buses_narrow)
    print("ts: ", ts_narrow)
    
    def chinese_remainder(n, a):
        p = math.prod(n)
        total = sum(y * pow(p // x, -1, x) * (p // x) for x, y in zip(n, a))
        # print(p)
        # print(total)
        return p - (total % p)
    n = buses_narrow
    a = ts_narrow

    print(int(chinese_remainder(n,a)))