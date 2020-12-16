with open("day15.txt") as file:

    f = file.read()

    history = [int(n) for n in f.split(",")]
    # history.append(0) # as in example
    turn = len(history) + 1

    while turn <= 30000000:
        # print("Turn: ", turn)
        last_spoken = history[-1]
        current_history = history[:-1]
        history_rev = current_history[::-1]
        # print("Last spoken:", last_spoken)

        if last_spoken in current_history:
            # print("diff=", turn-1, "- ", len(history_rev) - history_rev.index(last_spoken))
            diff = (turn-1) - (len(history_rev) - history_rev.index(last_spoken))
            last_spoken = diff
        else:
            last_spoken = 0
        history.append(last_spoken)
        # print("Next spoken: ", last_spoken)
        turn += 1

    print(history[-1])
    # print(history)
