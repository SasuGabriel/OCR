# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 18:54:38 2020

@author: Vladina
"""

#Importam modulul xml.etree.ElementTree pentru a reprezenta fisierul XML 
#sub forma unui arbore cu noduri
import xml.etree.ElementTree as ET
#Parsam fisierul XML si il salvam ca arbore in variabila tree
tree = ET.parse('C:/Users/Vladina/Desktop/PSDT/CPetrescuUltimanoapte_Parser.xml')
#Salvam radacina arborelui in variabila root
root = tree.getroot()

#Pentru a elimina semnele de punctuatie, folosim functia RegexpTokenizer
#din pachetul nltk.tokenize
from nltk.tokenize import RegexpTokenizer
#Omitem semnele de punctuatie
tokenizer=RegexpTokenizer(r'\w+') 
for child in root.iter('word'): #Parcurgem nodurile arborelui
    token=tokenizer.tokenize(child.get("form")) #Tokenizam folosind functia tokenize
    #In cazul in care tokenul rezultat nu este o lista goala, vom afisa cuvantul si lemma
    if (len(token)!=0): 
        print("Word: ", token, ", Lemma: ", child.get("lemma"))