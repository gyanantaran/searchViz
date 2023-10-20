""" ANT TOUR """
cities = [i for i in range(N)]


def make_the_ant_traverse():
    # Start with a random city
    tour = []
    start_city = random.choice(cities)
    current_city = start_city

    remaining_cities = [i for i in range(N)]
    remaining_cities = remaining_cities.remove(current_city)

    while len(remaining_cities) != 0:
        probababilites_of_transition = []
        for v in remaining_cities:
            probababilites_of_transition.append(probability(u, v))

        next_city = np.random.choose(remaining_cities, 1, probababilites_of_transition)
        remaining_cities.remove(next_city)
        tour.append(next_city)
        current_city = next_city

    return tour


""" OPTIMISATION LOOP """
num_iterations = 100
list_of_tours = []

i = 0
while i < num_iterations:
    latest_tour = make_the_ant_traverse()
    list_of_tours.append(new_tour)

    cost_of_tour = cost(
        latest_tour
    )  # the traversal cost of the most recently calculated tour
    # update the rewards, sliding window of 2 cities
    start_city = latest_tour[0]

    i = 0
    u = latest_tour[0]
    v = latest_tour[1]
    while v != start_city:
        reward(u, v, cost_of_tour)

    i += 1
