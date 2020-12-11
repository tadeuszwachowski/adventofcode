import re

passwords = []

with open("day2.txt","r") as file:
    for line in file:
        conds, passwd = line.strip().split(":")
        n, l = conds.split(" ")
        n_low, n_high = int(n.split("-")[0]), int(n.split("-")[1])
        # print(n_low, n_high, l, passwd, passwd[n_low-1], passwd[n_high-1])
        passwd = passwd.lstrip()
        if passwd[n_low-1] == l and passwd[n_high-1] != l:
            passwords.append(passwd)
            # print(n_low, n_high, l, passwd, passwd[n_low-1], passwd[n_high-1])
        if passwd[n_low-1] != l and passwd[n_high-1] == l:
            passwords.append(passwd)
            # print(n_low, n_high, l, passwd, passwd[n_low-1], passwd[n_high-1])

print("Length: ",len(passwords))