with open("data.txt","r") as file:
    
    count = 0
    answers = []
    
    for line in file:

        if line == "\n":
            count += len(answers)
            answers = []
        else:
            for l in line:
                if not l in answers and l != "\n":
                    answers.append(l)

    count += len(answers)
    
    print(count)

    