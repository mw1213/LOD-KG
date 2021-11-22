from owlready2 import *
from queries import *

def get_names(arr):
    return 'Countries Found: ' + ', '.join([str(item).split('.')[-1] for item in arr])

onto = get_ontology("test").load()

print('***FIND A COUNTRY***')
choice = input('Pick a query:\n1. Slovakia Neighbours\n2. Min Population\n3. Max Area\nChoice: ')

if choice == '1':
    print(get_names(is_neighbours_with_slovakia(onto)))
elif choice == '2':
    min_population = float(input('Population Higher Than: '))
    print(get_names(population_bigger_than(onto, min_population)))
elif choice == '3':
    max_area = float(input('Area Smaller Than: '))
    print(get_names(area_smaller_than(onto, max_area)))
