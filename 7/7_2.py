import time
with open("day7.txt","r") as file:

    inside = {}

    for line in file:
        line = line.strip().replace('.','')
        style, contains = line.split(" bags contain ") # rozdziel na zewnętrzną i wewnętrzne
        elements = contains.split(", ") # rozdziel wewnętrzne na pojedyńcze

        for i in range(len(elements)):
            elements[i] = elements[i].replace('bags','bag').replace('bag','').strip() # wybierz tylko kolor
            inside[style] = []

            for smaller_bag in elements:
                if smaller_bag == 'no other':
                    pass
                else:
                    n = int(smaller_bag[0])
                    for k in range(n):
                        inside[style].append(smaller_bag[2:])
    
    to_check = []
    to_remove = []
    checked = []
    prev_count = 0
    next_count = 0

    for item in inside['shiny gold']:
        to_check.append(item)
        next_count = len(to_check)
        checked.append(item)

    # for item in inside.keys():
    #     print("Key: ", item,", value: ", inside[item])
    #     time.sleep(1.5)

    while prev_count != next_count:
        prev_count = next_count

        for bag in to_check:

            try:
                for item in inside[bag]:
                    checked.append(item)

                    if item != 'no other':
                        to_check.append(item)
                        next_count = len(to_check)

                to_remove.append(bag)

            except KeyError:
                pass

        for i in range(len(to_remove)): # usuń z listy do sprawdzenia już sprawdzone
            to_check.pop(0)
        to_remove = []

    for item in set(checked): # wypisz jakie torby musi zawierać SHINY GOLD
        print(item,checked.count(item))
    print(len(checked))

    