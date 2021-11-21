from owlready2 import *

onto = get_ontology("test").load()

with onto:
    sync_reasoner()
