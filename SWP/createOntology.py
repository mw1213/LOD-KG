from owlready2 import *
owlready2.JAVA_EXE = r"C:\\Program Files (x86)\\Java\\jre1.8.0_301\\bin"

onto = get_ontology("http://test.org/countries.owl")

with onto:
    class Country(Thing): pass
    class name(Country >> str, FunctionalProperty): pass
    class population(Country >> int, FunctionalProperty): pass          # Creating some properties
    class area(Country >> float, FunctionalProperty): pass
    class has_neighbour(ObjectProperty):
        domain    = [Country]
        range     = [Country]
    class is_neighbour_of(ObjectProperty):
        domain           = [Country]
        range            = [Country]
        inverse_property = has_neighbour
#    rule = Imp()
    # Rule: "Drug instance ?d     AND     price of ?d is ?p     AND     drug ?d has number_of_tablets = ?n
    #        AND     ?r = ?p/?n     ->      Drug ?d has price_per_tablet = ?r"
#    rule.set_as_rule("""Drug(?d), price(?d,?p), number_of_tablets(?d,?n), divide(?r, ?p, ?n) -> price_per_tablet(?d, ?r)""")

    # ("Germany", "Russia", "Czech Republic", "Slovakia", "Belarus", "Ukraine")
    poland = Country(name = "Poland", population = 38268000, area = 312696)
    
    germany = Country("Germany", population = 83019200 , area = 357578)

    czechRepublic = Country("Czech Republic", population =10649800, area=78866)



    germany.has_neighbour.append(poland)
    germany.is_neighbour_of.append(poland)
    germany.has_neighbour.append(czechRepublic)
    germany.is_neighbour_of.append(czechRepublic)
    poland.has_neighbour.append(czechRepublic)
    poland.is_neighbour_of.append(czechRepublic)

    print(germany.has_neighbour)
    print(germany.is_neighbour_of)    
    print(poland.is_neighbour_of)    
    print(poland.has_neighbour)

onto.save(file = "test", format = "rdfxml")