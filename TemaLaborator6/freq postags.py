# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 19:58:12 2020

@author: pc
"""
#Disclaimer: Output-urile "Camil Petrescu - Ultima noapte de dragoste, intaia noapte de razboi_Parser.xml" și "Camil Petrescu - Ultima noapte de dragoste, intaia noapte de razboi_Tagger.xml" sunt obținute dintr-un tagger și un parser astfel: 
#Aici e parserul: https://www.dropbox.com/s/fbr7glgv9yz44sy/bin_FdgParserRo.zip?dl=0
#Aici este pos tager-ul: https://www.dropbox.com/s/74gl7ubh3s10mcv/bin_PosRo.zip?dl=0

import xml.etree.ElementTree as ET
#Analizam fisierul XML rezultat in urma parsarii
tree1 = ET.parse('D:/BusuiocI/Downloads/Camil Petrescu - Ultima noapte de dragoste, intaia noapte de razboi_Parser.xml')
#Elementul root1 contine un dictionar de atribute
root1 = tree1.getroot()

postag=[]
for dict1 in root1.iter('word'):
    postag.append(dict1.get("postag"))
        
words = [w for w in postag]
import nltk
word_freq  = nltk.FreqDist(words)
common_postags = word_freq.most_common(1000)
print (common_postags)
import numpy as np
np.savetxt("D:/BusuiocI/Downloads/common_postags.csv", common_postags, delimiter=",", fmt='%s')
