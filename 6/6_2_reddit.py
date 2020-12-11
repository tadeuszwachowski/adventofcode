#read input, strip non-printable characters at the end, then use list comprehensions to make a list of groups with each group being a list of questions that were answered in the affirmative
groups=[s.split("\n") for s in open("day6.txt","r").read().rstrip().split("\n\n")]

#for each part of the problem, create a function that takes a list of answers within a group of people and returns a set of responses for the group
part_funcs=[[1,lambda g:set("".join(g)),"anyone"],[2,lambda g:set.intersection(*map(set,g)),"everyone"]]

#Repeat for each function: for each group count how the number of elements in the set for each group and then sum that list
print("\n".join(["Part "+str(z[0])+": "+str((lambda fp: sum([len(fp(g)) for g in groups]))(z[1]))+" (answered yes by "+z[2]+" in the group)" for z in part_funcs]))