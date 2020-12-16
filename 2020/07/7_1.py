with open("day7.txt","r") as file:
    
    elders = {}
    checked = []
    
    for line in file:

        line = line.strip().replace('.','')
        style, contains = line.split(" bags contain ")
        elements = contains.split(", ")
        
        for i in range(len(elements)):
            elements[i] = elements[i].replace('bags','bag').replace('bag','')[2:].strip()
            lesser_bag = elements[i]
            if not lesser_bag in elders:
                # print("Adding:", style, " to elders:", lesser_bag)
                elders[lesser_bag] = [style]
            else:
                elders[lesser_bag].append(style)

    print(elders)

    prev_count = 0
    next_count = 0
    for item in elders['shiny gold']:
        checked.append(item)
        next_count = len(checked)

    while prev_count != next_count:
        prev_count = next_count
        for bag in checked:
            try:
                for item in elders[bag]:
                    if item not in checked:
                        checked.append(item)
                        next_count = len(checked)
            except KeyError:
                pass


    print("Max containing:", len(checked))