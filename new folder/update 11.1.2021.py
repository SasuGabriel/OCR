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
PDF_file = 'D:/BusuiocI/Documents/Bibliografie/Anul 2, Sem I/Statistical processing of textual data/Baza de date Analiza text/Corpus-master-Onofrei Mihaela/Corpus-master/Pdf/aviz de insotire a marfii.pdf'
import fitz
import cv2
import pytesseract
doc=fitz.open(PDF_file)
page=doc.loadPage(0)
pix=page.getPixmap()
output="outfile.PNG"
pix.writePNG(output)
img=cv2.imread("D:/BusuiocI/Documents/Bibliografie/Anul 2, Sem I/Statistical processing of textual data/Baza de date Analiza text/Facturi Analiza text-Ilinca/eon/20201023_130755.jpg")
pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'
custom_config = r'--oem 3 --psm 12'
text=pytesseract.image_to_string(img, config=custom_config, lang="ron")
text=text.replace('\n',' ')

#REGEX UNIVERSAL
import re
telephone=re.findall("Număr telefon/cont: (0\d{3}\d{3}\d{3}\s)| (0\d{3}\d{3}\d{3}\s)|(0\d{4} \d{2} \d{2} \d{2}\s)| (0\d{9})\s", text)
postalcodesender=re.findall("\s\d{6}\s", text)[0].strip()
CIF=re.findall("\s[A-Z][A-Z]\d{6,10}\s|\s[A-Z][A-Z]\d{6,10}\s|\sR\d{9}\s", text)[0].strip()
CIF
seria=re.findall("Seria [A-Z]{4} nr. [0-9]{7}", text)
seria=seria[0]
numepersoana=re.findall("([A-Z\-]{4,})\s+([A-Z\-]{5,})??\s?([A-Z\-]{5,})\s", text)
perioadafacturare=re.findall("[0-9]{2}\.[0-9]{2}\.[0-9]{4}\-[0-9]{2}\.[0-9]{2}\.[0-9]{4}|[0-9]{2}\.[0-9]{2}\.[0-9]{2}\s\-\s[0-9]{2}\.[0-9]{2}\.[0-9]{2}", text)[0].strip()
perioadafacturare
datafacturare=re.findall("\Data facturării\:\s([0-9]{2}\.[0-9]{2}\.[0-9]{4})\s|Data:\s([0-9]{4}\-[0-9]{2}\-[0-9]{2})\s|Data emiterii +([0-9]{2}\.[0-9]{2}\.[0-9]{4})", text)[0]
duedate=re.findall("Total de plată pană la\s([0-9]{2}\.[0-9]{2}\.[0-9]{4})|Scadent:\s([0-9]{4}\-[0-9]{2}\-[0-9]{2})\s|până la data de ([0-9]{2}\.[0-9]{2}\.[0-9]{4})", text)[0]
totalplata=re.findall("(\-?\d+,\d{2})|\s(\d+\.\d{2})\s|Vă rugăm să achitaţi suma de\s(\-?\d+,\d{2})", text)
totalplata2=[element for tupl in totalplata for element in tupl]
without_empty_strings = [string for string in totalplata2 if string != ""]
j=[]
for i in without_empty_strings:
    j.append(float(i.replace(',','.')))
totalplata=max(j) #nu merge extraordinar, adica ia valoarea maxima care nu e tot timpul suma de platit
IBAN=re.findall("Cod IBAN:\s([A-Z]{2}[0-9]{2}\s[a-zA-Z0-9]{4}\s[a-zA-Z0-9]{4}\s[a-zA-Z0-9]{4}\s[a-zA-Z0-9]{4}\s[a-zA-Z0-9]{4})\s|\s([A-Z0-9]{24})\s", text)
IBAN
codfacturare=re.findall("\s([0-9]{14})\s", text)[0]
furnizor=re.findall("[0-9]+ (.*? S.A.)|FURNIZOR: (.*? SRL)|(FIRMA .*?) Cumparator|(.*? SA)", text)
adresafurnizor=re.findall("(Oras:.*?)Cui", text)
produse=re.findall("Produse si servicii facturate (.*?) Suma facturata \(fara TVA\)|Denumire\/Produs\/Servicii (.*?)\s\d+\.\d{2}\s", text)
codclient=re.findall("COD CLIENT: ([0-9]{9})|Cod abonat: ([0-9]{10})", text)[0]
nrfacturii=re.findall("Nr. Facturii: ([0-9]{8})|Nr. factură: ([0-9]{13})", text)[0]

#SPACY NLP
import spacy
nlp = spacy.load('ro_core_news_lg')
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

#PRETTYTABLE
from prettytable import PrettyTable
camp=['CIF','numepersoana','perioada facturare','data facturare', 'total de plata pana la: ','IBAN',
      'cod facturare','telefon/cont','total plata', 'seria', 'adresa furnizor',
      'adresa destinatar']
valoare=[CIF,numepersoana,perioadafacturare,datafacturare,duedate,IBAN,
      codfacturare,telephone,totalplata, seria,adresafurnizor,
      adresadestinatar]
table=PrettyTable(['camp','valoare'])
for x in range(0,len(camp)):
    table.add_row([camp[x],valoare[x]])
print(table)


#EXPORT TABLE TO CSV
data = table.get_string()
import csv
result = [tuple(filter(None, map(str.strip, splitline))) for line in data.splitlines() for splitline in [line.split("|")] if len(splitline) > 1]
with open('output.csv', 'w', newline='') as outcsv:
    writer = csv.writer(outcsv)
    writer.writerows(result)
    