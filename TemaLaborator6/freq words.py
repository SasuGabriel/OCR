# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 09:16:45 2020

@author: Busuioci
"""
#Disclaimer: Output-urile "Camil Petrescu - Ultima noapte de dragoste, intaia noapte de razboi_Parser.xml" și "Camil Petrescu - Ultima noapte de dragoste, intaia noapte de razboi_Tagger.xml" sunt obținute dintr-un tagger și un parser astfel: 
#Aici e parserul: https://www.dropbox.com/s/fbr7glgv9yz44sy/bin_FdgParserRo.zip?dl=0
#Aici este pos tager-ul: https://www.dropbox.com/s/74gl7ubh3s10mcv/bin_PosRo.zip?dl=0

#Importam modulul xml.etree.ElementTree pentru a reprezenta fisierul XML 
#sub forma unui arbore cu noduri
import xml.etree.ElementTree as ET
#Parsam fisierul XML si il salvam ca arbore in variabila tree
tree = ET.parse('D:/BusuiocI/Downloads/Camil Petrescu - Ultima noapte de dragoste, intaia noapte de razboi_Parser.xml')
#Salvam radacina arborelui in variabila root
root = tree.getroot()

#Pentru a elimina semnele de punctuatie, folosim functia RegexpTokenizer
#din pachetul nltk.tokenize
from nltk.tokenize import RegexpTokenizer
#Omitem semnele de punctuatie
tokens=[]
from nltk.corpus import stopwords
stop_words = set(stopwords.words('romanian'))  # nltk stopwords list
tokenizer=RegexpTokenizer(r'\w+') 
for child in root.iter('word'): #Parcurgem nodurile arborelui
    token=tokenizer.tokenize(child.get("form")) #Tokenizam folosind functia tokenize
    #Eliminam tokenurile care sunt stopwords
    if (len(token)!=0 and token[0] not in stop_words): 
        tokens.append(token)
words = [w for doc in tokens for w in doc]
import nltk
word_freq  = nltk.FreqDist(words)
#Printam cele mai frecvente 1000 de cuvinte.
common_words = word_freq.most_common(1000)
print (common_words)
import numpy as np
np.savetxt("D:/BusuiocI/Downloads/common_words.txt", common_words, delimiter=",", fmt='%s', encoding='UTF-8') #trebuie deschis cu Notepad txt-ul, din cauza encoding-ului.
