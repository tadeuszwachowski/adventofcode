with open("day6.txt","r") as file:
    count = 0
    answers = set()
    i = 0

    for line in file:

        if line == "\n":
            i = 0
            count += len(answers)
            answers = set()

        else:
            line = line.strip()
            i += 1

            if i == 1:
                answers = set(line)

            else:
                answers = answers & set(line)

    count += len(answers) # ostatnia linijka
    print(count)

