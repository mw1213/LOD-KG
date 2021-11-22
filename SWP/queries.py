def is_neighbours_with_slovakia(onto):
    return onto.search(is_neighbour_of=onto.Slovakia)

def population_bigger_than(onto, n):
    return [ind for ind in onto.individuals() if ind.population > n]

def area_smaller_than(onto, n):
    return [ind for ind in onto.individuals() if ind.area < n]