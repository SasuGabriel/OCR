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
img=cv2.imread("D:/BusuiocI/Documents/Bibliografie/Anul 2, Sem I/Statistical processing of textual data/Baza de date Analiza text/Chitante Bonuri Andreea/IMG20201112121821.jpg")

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

#preprocesare imagine

def gray(img):
    img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    return img

def blur(img):
    img_blur=cv2.GaussianBlur(img,(1,1),0)
    cv2.imwrite(r"./preprocess/img_blur.png",img)
    return img_blur

def threshhold(img):
    img=cv2.threshold(img,100,255,cv2.THRESH_OTSU|cv2.THRESH_BINARY)[1]
    cv2.imwrite(r"./preprocess/img_threshold.png",img)
    return img
norm_img = np.zeros((img.shape[0], img.shape[1]))
img = cv2.normalize(img, norm_img, 0, 255, cv2.NORM_MINMAX)
img = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)[1]
img = cv2.GaussianBlur(img, (1, 1), 0)

text= pytesseract.image_to_string(img,config=custom_config)
text=text.replace('\n\n',' ')

#REGEX UNIVERSAL
import re
#telephonecorect=re.findall("Telefon\:? (0\d{9}\,?\s)|\s(0\d{9}\,?\s)|(0\d{3} \d{2} \d{2} \d{2}\,?\s)| (0\d{9}): ([0-9]{10})|(0\d{3} \d{3} \d{3})\,?\s|\+[0-9]{2}\s[0-9]{2}\s[0-9]{3}\s[0-9]{2}\s[0-9]{2}", text)
telefon=re.findall('\s([0-9]{4}\.[0-9]{3}\.[0-9]{3})\,?\s|\s([0-9]{4}\s[0-9]{3}\s[0-9]{3})\,?\s|([0-9]{4}\.[0-9]{3}\.[0-9]{3})\,?\s?|\s(\d{4}\s\d{2}\s\d{2}\s\d{2})|\+4[0-9]{4}\s?[0-9]{3}\s?[0-9]{3}|Telefon\:? (0\d{9}\,?\s)|\s(0\d{9}\,?\s)',text)
elements=[element for tupl in telefon for element in tupl]
telefon = [string for string in elements if string != ""]

postalcode=re.findall("\s(\d{6})\s|\s(\d{6})\s|([A-Z]{2,}\-[0-9]{6})\s", text)
elements=[element for tupl in postalcode for element in tupl]
postalcode = [string for string in elements if string != ""]

CIF=re.findall("\s[A-Z][A-Z]\d{4,10}\s|\s[A-Z][A-Z]\d{6,10}\s|\sR\d{9}\s|\sR\d{9}|Cod de inregistrare fiscala\:? +([A-z0-9]{9})|CIF\:?\s([A-Z][A-Z]\d{4,10})|CIF\:?\s([A-Z]{1,}[0-9]{8,})|CIF\:?\s([A-Z]{1,}[0-9]{2,}\s[0-9]{2,})|\(C\.I\.F\.\)\:\s([A-Z]{1,}[0-9]{7,})|C\.I\.F\.\s([A-Z]{1,}[0-9]{7,})", text)
elements=[element for tupl in CIF for element in tupl]
CIF = [string for string in elements if string != ""]

