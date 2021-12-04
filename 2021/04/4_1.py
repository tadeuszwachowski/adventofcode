import numpy as np

with open('input.txt') as f:
    numbers = [int(x) for x in f.readline().strip().split(',')]
    remains = f.readlines()
boardset = []

for i in range(len(remains)//6):
    
    # carve out important rows, split into tables and parse into integers
    bingo = np.array([[int(x) for x in row.strip().split()] for row in remains[6*i+1:6*i+6]])
    
    # get individual numbers for faster search
    nums = list(set(bingo.flatten()))

    boardset.append([nums,bingo])


bingo_win = []
last_n = 0
for n in numbers:
    for board in boardset:
        if n in board[0]:
            # update the board if hit
            pos = [(ix,iy) for ix, row in enumerate(board[1]) for iy, i in enumerate(row) if i == n]
            y,x = pos[0]
            # mark the hit spot with 100
            board[1][y][x] = 100
            board[0].remove(n)
        # if column hit or if row hit
        if 500 in np.sum(board[1],axis=0):
            bingo_win = board[1]
        if 500 in np.sum(board[1],axis=1):
            bingo_win = board[1]
    # if winning board found
    if bingo_win != []:
        last_n = n
        break

print("WINNING BOARD:\n",bingo_win)
print("LAST NUMBER: ",last_n)
parsed_bingo_win = [[num if num != 100 else 0 for num in row] for row in bingo_win]
remaining_sum = sum([sum(row) for row in parsed_bingo_win])
print("SUM OF REMAINING: ", remaining_sum)        

print("ANSWER: ",remaining_sum*last_n)
