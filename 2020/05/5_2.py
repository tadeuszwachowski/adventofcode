with open("day5.txt","r") as file:

    seat_table = [[0,0,0,0,0,0,0,0] for i in range(0,128)]

    for line in file:
        line = line.strip()
        S = 0
        N = 127
        W = 0
        E = 7
        for letter in line:
            if letter == 'F':
                tmp_v = (N+S+1)/2 - 1
                N = tmp_v
            if letter == 'B':
                tmp_v = (N+S+1)/2
                S = tmp_v
            if letter == 'L':
                tmp_h = (W+E+1)/2 - 1
                E = tmp_h
            if letter == 'R':
                tmp_h = (W+E+1)/2
                W = tmp_h
        seat_table[int(N)][int(E)] = 1


    # now we print the layout
    i = 0
    for row in seat_table:
        print(row, i)
        i += 1
 
    # and the answer
    print("#######################################")

    i = 0
    for row in seat_table:
        if sum(row) == 7:
            # print(row)
            print("row: %d, seat: %d, id: %d" % (i,row.index(0),i*8+row.index(0)))
        i += 1