cartedeidentitate=re.findall("\s([A-Z]{2}[0-9]{6})\s", text)
#seria=re.findall("Seria [A-Z]{4} nr. [0-9]{7}|SERIA [A-Z]{4} +NR. +[0-9]{11}\/[0-9]{4}\-[0-9]{2}-[0-9]{2}|Seria şi nr\.\:\s[A-Z0-9]{6}\-[A-Z]", text)
#seria=re.findall("Seria [A-Z]{4} nr. [0-9]{7}|SERIA [A-Z]{4} +NR. +[0-9]{11}\/[0-9]{4}\-[0-9]{2}-[0-9]{2}|Seria şi nr\.\:\s[A-Z0-9]{6}\-[A-Z] |([A-Z]{1,}\-[0-9]{1,}\s)", text)
seriabuna=re.findall("Seria ([A-Z]{4} nr. [0-9]{7})|(Seria\:\s[A-Z\s]+\sNr\.\sfactură\:\s[0-9]{7,})\s|SERIA ([A-Z]{3,}\sNR\.\s[0-9]{11}\/[0-9]{4}\-[0-9]{2}\-[0-9]{2})|Seria şi nr\.\:?\s([A-Z0-9]{6}\-[A-Z])|([A-Z]{1,}\-[0-9]{1,})|\s([A-Z]{2}\s[A-Z]{2,} nr. [0-9]{7,})|([A-Z]{2,}[0-9]{2}\s\/\s[0-9]{8,})|Seria\:?\s([A-Z]{2,}\s[A-Z]{3,})|Seria\:?\s([A-Z]{2,})|SERIA\s([A-Z]{1,}[0-9]{2,})\s", text)
elements=[element for tupl in seriabuna for element in tupl]
seriabuna = [string for string in elements if string != ""]

numepersoana=re.findall("([A-Z\-]{4,}\s+[A-Z\-]{0,}\s?[A-Z\-]{5,})\s|([A-Z]{1}[a-z]{2,}\s[A-Z][a-z]{2,})\s", text)
elements=[element for tupl in numepersoana for element in tupl]
numepersoana = [string for string in elements if string != ""]
numepersoana

perioadafacturare=re.findall("[0-9]{2}\.[0-9]{2}\.[0-9]{4}\-[0-9]{2}\.[0-9]{2}\.[0-9]{4}|[0-9]{2}\.[0-9]{2}\.[0-9]{2}\s\-\s[0-9]{2}\.[0-9]{2}\.[0-9]{2}|[0-9]{2}\.[0-9]{2}\.[0-9]{2}\-[0-9]{2}\.[0-9]{2}\.[0-9]{2}|[0-9]{2}\.[0-9]{2}\.[0-9]{4}\s\-\s[0-9]{2}\.[0-9]{2}\.[0-9]{4}", text)
perioadafacturare

datafacturare=re.findall("\Data facturării\:?\s([0-9]{2}\.[0-9]{2}\.[0-9]{4})\s|Data\:?\s([0-9]{4}\-[0-9]{2}\-[0-9]{2})\s|Data emiterii\:? +([0-9]{2}\.[0-9]{2}\.[0-9]{4})|Data facturii\:? ([0-9]{2}\.[0-9]{2}\.[0-9]{4})|din\:?\s([0-9]{2}\.[0-9]{2}\.[0-9]{4})\s|Data facturii\:? ([0-9]{2}\/[0-9]{2}\/[0-9]{4})\s|din data de\:?\s([0-9]{2}\.[0-9]{2}\.[0-9]{4})|Data\:?\s([0-9]{2}\.[0-9]{2}\.[0-9]{4})|Data emiterii\:?\s([0-9]{2}\.[0-9]{2}\.[0-9]{4})|Data avizului\:?\s([0-9]{2}\/[0-9]{2}\/[0-9]{4})", text)
elements=[element for tupl in datafacturare for element in tupl]
datafacturare = [string for string in elements if string != ""]
datafacturare

datascadenta=re.findall("Total de plată pană la\:?\s([0-9]{2}\.[0-9]{2}\.[0-9]{4})|Scadent\:?\s([0-9]{4}\-[0-9]{2}\-[0-9]{2})\s|până la data de\:? ([0-9]{2}\.[0-9]{2}\.[0-9]{4})|scadenta\:?\s([0-9]{2}\.[0-9]{2}\.[0-9]{4})\s|Data scadenţei\:? ([0-9]{2}\/[0-9]{2}\/[0-9]{4})|Scadenta\:?\s([0-9]{2}\.[0-9]{2}\.[0-9]{4})\s|Data scadentă\:?\s([0-9]{2}\.[0-9]{2}\.[0-9]{4})|Ultima zi de plată\:?\s([0-9]{2}\.[0-9]{2}\.[0-9]{4})|Ultima zi de plata\:?\s([0-9]{2}\.[0-9]{2}\.[0-9]{4})|Data scadentei\:?\s([0-9]{2}\.[0-9]{2}\.[0-9]{4})", text)
elements=[element for tupl in datascadenta for element in tupl]
datascadenta = [string for string in elements if string != ""]
datascadenta

