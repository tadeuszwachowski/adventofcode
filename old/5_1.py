with open("day5.txt","r") as file:
    max_id = 0
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
        seat_id = N*8 + E
        if seat_id > max_id:
            max_id = seat_id
        # print(line, N, S, E, W)
    print(max_id)