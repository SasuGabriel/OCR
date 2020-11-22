# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 19:58:12 2020

@author: pc
"""

import xml.etree.ElementTree as ET
#Analizam fisierul XML rezultat in urma parsarii
tree1 = ET.parse('D:/BusuiocI/Downloads/Camil Petrescu - Ultima noapte de dragoste, intaia noapte de razboi_Parser.xml')
#Elementul root1 contine un dictionar de atribute
root1 = tree1.getroot()

#Returnam specificatiile morfosintactice 
#for dict1 in root1.iter('word'):
#    print(dict1.get("form"),"Part of speech: "+ dict1.get("postag"), sep=",")
    
#Returnam specificatiile morfosintactice dupa tokenizare (se elimina semnele de punctuatie)
from nltk.tokenize import RegexpTokenizer
tokenizer=RegexpTokenizer(r'\w+')
tokenuri=[]
postags=[]

for dict1 in root1.iter('word'):
    tokens=tokenizer.tokenize(dict1.get("form"))
    #print(tokens, "Part of speech: "+ dict1.get("postag"), sep=",")
    tokenuri.append(tokens)
    postags.append(dict1.get("postag"))
tokensandpostags=list(zip(tokenuri, postags))
result = [r for r in tokensandpostags if all(x for x in r)]
result3 = [r for r in tokenuri if r != []]

import csv
with open("D:/BusuiocI/Downloads/tokensandpostags.txt", "w", newline='', encoding='utf-8') as f:
    writer = csv.writer(f, delimiter='-')
    writer.writerows(result)
    
import csv
with open("D:/BusuiocI/Downloads/tokens.txt", "w", newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerows(result3)
    
#Parsam fisierul XML rezultat in urma pos tagging
tree2 = ET.parse('D:/BusuiocI/Downloads/Camil Petrescu - Ultima noapte de dragoste, intaia noapte de razboi_Tagger.xml')
#Elementul root2 contine un dictionar de atribute
root2 = tree2.getroot()
 
#Printam obiectele din dictionar:
#for dict2 in root2.iter('W'):
#    print(dict2.items())
lemma=[]
postags=[]
#Printam lemma si partea de vorbire 
for dict2 in root2.iter('W'):
    #print(dict2.get("LEMMA"), " - Part of speech: ", dict2.get("POS"))
    lemma.append(dict2.get("LEMMA"))
    postags.append(dict2.get("POS"))
lemmaandpostag=list(zip(lemma, postags))
result2 = [r for r in lemmaandpostag if all(x for x in r)]

import csv
with open("D:/BusuiocI/Downloads/lemmaandpostags.txt", "w", newline='', encoding='utf-8') as f:
    writer = csv.writer(f, delimiter='-')
    writer.writerows(result2)
    
import csv
with open("D:/BusuiocI/Downloads/lemmas.txt", "w", newline='', encoding='utf-8') as f:
    f.writelines('\n'.join(lemma))
