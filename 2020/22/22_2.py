played_games = []

def rc(deck1,deck2,g,prev_rounds):
    
    if g not in played_games:
        played_games.append(g)
    
    rnd = 0
    # print(f'=== Game {g} ===\n')
    while len(deck1) > 0 and len(deck2) > 0:
        rnd += 1
        if (deck1, deck2) in prev_rounds:
            # print(deck1,deck2)
            # print(prev_rounds)
            return 'P1'
            break
 
        prev_rounds.append((deck1[:],deck2[:]))

        card1 = deck1[0]
        card2 = deck2[0]

        # print(f'-- Round {rnd} (Game {g}) --')
        # print(f'P1 deck: {deck1}')
        # print(f'P2 deck: {deck2}')
        # print(f'P1 plays: {card1}')
        # print(f'P2 plays: {card2}')

        if card1 <= len(deck1[1:]) and card2 <= len(deck2[1:]):
            # print('Playing a sub-game to determine the winner...\n')
            result = rc(deck1[1:card1+1],deck2[1:card2+1],played_games[-1]+1,[])
            if result == 'P1':
                deck1 += [card1,card2]
                # print(f'Player 1 wins round {rnd} of game {g}!\n')
            elif result == 'P2':
                deck2 += [card2,card1]
                # print(f'Player 2 wins round {rnd} of game {g}!\n')

            deck1.pop(0)
            deck2.pop(0)

        else:

            if card1 > card2:
                deck1 += [card1,card2]
                # print(f'Player 1 wins round {rnd} of game {g}!\n')
            elif card1 < card2:
                deck2 += [card2,card1]
                # print(f'Player 2 wins round {rnd} of game {g}!\n')

            deck1.pop(0)
            deck2.pop(0)

    if len(deck1) == 0:
        # if g > 1:
        #     print(f'The winner of game {g} is player 2!\n\n...anyway, back to game {g-1}.')
        return 'P2'
    elif len(deck2) == 0:
        # if g > 1:
        #     print(f'The winner of game {g} is player 1!\n\n...anyway, back to game {g-1}.')
        return 'P1'


with open('day22.txt') as file:

    f = file.read()

    deck1 = [int(i) for i in f.split('\n\n')[0].split('\n')[1:]]
    deck2 = [int(i) for i in f.split('\n\n')[1].split('\n')[1:]]

winner = rc(deck1,deck2,1,[])

ans = 0
if winner == 'P2':
    print('WINNER P2: ', deck2)
    for i in range(len(deck2)):
        ans += deck2[i]*(len(deck2)-i)
    print('SCORE: ', ans)

elif winner == 'P1':
    print('WINNER P1: ', deck1)
    for i in range(len(deck1)):
        ans += deck1[i]*(len(deck1)-i)
    print('SCORE: ', ans)


