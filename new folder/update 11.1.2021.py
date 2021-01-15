# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import json
with open('D:/BusuiocI/Desktop/134_4.json', encoding='utf-8') as f:
  data = json.load(f)
text=data['fullTextAnnotation']['text'].replace('\n',' ')

#READ FROM PDF
from pdf2image import convert_from_path
images = convert_from_path("D:/BusuiocI/Documents/Bibliografie/Anul 2, Sem I/Statistical processing of textual data/Baza de date Analiza text/Corpus-master-Onofrei Mihaela/Corpus-master/Pdf/factura_clasica.pdf", 500,poppler_path=r'D:/BusuiocI/Downloads/poppler-0.68.0_x86/poppler-0.68.0/bin')
for i, image in enumerate(images):
    fname = 'image'+str(i)+'.png'
    image.save(fname, "PNG")

import cv2
import pytesseract
img=cv2.imread("D:/BusuiocI/Desktop/image0.png")
pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'
custom_config = r'--oem 3 --psm 12'
text=pytesseract.image_to_string(img, config=custom_config, lang="ron")
img2=cv2.imread("D:/BusuiocI/Desktop/image1.png")
pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'
custom_config = r'--oem 3 --psm 12'
text2=pytesseract.image_to_string(img2, config=custom_config, lang="ron")
text=text+text2
#text=text.replace('\n',' ')

#REGEX UNIVERSAL
import re
telephone=re.findall("Număr telefon/cont: (0\d{3}\d{3}\d{3}\s)| (0\d{3}\d{3}\d{3}\s)|(0\d{4} \d{2} \d{2} \d{2}\s)| (0\d{9})\s|Voce: ([0-9]{10})", text)
postalcodesender=re.findall("\s\d{6}\s|\s\d{6}\,", text)
CIF=re.findall("\s[A-Z][A-Z]\d{4,10}\s|\s[A-Z][A-Z]\d{6,10}\s|\sR\d{9}\s|\sR\d{9}|Cod de inregistrare fiscala: +([A-z0-9]{9})|CIF:\s([A-Z][A-Z]\d{4,10})", text)
CIF
seria=re.findall("Seria [A-Z]{4} nr. [0-9]{7}|SERIA [A-Z]{4} +NR. +[0-9]{11}\/[0-9]{4}\-[0-9]{2}-[0-9]{2}|Seria şi nr\.\:\s[A-Z0-9]{6}\-[A-Z]", text)
numepersoana=re.findall("([A-Z\-]{4,})\s+([A-Z\-]{5,})??\s?([A-Z\-]{5,})\s", text)
perioadafacturare=re.findall("[0-9]{2}\.[0-9]{2}\.[0-9]{4}\-[0-9]{2}\.[0-9]{2}\.[0-9]{4}|[0-9]{2}\.[0-9]{2}\.[0-9]{2}\s\-\s[0-9]{2}\.[0-9]{2}\.[0-9]{2}|[0-9]{2}\.[0-9]{2}\.[0-9]{2}\-[0-9]{2}\.[0-9]{2}\.[0-9]{2}|[0-9]{2}\.[0-9]{2}\.[0-9]{4}\s\-\s[0-9]{2}\.[0-9]{2}\.[0-9]{4}", text)
perioadafacturare
datafacturare=re.findall("\Data facturării\:\s([0-9]{2}\.[0-9]{2}\.[0-9]{4})\s|Data:\s([0-9]{4}\-[0-9]{2}\-[0-9]{2})\s|Data emiterii +([0-9]{2}\.[0-9]{2}\.[0-9]{4})|Data facturii: ([0-9]{2}\.[0-9]{2}\.[0-9]{4})|din:\s([0-9]{2}\.[0-9]{2}\.[0-9]{4})\s|Data facturii: ([0-9]{2}\/[0-9]{2}\/[0-9]{4})\s", text)
duedate=re.findall("Total de plată pană la\s([0-9]{2}\.[0-9]{2}\.[0-9]{4})|Scadent:\s([0-9]{4}\-[0-9]{2}\-[0-9]{2})\s|până la data de ([0-9]{2}\.[0-9]{2}\.[0-9]{4})|scadenta:\s([0-9]{2}\.[0-9]{2}\.[0-9]{4})\s|Data scadenţei: ([0-9]{2}\/[0-9]{2}\/[0-9]{4})", text)
totalplata=re.findall("(\-?\d+,\d{2})\s|\s(\-?\d+\.\d{2})\s|Vă rugăm să achitaţi suma de\s(\-?\d+,\d{2})\s|TOTAL DE PLATA .*? (\-?\d+.\d{2})\s|(\-?\d+\.\d{3},\d{2})\s", text)
totalplata2=[element for tupl in totalplata for element in tupl]
without_empty_strings = [string for string in totalplata2 if string != ""]
#j=[]
#for i in without_empty_strings:
#    j.append(float(i.replace(',','.')))
#totalplata=max(j)
IBAN=re.findall("Cod IBAN:\s([A-Z]{2}[0-9]{2}\s[a-zA-Z0-9]{4}\s[a-zA-Z0-9]{4}\s[a-zA-Z0-9]{4}\s[a-zA-Z0-9]{4}\s[a-zA-Z0-9]{4})\s|\s([A-Z0-9]{24})\s|\s([A-Z0-9]{11}\s[0-9]{13})", text)
IBAN
codfacturare=re.findall("\s([0-9]{14})\s", text)
furnizor=re.findall("[0-9]+ (.*? S.A.)|FURNIZOR: (.*? SRL)|(FIRMA .*?) Cumparator|(.*? SA)|(.*? SRL)|(.*? S.A.)", text)
adresafurnizor=re.findall("(Oras:.*?)Cui|SRL (.*?) Capital social|S.A. (.*?) FACTURA", text)
adresadestinatar=re.findall("Adresa: (.*?)suma de|([A-Z]+\.[A-Z]+ NR.[0-9]{2,4}[A-Z])", text)
produse=re.findall("Produse si servicii facturate (.*?) Suma facturata \(fara TVA\)|Denumire\/Produs\/Servicii (.*?)\s\d+\.\d{2}\s", text)
codclient=re.findall("COD CLIENT: ([0-9]{9})|Cod abonat: ([0-9]{10})|Cod client: ([0-9]{8})", text)
nrfacturii=re.findall("Nr. Facturii: ([0-9]{8})|Nr. factură: ([0-9]{13})|Numar factura. ([A-Z0-9]{6} [0-9]{6})|Nr. ([0-9]{8})", text)
punctdelucru=re.findall("PUNCT DE LUCRU: (.*?) CHITANTA", text)
rambursla=re.findall("ramburs la ([A-Z]+ [0-9]+)", text)
clientulexpeditor=re.findall("(clientul .*?) Tiparit",text)
amprimitdela=re.findall("Am primit de la +: (.*?) CIF|Am primit de la +: (.*?) Adresa", text)

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
nlp = spacy.load('ro_core_news_md') #sm, lg
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
    
