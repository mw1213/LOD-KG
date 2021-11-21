from owlready2 import *

def is_neighbours_with_poland(onto):
    return onto.search(is_neighbour_of=onto.Poland)

def population_bigger_than(onto, n):
    return [ind for ind in onto.individuals() if ind.population > n]

def area_smaller_than(onto, n):
    return [ind for ind in onto.individuals() if ind.area < n]

onto = get_ontology("test").load()

print(onto.classes)
print(list(onto.individuals()))
print(is_neighbours_with_poland(onto))
print(population_bigger_than(onto, 38267000))
print(area_smaller_than(onto, 78890))