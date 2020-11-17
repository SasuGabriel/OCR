# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 19:58:12 2020

@author: pc
"""

import xml.etree.ElementTree as ET
#Analizam fisierul XML rezultat in urma parsarii
tree1 = ET.parse('C:/Users/pc/Desktop/PrelucrareaStatisticaaDatelorText/laborator6/CamilPetrescuParser.xml')
#Elementul root1 contine un dictionar de atribute
root1 = tree1.getroot()

#Returnam specificatiile morfosintactice 
for dict1 in root1.iter('word'):
    print(dict1.get("form"),"Part of speech: "+ dict1.get("postag"), sep=",")
    
#Returnam specificatiile morfosintactice dupa tokenizare (se elimina semnele de punctuatie)
from nltk.tokenize import RegexpTokenizer
tokenizer=RegexpTokenizer(r'\w+')
for dict1 in root1.iter('word'):
    tokens=tokenizer.tokenize(dict1.get("form"))
    print(tokens, "Part of speech: "+ dict1.get("postag"), sep=",")
        
#Parsam fisierul XML rezultat in urma pos tagging
tree2 = ET.parse('C:/Users/pc/Desktop/PrelucrareaStatisticaaDatelorText/laborator6/CamilPetrescuTagger.xml')
#Elementul root2 contine un dictionar de atribute
root2 = tree2.getroot()
 
#Printam obiectele din dictionar:
for dict2 in root2.iter('W'):
    print(dict2.items())

#Printam lemma si partea de vorbire 
for dict2 in root2.iter('W'):
    print(dict2.get("LEMMA"), " - Part of speech: ", dict2.get("POS"))


