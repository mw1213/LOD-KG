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

    poland = Country(name = "Poland", population=38268000, area=312696)
    
    germany = Country("Germany", population=83019200 , area=357578)
    czechRepublic = Country("Czech Republic", population=10649800, area=78866)
    slovakia = Country("Slovakia", population=5459000, area=49034)
    ukraine = Country("Ukraine", population=44130000, area=603700)
    belarus = Country("Belarus", population=9399000, area=207600)
    lithuania = Country("Lithuania", population=2795000, area=65300)
    russia = Country("Russia", population=144100000, area=17125191)

    germany.has_neighbour.append(poland)
    germany.is_neighbour_of.append(poland)
    germany.has_neighbour.append(czechRepublic)
    germany.is_neighbour_of.append(czechRepublic)

    czechRepublic.has_neighbour.append(germany)
    czechRepublic.is_neighbour_of.append(germany)
    czechRepublic.has_neighbour.append(poland)
    czechRepublic.is_neighbour_of.append(poland)
    czechRepublic.has_neighbour.append(slovakia)
    czechRepublic.is_neighbour_of.append(slovakia)

    slovakia.has_neighbour.append(ukraine)
    slovakia.is_neighbour_of.append(ukraine)
    slovakia.has_neighbour.append(poland)
    slovakia.is_neighbour_of.append(poland)
    slovakia.has_neighbour.append(czechRepublic)
    slovakia.is_neighbour_of.append(czechRepublic)

    ukraine.has_neighbour.append(slovakia)
    ukraine.is_neighbour_of.append(slovakia)
    ukraine.has_neighbour.append(poland)
    ukraine.is_neighbour_of.append(poland)
    ukraine.has_neighbour.append(belarus)
    ukraine.is_neighbour_of.append(belarus)

    belarus.has_neighbour.append(ukraine)
    belarus.is_neighbour_of.append(ukraine)
    belarus.has_neighbour.append(poland)
    belarus.is_neighbour_of.append(poland)
    belarus.has_neighbour.append(lithuania)
    belarus.is_neighbour_of.append(lithuania)

    lithuania.has_neighbour.append(belarus)
    lithuania.is_neighbour_of.append(belarus)
    lithuania.has_neighbour.append(poland)
    lithuania.is_neighbour_of.append(poland)
    lithuania.has_neighbour.append(russia)
    lithuania.is_neighbour_of.append(russia)

    germany.has_neighbour.append(poland)
    germany.is_neighbour_of.append(poland)
    germany.has_neighbour.append(lithuania)
    germany.is_neighbour_of.append(lithuania)

    poland.has_neighbour.append(czechRepublic)
    poland.is_neighbour_of.append(czechRepublic)
    poland.has_neighbour.append(germany)
    poland.is_neighbour_of.append(germany)
    poland.has_neighbour.append(slovakia)
    poland.is_neighbour_of.append(slovakia)
    poland.has_neighbour.append(ukraine)
    poland.is_neighbour_of.append(ukraine)
    poland.has_neighbour.append(belarus)
    poland.is_neighbour_of.append(belarus)
    poland.has_neighbour.append(lithuania)
    poland.is_neighbour_of.append(lithuania)
    poland.has_neighbour.append(russia)
    poland.is_neighbour_of.append(russia)

    # print(germany.has_neighbour)
    # print(germany.is_neighbour_of)    
    # print(poland.is_neighbour_of)    
    # print(poland.has_neighbour)

onto.save(file = "test", format = "rdfxml")