sumedebani=re.findall("(\-?\d+,\d{2})\s|\s(\-?\d+\.\d{2})\s|Vă rugăm să achitaţi suma de\:?\s(\-?\d+,\d{2})\s|TOTAL DE PLATA .*? (\-?\d+.\d{2})\s|(\-?\d+\.\d{3},\d{2})\s|(\-?\d+?\.\d{3}\.\d{3}\,\d{2})|\s(\-?[0-9]{1,}\.[0-9]{2})\s", text)
elements=[element for tupl in sumedebani for element in tupl]
sumedebani = [string for string in elements if string != ""]
sumedebani
j=[]
for i in sumedebani:
    i=i.replace('.','')
    i=i.replace(',','.')
    j.append(float(i))
totalplata=max(j)

IBAN=re.findall("([A-Z]{2}[0-9]{2}\s[a-zA-Z0-9]{4}\s[a-zA-Z0-9]{4}\s[a-zA-Z0-9]{4}\s[a-zA-Z0-9]{4}\s[a-zA-Z0-9]{4})\s|\s([A-Z0-9]{24})\s|\s([A-Z0-9]{11}\s[0-9]{13})|([A-Z]{2}[0-9]{2}[a-zA-Z0-9]{9}\s[a-zA-Z0-9]{13})", text)
elements=[element for tupl in IBAN for element in tupl]
IBAN = [string for string in elements if string != ""]
IBAN

codfacturare=re.findall("\s([0-9]{14})\s",text)

furnizor=re.findall("(.{,15}\sS\.A\.)|FURNIZOR\:? (.*? SRL)|(FIRMA .*?) Cumparator|(.{,15}\sSA)|(.{,15}\sSRL)|Furnizor Client(.*? SRL)|Furnizor\:? (.*? SA)|Furnizor\:? (.*? SRL)|Furnizor\:?\s(.*? S\.A\.)|Furnizor\:?\s(.*? S\.R\.L\.)|([a-z\-]{3,}\-[a-z\-]{3,}\-[a-z\-]{3,})|([A-Z]{1}\.[A-Z]{2})\s|([A-Z\-]{1,}\.[A-Z\-]{2,}\s[A-z\-]{3,}\s[A-z\-]{3,})|([A-Z]{2,}\sS\.A\.)|([A-Z\-]{3,}\s[&]\s[A-Z\-]{3,})|(.{,15}\sPFA)", text)
furnizor2=re.findall("(.{,20}\sS\.A\.)\s|(.{,20}\sSA)\s|(.{,20}\sSRL)\s|(.{,20}\sPFA)\s|(.{,20}\sS\.R\.L\.)\s", text)
elements=[element for tupl in furnizor2 for element in tupl]
furnizor2 = [string for string in elements if string != ""]
furnizor2

adresafurnizor=re.findall("(Oras:.*?)Cui|SRL (.*?) Capital social|S.A. (.*?) FACTURA", text)
elements=[element for tupl in adresafurnizor for element in tupl]
adresafurnizor = [string for string in elements if string != ""]
adresafurnizor

adresa=re.findall("(Str\..+Ap\.\s[0-9]{1,}\s)|Adresa: (.*?)suma de|([A-Z]+\.[A-Z]+ NR.[0-9]{2,4}[A-Z])|Str.(.*?)|Adresa\:?\s(.*?ap.\s[0-9]{1,})|Adresa: (.*?)suma de|([A-Z]+\.[A-Z]+ NR.[0-9]{2,4}[A-Z])", text)
elements=[element for tupl in adresa for element in tupl]
adresa = [string for string in elements if string != ""]
adresa

