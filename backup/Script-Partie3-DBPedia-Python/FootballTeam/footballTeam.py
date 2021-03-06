#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 10:15:20 2020

@author: claude
"""
import numpy as np
from SPARQLWrapper import SPARQLWrapper, JSON
import json

sparql = SPARQLWrapper("http://dbpedia.org/sparql")
query="""select  ?f ?e
where {?f a <http://dbpedia.org/ontology/SoccerClub>.
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
    data_dict={'lien':result["f"]["value"],'footballTeam':result["e"]["value"]}
    # ajouter les pairs de nom et de valeur du dictionnaire dans une liste
    print("footballTeam:",result["e"]["value"])
    data_list.append(data_dict)
    #print(result["ville"]["value"])
fi = open("footballTeam.json", 'w')
fi.write(json.dumps(data_list))

