from owlready2 import *

onto = get_ontology("test").load()

print(onto.classes)
print(list(onto.individuals()))