produse=re.findall("Produse si servicii facturate (.*?) Suma facturata \(fara TVA\)|Denumire\/Produs\/Servicii (.*?)\s\d+\.\d{2}\s|[0-9]{1,}\,[0-9]{2}\s[0-9]{1,}\,[0-9]{2}(.*?)[0-9]{1,}\,[0-9]{2}\s[0-9]{1,}\,[0-9]{2}|[0-9]{1,}\,?[0-9]{0,}(.*?)[0-9]{1,}\,[0-9]{2}|[0-9]{1,}\s(.*?)[0-9]{1,}", text)
elements=[element for tupl in produse for element in tupl]
produse = [string for string in elements if string != ""]
produse

codclient=re.findall("COD CLIENT\:? ([0-9]{7,})|Cod abonat\:? ([0-9]{10})|Cod client\:? ([0-9]{8})|Cod client\:? ([0-9]{7,})\s", text)
elements=[element for tupl in codclient for element in tupl]
codclient = [string for string in elements if string != ""]
codclient

nrfacturii=re.findall("Nr. Facturii\:? ([0-9]{8})|Nr. factură\:? ([0-9]{10,})|Numar factura\:? ([A-Z0-9]{6} [0-9]{6})|Nr. ([0-9]{8})|\s([0-9]{11})\s|Număr factură\:? ([0-9]{6,})|\s([A-Z]{3,}[0-9]{8,})|nr.\s([0-9]{8,})", text)
elements=[element for tupl in nrfacturii for element in tupl]
nrfacturii = [string for string in elements if string != ""]
nrfacturii

punctdelucru=re.findall("PUNCT DE LUCRU: (.*?) CHITANTA", text)
rambursla=re.findall("ramburs la ([A-Z]+ [0-9]+)", text)
clientulexpeditor=re.findall("(clientul .*?) Tiparit",text)

amprimitdela=re.findall("Am primit de la +: (.*?) CIF|Am primit de la +: (.*?) Adresa", text)
elements=[element for tupl in amprimitdela for element in tupl]
amprimitdela = [string for string in elements if string != ""]
amprimitdela

CI=re.findall("([A-Z]{2}[0-9]{8})\s", text)


#SPACY NLP
import spacy
nlp = spacy.load('ro_core_news_lg') #sm, lg
doc=nlp(text)

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
produse=[]
def show_entsproduct(doc):
    if doc.ents:
            for ent in doc.ents:
                if(ent.label_=="PRODUCT"):
                    print(ent.text+' - '+ent.label_+ ' - '+str(spacy.explain(ent.label_)))
                    produse.append(ent.text+' - '+ent.label_+ ' - '+str(spacy.explain(ent.label_)))
    else: print('No named entities found.')
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

#PRETTYTABLE
from prettytable import PrettyTable
camp=['telefon','postalcode','CIF','cartedeidentitate','seria','numepersoana','perioadafacturare',
         'datafacturare', 'datascadenta', 'sumedebani','IBAN', 'codfacturare', 'furnizor', 'adresafurnizor', 'adresa', 'produse',
         'codclient', 'nrfacturii', 'punctdelucru', 'rambursla', 'clientulexpeditor', 'amprimitdela', 'CI']
valoare=[telefon,postalcode,CIF,cartedeidentitate,seriabuna,numepersoana,perioadafacturare,
         datafacturare, datascadenta, sumedebani,IBAN, codfacturare, furnizor, adresafurnizor, adresa, produse,
         codclient, nrfacturii, punctdelucru, rambursla, clientulexpeditor, amprimitdela, CI]
table=PrettyTable(['camp','valoare'])
for x in range(0,len(camp)):
    table.add_row([camp[x],valoare[x]])
print(table)

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
