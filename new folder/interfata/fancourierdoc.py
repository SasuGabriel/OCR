# -*- coding: utf-8 -*-

import cv2
import os
import numpy as np
import pytesseract
import pandas as pd
from pytesseract import Output
from  PIL import  Image
import re
from unidecode import unidecode
from prettytable import PrettyTable
import csv
def test1(path):
      pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'
      img=cv2.imread(path)
      custom_config = r'--oem 3 --psm 12'
      text=pytesseract.image_to_string(img, config=custom_config, lang="ron")
      text=text.replace('\n',' ')
      text=text.replace('\n\n',' ')
      unidecode(text)

      #REGEX UNIVERSAL
      telephonecorect=re.findall("Telefon\:? (0\d{9}\s)| (0\d{9}\s)|(0\d{4} \d{2} \d{2} \d{2}\s)| (0\d{9}): ([0-9]{10})|(0\d{3} \d{3} \d{3})\s", text)
      telefon=re.findall('\s([0-9]{7})\s|\s([0-9]{4}\.[0-9]{3}\.[0-9]{3})\s|\s([0-9]{4}\s[0-9]{3}\s[0-9]{3})\s|\s([0-9]{10})|\s([0-9]{4}\s[0-9]{2}\s[0-9]{2})',text)
      postalcode=re.findall("\s(\d{6})\s|\s(\d{6})\,|([A-Z]{2,}\-[0-9]{6})", text)
      CIF=re.findall("\s[A-Z][A-Z]\d{4,10}\s|\s[A-Z][A-Z]\d{6,10}\s|\sR\d{9}\s|\sR\d{9}|Cod de inregistrare fiscala\:? +([A-z0-9]{9})|CIF\:?\s([A-Z][A-Z]\d{4,10})|CIF\:?\s([A-Z]{1,}[0-9]{8,})|CIF\:?\s([A-Z]{1,}[0-9]{2,}\s[0-9]{2,})|\(C\.I\.F\.\)\:\s([A-Z]{1,}[0-9]{7,})|C\.I\.F\.\s([A-Z]{1,}[0-9]{7,})", text)
      cartedeidentitate=re.findall("([A-Z]{2}[0-9]{6})\n", text)
      seria=re.findall("Seria [A-Z]{4} nr. [0-9]{7}|SERIA [A-Z]{4} +NR. +[0-9]{11}\/[0-9]{4}\-[0-9]{2}-[0-9]{2}|Seria şi nr\.\:\s[A-Z0-9]{6}\-[A-Z]", text)
      seria=re.findall("Seria [A-Z]{4} nr. [0-9]{7}|SERIA [A-Z]{4} +NR. +[0-9]{11}\/[0-9]{4}\-[0-9]{2}-[0-9]{2}|Seria şi nr\.\:\s[A-Z0-9]{6}\-[A-Z] |([A-Z]{1,}\-[0-9]{1,}\s)", text)
      seria=re.findall("Seria ([A-Z]{4} nr. [0-9]{7})|SERIA ([A-Z]{3,}\sNR\.\s[0-9]{11}\/[0-9]{4}\-[0-9]{2}\-[0-9]{2})|Seria şi nr\.\:?\s([A-Z0-9]{6}\-[A-Z])|([A-Z]{1,}\-[0-9]{1,})|\s([A-Z]{2}\s[A-Z]{2,} nr. [0-9]{7,})|([A-Z]{2,}[0-9]{2}\s\/\s[0-9]{8,})|Seria\:?\s([A-Z]{2,}\s[A-Z]{3,})|Seria\:?\s([A-Z]{2,})|SERIA\s([A-Z]{1,}[0-9]{2,})\s", text)
      seria2=re.findall("SERIA [A-Z]{3,}\sNR\.\s[0-9]{11}\/[0-9]{4}\-[0-9]{2}\-[0-9]{2}",text)
      numepersoana=re.findall("([A-Z\-]{4,})\s+([A-Z\-]{5,})?\s?([A-Z\-]{5,})", text)
      perioadafacturare=re.findall("[0-9]{2}\.[0-9]{2}\.[0-9]{4}\-[0-9]{2}\.[0-9]{2}\.[0-9]{4}|[0-9]{2}\.[0-9]{2}\.[0-9]{2}\s\-\s[0-9]{2}\.[0-9]{2}\.[0-9]{2}|[0-9]{2}\.[0-9]{2}\.[0-9]{2}\-[0-9]{2}\.[0-9]{2}\.[0-9]{2}|[0-9]{2}\.[0-9]{2}\.[0-9]{4}\s\-\s[0-9]{2}\.[0-9]{2}\.[0-9]{4}", text)
      datafacturare=re.findall("\Data facturării\:?\s([0-9]{2}\.[0-9]{2}\.[0-9]{4})\s|Data\:?\s([0-9]{4}\-[0-9]{2}\-[0-9]{2})\s|Data emiterii\:? +([0-9]{2}\.[0-9]{2}\.[0-9]{4})|Data facturii\:? ([0-9]{2}\.[0-9]{2}\.[0-9]{4})|din\:?\s([0-9]{2}\.[0-9]{2}\.[0-9]{4})\s|Data facturii\:? ([0-9]{2}\/[0-9]{2}\/[0-9]{4})\s|din data de\:?\s([0-9]{2}\.[0-9]{2}\.[0-9]{4})|Data\:?\s([0-9]{2}\.[0-9]{2}\.[0-9]{4})|Data emiterii\:?\s([0-9]{2}\.[0-9]{2}\.[0-9]{4})", text)
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
      furnizor=re.findall("[0-9]+ (.*? S.A.)|FURNIZOR\:? (.*? SRL)|(FIRMA .*?) Cumparator|(.*? SA)|(.*? SRL)|(.*? S.A.)", text)
      adresafurnizor=re.findall("(Oras:.*?)Cui|SRL (.*?) Capital social|S.A. (.*?) FACTURA", text)
      adresa=re.findall("Adresa: (.*?)suma de|([A-Z]+\.[A-Z]+ NR.[0-9]{2,4}[A-Z])|Str.(.*?)|Adresa\:?\s(.*?ap.\s[0-9]{1,})|Adresa: (.*?)suma de|([A-Z]+\.[A-Z]+ NR.[0-9]{2,4}[A-Z])", text)

      produse=re.findall("Produse si servicii facturate (.*?) Suma facturata \(fara TVA\)|Denumire\/Produs\/Servicii (.*?)\s\d+\.\d{2}\s", text)
      codclient=re.findall("COD CLIENT\:? ([0-9]{7,})|Cod abonat\:? ([0-9]{10})|Cod client\:? ([0-9]{8})|Cod client\:? ([0-9]{7,})\s", text)
      nrfacturii=re.findall("Nr. Facturii\:? ([0-9]{8})|Nr. factură\:? ([0-9]{10,})|Numar factura\:? ([A-Z0-9]{6} [0-9]{6})|Nr. ([0-9]{8})|\s([0-9]{11})\s|Număr factură\:? ([0-9]{6,})|\s([A-Z]{3,}[0-9]{8,})|nr.\s([0-9]{8,})", text)

      punctdelucru=re.findall("PUNCT DE LUCRU: (.*?) CHITANTA", text)
      rambursla=re.findall("ramburs la ([A-Z]+ [0-9]+)", text)
      clientulexpeditor=re.findall("(clientul .*?) Tiparit",text)
      amprimitdela=re.findall("Am primit de la +: (.*?) CIF|Am primit de la +: (.*?) Adresa", text)
      CI=re.findall("[A-Z]{2}[0-9]{8}", text)


      camp=['CIF','furnizor','codclient','codfacturare','datafacturare','furnizor','nrfacturii','numepersoana','perioadafacturare',
            'totalplata', 'seria', 'adresafurnizor', 'punctdelucru', 'rambursla', 'clientulexpeditor', 'amprimitdela']
      valoare=[CIF,furnizor,codclient,codfacturare,datafacturare,furnizor,nrfacturii,numepersoana,perioadafacturare,
      totalplata, seria, adresafurnizor, punctdelucru, rambursla, clientulexpeditor, amprimitdela]
      table=PrettyTable(['camp','valoare'])
      for x in range(0,len(camp)):
            table.add_row([camp[x],valoare[x]])
      return table

#EXPORT TABLE TO CSV
def test2(table):
      data = table.get_string()
      result = [tuple(filter(None, map(str.strip, splitline))) for line in data.splitlines() for splitline in [line.split("|")] if len(splitline) > 1]
      with open('C:/Users/pc/Desktop/PrelucrareaStatisticaaDatelorText/proiect/try/output.csv', 'w', newline='', encoding="utf-8") as outcsv:
            writer = csv.writer(outcsv)
            writer.writerows(result)

