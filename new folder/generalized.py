# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 14:56:38 2021

@author: Andre
"""


import json
with open('D:/BusuiocI/Desktop/134_4.json', encoding='utf-8') as f:
  data = json.load(f)
text=data['fullTextAnnotation']['text'].replace('\n',' ')

import cv2
import os
import numpy as np
import pytesseract
import pandas as pd
from pytesseract import Output
from  PIL import  Image
pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'
img=cv2.imread("H:/FEAA/master/anul 2/Prelucrarea statistica a datelor text/facturi si chitante/IMG20201112121804.jpg")
#READ FROM PDF
#Download Poppler Latest binary from http://blog.alivate.com.au/poppler-windows/
import PyPDF2 
from pdf2image import convert_from_path
images=convert_from_path('H:/FEAA/master/anul 2/Prelucrarea statistica a datelor text/facturi si chitante/Doua_pagini.pdf',500,poppler_path=r'H:/Downloads/poppler-0.68.0_x86/poppler-0.68.0/bin')
for i, image in enumerate(images):
    fname='image'+str(i)+'.png'
    image.save(fname,'PNG')
img=cv2.imread("C:/Users/Andre/image0.png")
custom_config = r'--oem 3 --psm 12'
text=pytesseract.image_to_string(img, config=custom_config, lang="ron")
text=text.replace('\n',' ')
import cv2
import pytesseract
img=cv2.imread("D:/BusuiocI/Desktop/image0.png")
pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'
custom_config = r'--oem 3 --psm 12'
text=pytesseract.image_to_string(img, config=custom_config, lang="ron")
img2=cv2.imread("C:/Users/Andre/image1.png")
pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'
custom_config = r'--oem 3 --psm 12'
text2=pytesseract.image_to_string(img2, config=custom_config, lang="ron")
text=text+text2
text=text.replace('\n\n',' ')
from unidecode import unidecode
unidecode(text)
text="e-on FACTURA FISCALA Seria BCEMF nr. 835503401 E.ON Moldova Furnizare S.A. C.I.F. RO21537385 R.C. J04/648/2007 Bacau, str. Stefan cel Mare, nr. 22 Capital social 138.693.790 RON Trezorerie RO87TREZ0615069XXX004267 BRD Bacau RO98BRDE040SV11128470400 - ING Bacau RO58INGB0008008151258927 C.R.C. CRC lasi Municipal Adresa IASI, Str., AGATHA BIRSESCU, 4, Call Center 0235305555, 0801000939 Deranjamente prefix judet + 929 www.eon-energie.ro 3103 1412583 BUSUIOC PETRICA VASILE Sos. NATIONALA Nr.46 D5D7/4 IASI 700606 1511177 Jud. IASI Simbol variabil 1412583090 COD CLIENT 10412583 NLC 1412583 Data facturii 08.09.2009 Data scadentei 23.09.2009 Stimate client, Vi s-a intocmit urmatoarea factura: Produse si servicii facturate Energia electrica activa Abonament/Rezervare Taxa RADIO Taxa TV Accize Suma facturata (fara TVA) 113,75 lei 9,02 lei 5,00 lei 8,00 lei 1,14 lei CASNIC Prezumat Contract: 1.9611.008573 28.12.2001 Perioda de facturare: 10.07.2009-07.09.2009 Sistem de facturare: Facturare la 2 luni Temei legal preturi: ORD.ANRE 134 30.12.2008 Temei legal accize: Legea 571 22.12.2003 Curs valutar: 1 euro = 3,7364 Lei Acciza unitara consum necomercial: 0,84 Acciza unitara consum comercial: 0,42 Total factura fara TVA BAZA impozitare TVA TVA 19% Total factura cu TVA Alte sume TOTAL DE PLATA 136,91 123,91 23,54 160,45 lei lei lei lei lei lei 160,45 PERIOADA CITIRE CONSUM SERIE/CONST CONTOR INDEX VECHI UM CANT INDEX NOU PERIOADA TIP FACTURARE TARIF DENUMIRE CONCEPT FACTURAT PRET UNITAR VALOARE (cu TVA) 1412583 NATIONALA 46/D5 D 74 IASI 1412583 09.07-07.09 1761285 1 2753 3117 Zile 60 2 364||10.07-07.09 J CR 10.07-07.09 10.07-07.09 10.07-07.09 J CR Rezervare Taxa Radio Taxa TV Energie activa Accize MWh necomercial Luni Luni 0,1503 2,5000 4,0000 0,3125 2 10,73 5,00 8,00 135,36 1,36 364 kWh MWh 0.364 61 zile 5.967 kWh/zi TOTAL 364 TOTAL 160,45 Sold debitor anterior 0,00 lei Va informam ca Soldul debitor anterior nu este inclus in TOTAL DE PLATA.In Total de plata factura curenta cazul in care nu a fost achitat pâna la primirea acestei facturi pentru a evita riscul 160,45 lei Sold debitor curent deconectarii pentru neplata, va rugam sa va prezentati la casieria E.ON Moldova 160,45 lei Furnizare. La plata facturii va rugam sa indicati intotdeauna Simbolul Variabil. Aceasta informatie se gaseste evidentiata in partea din dreapta sus a facturii. sgcbatch BUSUIOC PETRICA VASILE Sos. NATIONALA Nr.46 D5D7/4 IASI 700606 COD BARE PENTRU PLATA FACTURA COD CLIENT 10412583 NLC 1412583 Factura Fiscala Seria BCEMF nr. 835503401 Data facturii 08.09.2009 Data scadentei 23.09.2009 Simbol variabil 1412583090 TOTAL DE PLATA 160,45 lei Jud. IASI 0141258301070909090000000001604510 ||| |||| "
#REGEX UNIVERSAL
import re
telephonecorect=re.findall("Telefon\:? (0\d{9}\,?\s)| (0\d{9}\,?\s)|(0\d{4} \d{2} \d{2} \d{2}\,?\s)| (0\d{9}): ([0-9]{10})|(0\d{3} \d{3} \d{3})\,?\s|\+[0-9]{2}\s[0-9]{2}\s[0-9]{3}\s[0-9]{2}\s[0-9]{2}", text)
telefon=re.findall('\s([0-9]{6,})\,?\s?|\s([0-9]{4}\.[0-9]{3}\.[0-9]{3})\,?\s|\s([0-9]{4}\s[0-9]{3}\s[0-9]{3})\,?\s|\s([0-9]{10})\,?\s?|\s([0-9]{4}\s[0-9]{2}\s[0-9]{2})\,?\s?|([0-9]{3}\.[0-9]{3}\.[0-9]{3})\,?\s?',text)
postalcode=re.findall("\s(\d{6})\s|\s(\d{6})\s|([A-Z]{2,}\-[0-9]{6})\s", text)

CIF=re.findall("\s[A-Z][A-Z]\d{4,10}\s|\s[A-Z][A-Z]\d{6,10}\s|\sR\d{9}\s|\sR\d{9}|Cod de inregistrare fiscala\:? +([A-z0-9]{9})|CIF\:?\s([A-Z][A-Z]\d{4,10})|CIF\:?\s([A-Z]{1,}[0-9]{8,})|CIF\:?\s([A-Z]{1,}[0-9]{2,}\s[0-9]{2,})|\(C\.I\.F\.\)\:\s([A-Z]{1,}[0-9]{7,})|C\.I\.F\.\s([A-Z]{1,}[0-9]{7,})", text)
cartedeidentitate=re.findall("([A-Z]{2}[0-9]{6})", text)
seria=re.findall("Seria [A-Z]{4} nr. [0-9]{7}|SERIA [A-Z]{4} +NR. +[0-9]{11}\/[0-9]{4}\-[0-9]{2}-[0-9]{2}|Seria şi nr\.\:\s[A-Z0-9]{6}\-[A-Z]", text)
seria=re.findall("Seria [A-Z]{4} nr. [0-9]{7}|SERIA [A-Z]{4} +NR. +[0-9]{11}\/[0-9]{4}\-[0-9]{2}-[0-9]{2}|Seria şi nr\.\:\s[A-Z0-9]{6}\-[A-Z] |([A-Z]{1,}\-[0-9]{1,}\s)", text)
seria=re.findall("Seria ([A-Z]{4} nr. [0-9]{7})|SERIA ([A-Z]{3,}\sNR\.\s[0-9]{11}\/[0-9]{4}\-[0-9]{2}\-[0-9]{2})|Seria şi nr\.\:?\s([A-Z0-9]{6}\-[A-Z])|([A-Z]{1,}\-[0-9]{1,})|\s([A-Z]{2}\s[A-Z]{2,} nr. [0-9]{7,})|([A-Z]{2,}[0-9]{2}\s\/\s[0-9]{8,})|Seria\:?\s([A-Z]{2,}\s[A-Z]{3,})|Seria\:?\s([A-Z]{2,})|SERIA\s([A-Z]{1,}[0-9]{2,})\s", text)
seria2=re.findall("SERIA [A-Z]{3,}\sNR\.\s[0-9]{11}\/[0-9]{4}\-[0-9]{2}\-[0-9]{2}",text)
numepersoana=re.findall("([A-Z\-]{4,})\s+([A-Z\-]{5,})?\s?([A-Z\-]{5,})|([A-z]{3,}\s[A-z]{3,})", text)

perioadafacturare=re.findall("[0-9]{2}\.[0-9]{2}\.[0-9]{4}\-[0-9]{2}\.[0-9]{2}\.[0-9]{4}|[0-9]{2}\.[0-9]{2}\.[0-9]{2}\s\-\s[0-9]{2}\.[0-9]{2}\.[0-9]{2}|[0-9]{2}\.[0-9]{2}\.[0-9]{2}\-[0-9]{2}\.[0-9]{2}\.[0-9]{2}|[0-9]{2}\.[0-9]{2}\.[0-9]{4}\s\-\s[0-9]{2}\.[0-9]{2}\.[0-9]{4}", text)

datafacturare=re.findall("\Data facturării\:?\s([0-9]{2}\.[0-9]{2}\.[0-9]{4})\s|Data\:?\s([0-9]{4}\-[0-9]{2}\-[0-9]{2})\s|Data emiterii\:? +([0-9]{2}\.[0-9]{2}\.[0-9]{4})|Data facturii\:? ([0-9]{2}\.[0-9]{2}\.[0-9]{4})|din\:?\s([0-9]{2}\.[0-9]{2}\.[0-9]{4})\s|Data facturii\:? ([0-9]{2}\/[0-9]{2}\/[0-9]{4})\s|din data de\:?\s([0-9]{2}\.[0-9]{2}\.[0-9]{4})|Data\:?\s([0-9]{2}\.[0-9]{2}\.[0-9]{4})|Data emiterii\:?\s([0-9]{2}\.[0-9]{2}\.[0-9]{4})|Data avizului\:?\s([0-9]{2}\/[0-9]{2}\/[0-9]{4})", text)

datascadenta=re.findall("Total de plată pană la\:?\s([0-9]{2}\.[0-9]{2}\.[0-9]{4})|Scadent\:?\s([0-9]{4}\-[0-9]{2}\-[0-9]{2})\s|până la data de\:? ([0-9]{2}\.[0-9]{2}\.[0-9]{4})|scadenta\:?\s([0-9]{2}\.[0-9]{2}\.[0-9]{4})\s|Data scadenţei\:? ([0-9]{2}\/[0-9]{2}\/[0-9]{4})|Scadenta\:?\s([0-9]{2}\.[0-9]{2}\.[0-9]{4})\s|Data scadentă\:?\s([0-9]{2}\.[0-9]{2}\.[0-9]{4})|Ultima zi de plată\:?\s([0-9]{2}\.[0-9]{2}\.[0-9]{4})|Ultima zi de plata\:?\s([0-9]{2}\.[0-9]{2}\.[0-9]{4})|Data scadentei\:?\s([0-9]{2}\.[0-9]{2}\.[0-9]{4})", text)

totalplata=re.findall("(\-?\d+,\d{2})\s|\s(\-?\d+\.\d{2})\s|Vă rugăm să achitaţi suma de\:?\s(\-?\d+,\d{2})\s|TOTAL DE PLATA .*? (\-?\d+.\d{2})\s|(\-?\d+\.\d{3},\d{2})\s|(\-?\d+?\.\d{3}\.\d{3}\,\d{2})|\s(\-?[0-9]{1,}\.[0-9]{2})\s", text)
totalplata2=[element for tupl in totalplata for element in tupl]
without_empty_strings = [string for string in totalplata2 if string != ""]
#j=[]
#for i in without_empty_strings:
#    j.append(float(i.replace(',','.')))
#totalplata=max(j)
IBAN=re.findall("([A-Z]{2}[0-9]{2}\s[a-zA-Z0-9]{4}\s[a-zA-Z0-9]{4}\s[a-zA-Z0-9]{4}\s[a-zA-Z0-9]{4}\s[a-zA-Z0-9]{4})\s|\s([A-Z0-9]{24})\s|\s([A-Z0-9]{11}\s[0-9]{13})|([A-Z]{2}[0-9]{2}[a-zA-Z0-9]{9}\s[a-zA-Z0-9]{13})", text)

codfacturare=re.findall("\s([0-9]{14})\s",text)
furnizor=re.findall("[0-9]+ (.*? S.A.)|FURNIZOR\:? (.*? SRL)|(FIRMA .*?) Cumparator|(.*? SA)|(.*? SRL)|(.*? S.A.)|Furnizor Client(.*? SRL)|Furnizor\:? (.*? SA)|Furnizor\:? (.*? SRL)|Furnizor\:?\s(.*? S\.A\.)|Furnizor\:?\s(.*? S\.R\.L\.)|([A-Z]{1}[A-z]+.*? S\.A\.)|([a-z\-]{3,}\-[a-z\-]{3,}\-[a-z\-]{3,})|([A-Z]{1}\.[A-Z]{2})\s|([A-Z\-]{1,}\.[A-Z\-]{2,}\s[A-z\-]{3,}\s[A-z\-]{3,})|([A-Z]{2,}\sS\.A\.)|([A-Z\-]{3,}\s[&]\s[A-Z\-]{3,})", text)
furnizor1=re.findall("([A-Z]{3,}\sS.A.)",text)
adresafurnizor=re.findall("(Oras:.*?)Cui|SRL (.*?) Capital social|S.A. (.*?) FACTURA", text)
adresa=re.findall("Adresa: (.*?)suma de|([A-Z]+\.[A-Z]+ NR.[0-9]{2,4}[A-Z])|Str.(.*?)|Adresa\:?\s(.*?ap.\s[0-9]{1,})|Adresa: (.*?)suma de|([A-Z]+\.[A-Z]+ NR.[0-9]{2,4}[A-Z])", text)

produse=re.findall("Produse si servicii facturate (.*?) Suma facturata \(fara TVA\)|Denumire\/Produs\/Servicii (.*?)\s\d+\.\d{2}\s|[0-9]{1,}\,[0-9]{2}\s[0-9]{1,}\,[0-9]{2}(.*?)[0-9]{1,}\,[0-9]{2}\s[0-9]{1,}\,[0-9]{2}|[0-9]{1,}\,?[0-9]{0,}(.*?)[0-9]{1,}\,[0-9]{2}|[0-9]{1,}\s(.*?)[0-9]{1,}", text)

codclient=re.findall("COD CLIENT\:? ([0-9]{7,})|Cod abonat\:? ([0-9]{10})|Cod client\:? ([0-9]{8})|Cod client\:? ([0-9]{7,})\s", text)
nrfacturii=re.findall("Nr. Facturii\:? ([0-9]{8})|Nr. factură\:? ([0-9]{10,})|Numar factura\:? ([A-Z0-9]{6} [0-9]{6})|Nr. ([0-9]{8})|\s([0-9]{11})\s|Număr factură\:? ([0-9]{6,})|\s([A-Z]{3,}[0-9]{8,})|nr.\s([0-9]{8,})", text)

punctdelucru=re.findall("PUNCT DE LUCRU: (.*?) CHITANTA", text)
rambursla=re.findall("ramburs la ([A-Z]+ [0-9]+)", text)
clientulexpeditor=re.findall("(clientul .*?) Tiparit",text)
amprimitdela=re.findall("Am primit de la +: (.*?) CIF|Am primit de la +: (.*?) Adresa", text)
CI=re.findall("[A-Z]{2}[0-9]{8}", text)

from prettytable import PrettyTable
camp=['CIF','furnizor','codclient','codfacturare','datafacturare','duedate','furnizor','nrfacturii','numepersoana','perioadafacturare',
      'totalplata', 'seria',
      'adresadestinatar','adresafurnizor', 'punctdelucru', 'rambursla', 'clientulexpeditor', 'amprimitdela']
valoare=[CIF,furnizor,codclient,codfacturare,datafacturare,duedate,furnizor,nrfacturii,numepersoana,perioadafacturare,
      totalplata, seria,
      adresadestinatar,adresafurnizor, punctdelucru, rambursla, clientulexpeditor, amprimitdela]
table=PrettyTable(['camp','valoare'])
for x in range(0,len(camp)):
    table.add_row([camp[x],valoare[x]])
print(table)

#SPACY NLP
import spacy
nlp = spacy.load('ro_core_news_lg') #sm, lg
doc=nlp(text)
doc=nlp(numepersoana)
#ELIMINARE TOKENURI CARE NU SUNT DIN DEXONLINE
from lxml import html
import requests

def DefinitieCuvant(Cuvant, NumarDefinitii = 0,  TipDictionar = 0, encoding="utf-8"):
    WordPage = "https://dexonline.ro/definitie/" + str(Cuvant) + "/expandat"
    Tree = html.fromstring(requests.get(WordPage).content)
    Words = Tree.xpath('/html/body/div[1]/main/div/div/div[1]/div[2]/p/span[1]/text()')
    return(Words)
lemma=[]
tokens=[]
for token in doc:
        print(token.text, token.lemma_, token.pos_, token.is_stop)
        lemma.append(token.lemma_)
        tokens.append(token.text)
lemma=list(filter(lambda a: a != " ", lemma))
tokens=list(filter(lambda a: a != " ", tokens))
for i in tokens:
        if DefinitieCuvant(i)==[]:
         tokens.remove(i)
textcorectatcudexonline=' '.join(tokens)

#NER PE CATEGORII
def show_entsproduct(doc):
    if doc.ents:
            for ent in doc.ents:
                if(ent.label_=="PRODUCT"):
                    print(ent.text+' - '+ent.label_+ ' - '+str(spacy.explain(ent.label_)))
    else: print('No named entities found.')
print("Produsele oferite sunt: ")
show_entsproduct(doc)
def show_entsmoney(doc):
    if doc.ents:
            for ent in doc.ents:
                if(ent.label_=="MONEY"):
                    print(ent.text+' - '+ent.label_+ ' - '+str(spacy.explain(ent.label_)))
    else: print('No named entities found.')
print("Cantitatile de bani sunt: ")
show_entsmoney(doc)
def show_entsorganization(doc):
    if doc.ents:
            for ent in doc.ents:
                if(ent.label_=="ORGANIZATION"):
                    print(ent.text+' - '+ent.label_+ ' - '+str(spacy.explain(ent.label_)))
    else: print('No named entities found.')
show_entsorganization(doc)
def show_entsperson(doc):
    if doc.ents:
            for ent in doc.ents:
                if(ent.label_=="PERSON"):
                    print(ent.text+' - '+ent.label_+ ' - '+str(spacy.explain(ent.label_)))
    else: print('No named entities found.')
show_entsperson(doc)
def show_entsnumeric(doc):
    if doc.ents:
            for ent in doc.ents:
                if(ent.label_=="NUMERIC_VALUE"):
                    print(ent.text+' - '+ent.label_+ ' - '+str(spacy.explain(ent.label_)))
    else: print('No named entities found.')
show_entsnumeric(doc)
def show_entswork(doc):
    if doc.ents:
            for ent in doc.ents:
                if(ent.label_=="WORK_OF_ART"):
                    print(ent.text+' - '+ent.label_+ ' - '+str(spacy.explain(ent.label_)))
    else: print('No named entities found.')
show_entswork(doc)
def show_entsgpe(doc):
    if doc.ents:
            for ent in doc.ents:
                if(ent.label_=="GPE"):
                    print(ent.text+' - '+ent.label_+ ' - '+str(spacy.explain(ent.label_)))
    else: print('No named entities found.')
show_entsgpe(doc)
def show_entsfacility(doc):
    if doc.ents:
            for ent in doc.ents:
                if(ent.label_=="FACILITY"):
                    print(ent.text+' - '+ent.label_+ ' - '+str(spacy.explain(ent.label_)))
    else: print('No named entities found.')
show_entsfacility(doc)
def show_entsordinal(doc):
    if doc.ents:
            for ent in doc.ents:
                if(ent.label_=="ORDINAL"):
                    print(ent.text+' - '+ent.label_+ ' - '+str(spacy.explain(ent.label_)))
    else: print('No named entities found.')
show_entsordinal(doc)
def show_entsloc(doc):
    if doc.ents:
            for ent in doc.ents:
                if(ent.label_=="LOC"):
                    print(ent.text+' - '+ent.label_+ ' - '+str(spacy.explain(ent.label_)))
    else: print('No named entities found.')
show_entsloc(doc)
def show_entsquantity(doc):
    if doc.ents:
            for ent in doc.ents:
                if(ent.label_=="QUANTITY"):
                    print(ent.text+' - '+ent.label_+ ' - '+str(spacy.explain(ent.label_)))
    else: print('No named entities found.')
show_entsquantity(doc)
def show_entsdatetime(doc):
    if doc.ents:
            for ent in doc.ents:
                if(ent.label_=="DATETIME"):
                    print(ent.text+' - '+ent.label_+ ' - '+str(spacy.explain(ent.label_)))
    else: print('No named entities found.')
show_entsdatetime(doc)
def show_entsall(doc):
    if doc.ents:
            for ent in doc.ents:
                    print(ent.text+' - '+ent.label_+ ' - '+str(spacy.explain(ent.label_)))
    else: print('No named entities found.')
show_entsall(doc)

#EXPORT TABLE TO CSV
data = table.get_string()
import csv
result = [tuple(filter(None, map(str.strip, splitline))) for line in data.splitlines() for splitline in [line.split("|")] if len(splitline) > 1]
with open('output.csv', 'w', newline='', encoding="utf-8") as outcsv:
    writer = csv.writer(outcsv)
    writer.writerows(result)
    
    #####

from nltk import ngrams
n = 2
bigrams = ngrams(text.split(), n)
def convertTuple(tup): 
    str =  ' '.join(tup) 
    return str

for grams in bigrams:
    show_entsproduct(nlp(convertTuple(grams)))
print(convertTuple())
