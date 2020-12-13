with open("day13.txt","r") as file:

    f = file.read().splitlines()

    timestamp = int(f[0])

    buses = [int(bus) for bus in f[1].split(",") if bus != 'x']

    min_diff = 999999
    min_id = 0
    for n in buses:
        next_bus = timestamp + n - (timestamp % n)
        diff = next_bus - timestamp
        if diff < min_diff:
            min_diff = diff
            min_id = n

    print(min_diff,min_id)
    print("Answer: ", min_diff*min_id)
