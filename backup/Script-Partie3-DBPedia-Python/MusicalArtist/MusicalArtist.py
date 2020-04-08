#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 12:18:50 2020

@author: claude
"""

import numpy as np
from SPARQLWrapper import SPARQLWrapper, JSON
import json

sparql = SPARQLWrapper("http://dbpedia.org/sparql")
query="""select  ?f ?e
where {?f a <http://dbpedia.org/ontology/MusicalArtist>.
?f rdfs:label ?e
FILTER langMatches(lang(?e),'fr')
} LIMIT 90000"""
#FILTER langMatches(lang(?ville),'en')
sparql.setQuery(query)
sparql.setReturnFormat(JSON)
results = sparql.query().convert()
data_dict = dict()
data_list = []
for result in results["results"]["bindings"]:
     # creer le dictionnaire
    data_dict={'lien':result["f"]["value"],'Nom':result["e"]["value"]}
    # ajouter les pairs de nom et de valeur du dictionnaire dans une liste
    print("Nom:",result["e"]["value"])
    data_list.append(data_dict)
    #print(result["ville"]["value"])
fi = open("MusicalArtist.json", 'w')
fi.write(json.dumps(data_list))