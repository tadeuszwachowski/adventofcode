with open("day13.txt","r") as file:

    f = file.read().splitlines()

    timestamp = int(f[0])
    buses = f[1]
    buses = buses.split(",")
    buses_set = set(buses)
    buses_set.remove("x")
    buses = list(buses_set)
    for b in range(len(buses)):
        buses[b] = int(buses[b])
    buses.sort()

    min_diff = 999999
    min_id = 0
    for n in buses:
        next_bus = timestamp + n - (timestamp % n)
        diff = next_bus - timestamp
        if diff < min_diff:
            min_diff = diff
            min_id = n
    # print(timestamp,buses)
    print(min_diff,min_id)
    print("Answer: ", min_diff*min_id)
