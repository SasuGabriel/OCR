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

postag=[]
from nltk.tokenize import RegexpTokenizer
tokenizer=RegexpTokenizer(r'\w+')
for dict1 in root1.iter('word'):
    postag.append(dict1.get("postag"))
        
words = [w for w in postag]
import nltk
word_freq  = nltk.FreqDist(words)
common_postags = word_freq.most_common(1000)
print (common_postags)


