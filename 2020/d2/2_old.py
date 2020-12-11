import re

passwords = []

with open("data.txt","r") as file:
    for line in file:
        conds, passwd = line.strip().split(":")
        n, l = conds.split(" ")
        regex = r"_l{_n}".replace("_n",n).replace("_l",l).replace("-",",")
        print(regex)
        found = re.search(regex,passwd)
        if found != None:
            # print(found.string)
            passwords.append(found.string)

print(len(passwords))