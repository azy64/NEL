#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 11:36:03 2020

@author: claude
"""
import numpy as np
from SPARQLWrapper import SPARQLWrapper, JSON
import json

sparql = SPARQLWrapper("http://dbpedia.org/sparql")
query="""select distinct ?co ?ville ?pays ?localisation
where {?co a <http://dbpedia.org/ontology/City>. 
?co rdfs:label ?ville.
?co dbp:country ?pays.
?co dbp:location ?localisation
} LIMIT 40000"""
#FILTER langMatches(lang(?ville),'en')
sparql.setQuery(query)
sparql.setReturnFormat(JSON)
results = sparql.query().convert()
data_dict = dict()
data_list = []
for result in results["results"]["bindings"]:
     # creer le dictionnaire
    data_dict={'lien':result["co"]["value"],'ville':result["ville"]["value"],
               'Pays': result["pays"]["value"], 'localisation': result["localisation"]["value"]}
    # ajouter les pairs de nom et de valeur du dictionnaire dans une liste
    print("ville:",result["ville"]["value"])
    data_list.append(data_dict)
    #print(result["ville"]["value"])
fi = open("ville.json", 'w')
fi.write(json.dumps(data_list))