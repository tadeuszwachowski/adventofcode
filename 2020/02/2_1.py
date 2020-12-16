import re

passwords = []

with open("day2.txt","r") as file:
    for line in file:
        conds, passwd = line.strip().split(":")
        n, l = conds.split(" ")
        n_low, n_high = int(n.split("-")[0]), int(n.split("-")[1])
        
        c = 0
        for letter in passwd:
            if letter == l:
                c += 1
        if c >= n_low and c <= n_high:
            passwords.append(passwd)
        

print(len(passwords))