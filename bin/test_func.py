#_*_coding:utf8_*_
import os, json, re, codecs, sys, collections, math, wikiapi, string,glob

json_files = '/home/azaria/zagabe/dico/'
def retourOb(ob):
    for j in ob:
        print(j[0])

def extract_data_from_json_files(rep=""):
    #on recupère la liste de fichiers json
    print("on commence ici ---------------------------")
    dico={}
    if rep=="":
        rep=json_files
    fichiers = glob.glob(rep+ '*json' )
    for fic in fichiers:
        ent=os.path.basename(fic)
        #clename=ent.split(".")
        #ne=name[0]
        print("voici les fichier:",fic," --- ",ent)
        with open(fic) as json_data:
            data_dict = json.load(json_data)
            for obj in data_dict:
                cl=list()
                for c in obj.keys():
                    cl.append(c)
                if cl[0]=="lien":
                    dico[obj[cl[1]]]=obj[cl[0]]
                else:
                    dico[obj[cl[0]]]=obj[cl[1]]  
            #print("--------------------------------------------------------------------")
            #print(dico)                              
        #break
    return dico    
extract_data_from_json_files("")