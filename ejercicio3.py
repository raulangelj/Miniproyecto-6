#Miniproyecto 6
#Bryann Alfaro
#Raul Jimenez
#Donaldo Garcia

#Ejercicio 3
# %%
import itertools
import random

# %%
NUMBER_ITERATIONS = 300
# create an array of cities h1 to H8
# cities = [f"H{i}" for i in range(1, 9)]
cities = {
    "H1": {
        "H2": 5,
        "H4": 6,
        "H6": 4,
        "H8": 7,
    },
    "H2": {
        "H1": 5,
        "H3": 2,
        "H4": 4,
        "H5": 3,
    },
    "H3": {
        "H2": 2,
        "H4": 1,
    },
    "H4": {
        "H1": 6,
        "H2": 4,
        "H3": 1,
        "H5": 7,
    },
    "H5": {
        "H2": 3,
        "H4": 7,
        "H7": 6,
        "H8": 4,
    },
    "H6": {
        "H1": 4,
        "H7": 3,
    },
    "H7": {
        "H5": 6,
        "H6": 3,
        "H8": 2,
    },
    "H8": {
        "H1": 7,
        "H5": 4,
        "H7": 2,
    },
}
route = list(itertools.permutations(cities))
route = random.choice(route)
print(route)
best_route = route

for i in range(1, NUMBER_ITERATIONS):
    # swapp two successive cities and store it in a new route
    new_route = list(route)
    pos = random.randint(0, len(route) - 1)
    print(new_route)
    new_route[pos], new_route[(pos + 1) % len(route)] = new_route[(pos + 1)% len(route)], new_route[pos]
    print(new_route)
    # calculate the delta distance between the old route and the new route
    delta_distance = 0
    for i in range(len(route)):
        delta_distance += cities[route[i]][new_route[i]] - cities[new_route[i]][route[i]]
    # if the new route is better, then replace the old route with the new route
    if delta_distance < 0 or ():
        route = new_route
    # if the new route is not better, then calculate the probability of accepting the new route
    # else:
    #     probability = 1 / (1 + delta_distance)
    #     if random.random() < probability:
    #         route = new_route
    


# %%
