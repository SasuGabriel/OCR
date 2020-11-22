# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 19:58:12 2020

@author: pc
"""

""" Afisare tokens & postags """
import xml.etree.ElementTree as ET
#Analizam fisierul XML rezultat in urma parsarii
tree1 = ET.parse('C:/Users/pc/Desktop/PrelucrareaStatisticaaDatelorText/laborator6/CamilPetrescuParser.xml')

#In elementul root1 avem radacina arborelui care contine un dictionar de atribute
root1 = tree1.getroot()
print(root1.attrib)

#Afisam obiectele din dictionar sub forma (cheie, valoare):
for dict1 in root1.iter('word'):
    print(dict1.items())
    
#Parcurgem arborele si afisam specificatiile morfosintactice pentru cuvinte +
#semne de punctuatie
for dict1 in root1.iter('word'):
    print("Element: "+ dict1.get("form"),"Part of speech: "+ dict1.get("postag"), sep=" -> ")
    
#Afisam specificatiile morfosintactice dupa tokenizare utilizand o functie
#de tokenizare cu expresii regulate, RegexpTokenizer
from nltk.tokenize import RegexpTokenizer
tokenizer=RegexpTokenizer(r'\w+')

#Moduri de afisare:
#1. Print tokens si postags
#Parcurgem arborele si salvam tokens in lista
for dict1 in root1.iter('word'):
    tokens=tokenizer.tokenize(dict1.get("form"))
    #Se intampla ca dupa eliminarea punctuatiei, sa ramana liste de tokeni vide
    #Daca lista nu este nula, printam tokenul si specificatia morfosintactica corespunzatoare
    if (len(tokens)!=0):
        print("Token:", tokens, "-> Part of speech: "+ dict1.get("postag"))
        
    
#2. Import tokens si postags intr-un dataframe & export dataframe in fisiere txt si csv
#Cream o lista in care vor fi adaugati tokens si postags
list1=[]
#Denumim coloanele dataframe-ului
cols1=["token", "postag"]
#Parcurgem arborele, salvand tokens & postags in liste
for dict1 in root1.iter('word'):
    tokens=tokenizer.tokenize(dict1.get("form"))
    postags=tokenizer.tokenize(dict1.get("postag"))
    #Se intampla ca dupa eliminarea punctuatiei, sa ramana liste de tokeni vide
    #Daca listele nu sunt nule, adaugam in list1
    if (len(tokens)!=0 and len(postags)!=0):
        list1.append({'token':tokens,'postag':postags})
import pandas as pd
df1=pd.DataFrame(list1, columns=cols1)
print(df1)
df1.to_csv(r'C:/Users/pc/Desktop/PrelucrareaStatisticaaDatelorText/laborator6/Token_and_Postag.txt',header=cols1,index=False, sep=' ')
df1.to_csv('C:/Users/pc/Desktop/PrelucrareaStatisticaaDatelorText/laborator6/Token_and_Postag.csv', index=False)


""" Afisare lemmas & postags """
#Parsam fisierul XML rezultat in urma pos tagging
tree2 = ET.parse('C:/Users/pc/Desktop/PrelucrareaStatisticaaDatelorText/laborator6/CamilPetrescuTagger.xml')
#In elementul root2 avem radacina arborelui care contine un dictionar de atribute
root2 = tree2.getroot()
print(root2.attrib)
 
#Afisam obiectele din dictionar sub forma (cheie, valoare):
for dict2 in root2.iter('W'):
    print(dict2.items())

#Afisam lemma si partea de vorbire, eliminand semnele de punctuatie
from nltk.tokenize import RegexpTokenizer
tokenizer=RegexpTokenizer(r'\w+')

#Printare lemmas si postags
#Parcurgem arborele, salvand lemmas in liste
for dict2 in root2.iter('W'):
    lemmas=tokenizer.tokenize(dict2.get("LEMMA"))
    #Daca lista nu este nula, printam lemma si partea de vorbire corespunzatoare
    if (len(lemmas)!=0):
        print("Lemma: ", lemmas, "-> Part of speech: ", dict2.get("POS"))