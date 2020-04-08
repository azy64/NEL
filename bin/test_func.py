#_*_coding:utf8_*_
import os, json, re, codecs, sys, collections, math, wikiapi, string,glob

json_files = '/home/azaria/zagabe/dico/'
def retourOb(ob):
    for j in ob:
        print(j)

def extract_data_from_json_files(rep=""):
    #on recupère la liste de fichiers json
    print("on commence ici ---------------------------")
    if rep=="":
        rep=json_files
    fichiers = glob.glob(rep+ '*json' )
    for fic in fichiers:
        ent=os.path.basename(fic)
        name=ent.split(".")
        ne=name[0]
        print("voici les fichier:",fic," --- ",ent)
        with open(fic) as json_data:
            data_dict = json.load(json_data)
            #print(data_dict[0])
            retourOb(data_dict)
        #break
extract_data_from_json_files("")