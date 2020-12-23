with open('day22.txt') as file:

    f = file.read()

    deck1 = [int(i) for i in f.split('\n\n')[0].split('\n')[1:]]
    deck2 = [int(i) for i in f.split('\n\n')[1].split('\n')[1:]]

rnd = 0
while len(deck1) > 0 and len(deck2) > 0:
    rnd += 1

    card1 = deck1[0]
    card2 = deck2[0]

    print(f'-- Round {rnd} --')
    print(f'P1 deck: {deck1}')
    print(f'P2 deck: {deck2}')
    print(f'P1 plays: {card1}')
    print(f'P2 plays: {card2}')


    if card1 > card2:
        deck1 += [card1,card2]
        print('Player 1 wins the round\n')
    elif card1 < card2:
        deck2 += [card2,card1]
        print('Player 2 wins the round\n')

    
    deck1.pop(0)
    deck2.pop(0)

ans = 0
if len(deck1) == 0:
    print('WINNER P2: ', deck2)
    for i in range(len(deck2)):
        ans += deck2[i]*(len(deck2)-i)
    print('SCORE: ', ans)

elif len(deck2) == 0:
    print('WINNER P1: ', deck1)
    for i in range(len(deck1)):
        ans += deck1[i]*(len(deck1)-i)
    print('SCORE: ', ans)



