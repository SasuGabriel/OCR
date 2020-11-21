# -*- coding: utf-8 -*-
"""
Created on Sat Nov 21 20:16:29 2020

@author: Andre
"""
import xml.etree.ElementTree as ET
tree = ET.parse('C:/Users/Andre/Downloads/Camil Petrescu - Ultima noapte de dragoste, intaia noapte de razboi_Parser.xml')
#Salvam radacina arborelui in variabila root
root = tree.getroot()
#definim coloanele cu numele de form si lemma
df_cols=['form','lemma']
rows=[]
#omitem semnele de punctuatie
from nltk.tokenize import RegexpTokenizer
tokenizer=RegexpTokenizer(r'\w+')
from nltk.corpus import stopwords
stop_words = set(stopwords.words('romanian'))
#parcurgem arborele pentru a ne returna forma si lemma
for node in root.iter('word'):
    form=tokenizer.tokenize(node.get('form'))
    lemma=tokenizer.tokenize(node.get('lemma'))   
    if(len(form)!=0 and len(lemma)!=0 and form[0] not in stop_words and lemma[0] not in stop_words):
        rows.append({'form':form,'lemma':lemma})

#importam ceea ce am obtinut intr-un dataframe df
import pandas as pd
df=pd.DataFrame(rows, columns=df_cols)
print(type(df))
df.to_csv(r'C:/Users/Andre/Downloads/form_and_lemma.txt',header=df_cols,sep='-')

#definim coloanele pentru lemma si postag
df_cols1=['lemma','postag']
rows1=[]

for node in root.iter('word'):
    lemma=tokenizer.tokenize(node.get('lemma'))
    postag=tokenizer.tokenize(node.get('postag'))   
    if(len(postag)!=0 and len(lemma)!=0):
        rows1.append({'lemma':lemma,'postag':postag})
#importam ceea ce am obtinut intr-un dataframe df1
import pandas as pd
df1=pd.DataFrame(rows1, columns=df_cols1)
print(type(df))
df1.to_csv(r'C:/Users/Andre/Downloads/lemma_and_postag.txt',header=df_cols,sep='-')


