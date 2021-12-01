import math
def get_divisors(n):
    divs = [1]
    for i in range(2,int(math.sqrt(n))+1):
        if n%i == 0:
            divs.extend([i,n//i])
    divs.extend([n])
    return list(set(divs))

# houses = [0]
for house_number in range(500000,1000000):
	elves = get_divisors(house_number)
	presents = sum(list(map(lambda x: x*10,elves)))
	# print(presents)
	if presents >= 33100000:
		print(house_number)
		break