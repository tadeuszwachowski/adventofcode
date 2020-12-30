import itertools

with open('input.txt') as file:
    f = file.read().splitlines()

ingredients = {}

for line in f:
    values = line.split()

    name = values[0][:-1]
    capacity = int(values[2][:-1])
    durability = int(values[4][:-1])
    flavor = int(values[6][:-1])
    texture = int(values[8][:-1])
    calories = int(values[10])

    ingredients[name] = [capacity,durability,flavor,texture,calories]

    best_spoons = []
    best_score = 0
    best_spoons_500kcal = []
    best_score_500kcal = 0

    for a in range(0,101):
        for b in range(0,101-a):
            for c in range(0,101-(a+b)):
                for d in range(0,101-(a+b+c)):
                        if a+b+c+d == 100:
                            # print(a,b,c,d)
                            total_capacity, total_durability, total_flavor, total_texture, total_calories = 0,0,0,0,0

                            for name, n_spoons in zip(ingredients.keys(), [a,b,c,d]):
                                total_capacity += ingredients[name][0] * n_spoons
                                total_durability += ingredients[name][1] * n_spoons
                                total_flavor += ingredients[name][2] * n_spoons
                                total_texture += ingredients[name][3] * n_spoons
                                total_calories += ingredients[name][4] * n_spoons

                            if total_capacity < 0:
                                total_capacity = 0
                            if total_durability < 0:
                                total_durability = 0
                            if total_flavor < 0:
                                total_flavor = 0
                            if total_texture < 0:
                                total_texture = 0
                            if total_calories < 0:
                                total_calories = 0

                            cookie_score = total_capacity * total_durability * total_flavor * total_texture
                            
                            if cookie_score > best_score:
                                best_score = cookie_score
                                best_spoons = [a,b,c,d]

                            if total_calories == 500:
                                if cookie_score > best_score_500kcal:
                                    best_score_500kcal = cookie_score
                                    best_spoons_500kcal = [a,b,c,d]
                            
print('Part 1: ', best_score, ' spoons: ', best_spoons)
print('Part 2: ', best_score_500kcal, ' spoons: ', best_spoons_500kcal)