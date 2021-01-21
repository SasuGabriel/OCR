import cv2
import os
import numpy as np
import pytesseract
import pandas as pd
from pytesseract import Output
from  PIL import  Image
import re
from prettytable import PrettyTable
import csv
from pdf2image import convert_from_path
import spacy



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

def test1(path):
    produse=[]
    def show_entsproduct(doc):
        if doc.ents:
            for ent in doc.ents:
                if(ent.label_=="PRODUCT"):
                    #print(ent.text+' - '+ent.label_+ ' - '+str(spacy.explain(ent.label_)))
                    produse.append(ent.text+' - '+ent.label_+ ' - '+str(spacy.explain(ent.label_)))
                #else: print('No named entities found.')
        return produse
    pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'
    if path.endswith('.pdf'):
            pages = convert_from_path(path, poppler_path=r"D:/BusuiocI/Downloads/poppler-0.68.0_x86/poppler-0.68.0/bin") 
            #Saving pdf page in jpeg format
            for page in pages:
                  path="D:/BusuiocI/Desktop/output.jpg"
                  page.save(path, "JPEG")
                  img=cv2.imread(path)
                  img=gray(img)
                  img=blur(img)
                  img=threshhold(img)
                  norm_img = np.zeros((img.shape[0], img.shape[1]))
                  img = cv2.normalize(img, norm_img, 0, 255, cv2.NORM_MINMAX)
                  img = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)[1]
                  img = cv2.GaussianBlur(img, (1, 1), 0)
                  custom_config = r'--oem 3 --psm 12'
                  text=pytesseract.image_to_string(img, config=custom_config, lang="ron")
                  text=text.replace('\n\n',' ')
                  text=text.replace('\n',' ')
                  nlp = spacy.load('ro_core_news_lg') #sm, lg
                  doc=nlp(text)
                  
    else:
          img=cv2.imread(path)
          img=gray(img)
          img=blur(img)
          img=threshhold(img)
          norm_img = np.zeros((img.shape[0], img.shape[1]))
          img = cv2.normalize(img, norm_img, 0, 255, cv2.NORM_MINMAX)
          img = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)[1]
          img = cv2.GaussianBlur(img, (1, 1), 0)
          custom_config = r'--oem 3 --psm 12'
          text=pytesseract.image_to_string(img, config=custom_config, lang="ron")
          text=text.replace('\n\n',' ')
          text=text.replace('\n',' ')
          nlp = spacy.load('ro_core_news_lg') #sm, lg
          doc=nlp(text)
#REGEX UNIVERSAL
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
    perioadafacturare=re.findall("[0-9]{2}\.[0-9]{2}\.[0-9]{4}\-[0-9]{2}\.[0-9]{2}\.[0-9]{4}|[0-9]{2}\.[0-9]{2}\.[0-9]{2}\s\-\s[0-9]{2}\.[0-9]{2}\.[0-9]{2}|[0-9]{2}\.[0-9]{2}\.[0-9]{2}\-[0-9]{2}\.[0-9]{2}\.[0-9]{2}|[0-9]{2}\.[0-9]{2}\.[0-9]{4}\s\-\s[0-9]{2}\.[0-9]{2}\.[0-9]{4}", text)
    datafacturare=re.findall("\Data facturării\:?\s([0-9]{2}\.[0-9]{2}\.[0-9]{4})\s|Data\:?\s([0-9]{4}\-[0-9]{2}\-[0-9]{2})\s|Data emiterii\:? +([0-9]{2}\.[0-9]{2}\.[0-9]{4})|Data facturii\:? ([0-9]{2}\.[0-9]{2}\.[0-9]{4})|din\:?\s([0-9]{2}\.[0-9]{2}\.[0-9]{4})\s|Data facturii\:? ([0-9]{2}\/[0-9]{2}\/[0-9]{4})\s|din data de\:?\s([0-9]{2}\.[0-9]{2}\.[0-9]{4})|Data\:?\s([0-9]{2}\.[0-9]{2}\.[0-9]{4})|Data emiterii\:?\s([0-9]{2}\.[0-9]{2}\.[0-9]{4})|Data avizului\:?\s([0-9]{2}\/[0-9]{2}\/[0-9]{4})|([0-9]{2}\-[0-9]{2}\-[0-9]{4})\s", text)
    elements=[element for tupl in datafacturare for element in tupl]
    datafacturare = [string for string in elements if string != ""]
    datascadenta=re.findall("Total de plată pană la\:?\s([0-9]{2}\.[0-9]{2}\.[0-9]{4})|Scadent\:?\s([0-9]{4}\-[0-9]{2}\-[0-9]{2})\s|până la data de\:? ([0-9]{2}\.[0-9]{2}\.[0-9]{4})|scadenta\:?\s([0-9]{2}\.[0-9]{2}\.[0-9]{4})\s|Data scadenţei\:? ([0-9]{2}\/[0-9]{2}\/[0-9]{4})|Scadenta\:?\s([0-9]{2}\.[0-9]{2}\.[0-9]{4})\s|Data scadentă\:?\s([0-9]{2}\.[0-9]{2}\.[0-9]{4})|Ultima zi de plată\:?\s([0-9]{2}\.[0-9]{2}\.[0-9]{4})|Ultima zi de plata\:?\s([0-9]{2}\.[0-9]{2}\.[0-9]{4})|Data scadentei\:?\s([0-9]{2}\.[0-9]{2}\.[0-9]{4})", text)
    elements=[element for tupl in datascadenta for element in tupl]
    datascadenta = [string for string in elements if string != ""]
    if datascadenta==[]:
          datascadenta=re.findall("\s([0-9]{2}\.[0-9]{1}[1-9]{0,1}\.[0-9]{4})", text)
          datascadenta=pd.to_datetime(datascadenta, format="%d.%m.%Y")
          datascadenta=datascadenta.max()
          datascadenta=str(datascadenta)
    sumedebani=re.findall("(\-?\d+,\d{2})\s|\s(\-?\d+\.\d{2})\s|Vă rugăm să achitaţi suma de\:?\s(\-?\d+,\d{2})\s|TOTAL DE PLATA .*? (\-?\d+.\d{2})\s|(\-?\d+\.\d{3},\d{2})\s|(\-?\d+?\.\d{3}\.\d{3}\,\d{2})|\s(\-?[0-9]{1,}\.[0-9]{2})\s", text)
    elements=[element for tupl in sumedebani for element in tupl]
    sumedebani = [string for string in elements if string != ""]
    #j=[]
    #for i in sumedebani:
    #    i=i.replace('.','')
    #    i=i.replace(',','.')
    #    j.append(float(i))
    #totalplata=max(j)
    IBAN=re.findall("([A-Z]{2}[0-9]{2}\s[a-zA-Z0-9]{4}\s[a-zA-Z0-9]{4}\s[a-zA-Z0-9]{4}\s[a-zA-Z0-9]{4}\s[a-zA-Z0-9]{4})\s|\s([A-Z0-9]{24})\s|\s([A-Z0-9]{11}\s[0-9]{13})|([A-Z]{2}[0-9]{2}[a-zA-Z0-9]{9}\s[a-zA-Z0-9]{13})", text)
    elements=[element for tupl in IBAN for element in tupl]
    IBAN = [string for string in elements if string != ""]
    codfacturare=re.findall("\s([0-9]{14})\s",text)
    furnizor=re.findall("(.{,15}\sS\.A\.)|FURNIZOR\:? (.*? SRL)|(FIRMA .*?) Cumparator|(.{,15}\sSA)|(.{,15}\sSRL)|Furnizor Client(.*? SRL)|Furnizor\:? (.*? SA)|Furnizor\:? (.*? SRL)|Furnizor\:?\s(.*? S\.A\.)|Furnizor\:?\s(.*? S\.R\.L\.)|([a-z\-]{3,}\-[a-z\-]{3,}\-[a-z\-]{3,})|([A-Z]{1}\.[A-Z]{2})\s|([A-Z\-]{1,}\.[A-Z\-]{2,}\s[A-z\-]{3,}\s[A-z\-]{3,})|([A-Z]{2,}\sS\.A\.)|([A-Z\-]{3,}\s[&]\s[A-Z\-]{3,})|(.{,15}\sPFA)", text)
    elements=[element for tupl in furnizor for element in tupl]
    furnizor = [string for string in elements if string != ""]
    furnizor2=re.findall("(.{,20}\sS\.A\.)\s|(.{,20}\sSA)\s|(.{,20}\sSRL)\s|(.{,20}\sPFA)\s|(.{,20}\sS\.R\.L\.)\s", text)
    elements=[element for tupl in furnizor2 for element in tupl]
    furnizor2 = [string for string in elements if string != ""]
    adresafurnizor=re.findall("(Oras:.*?)Cui|SRL (.*?) Capital social|S.A. (.*?) FACTURA", text)
    elements=[element for tupl in adresafurnizor for element in tupl]
    adresafurnizor = [string for string in elements if string != ""]
    adresa=re.findall("(Str\..+Ap\.\s[0-9]{1,}\s)|Adresa: (.*?)suma de|([A-Z]+\.[A-Z]+ NR.[0-9]{2,4}[A-Z])|Str.(.*?)|Adresa\:?\s(.*?ap.\s[0-9]{1,})|Adresa: (.*?)suma de|([A-Z]+\.[A-Z]+ NR.[0-9]{2,4}[A-Z])||.{20}nr\.\s[0-9]{1,2}\-?[0-9]{0,2}", text)
    elements=[element for tupl in adresa for element in tupl]
    adresa = [string for string in elements if string != ""]
    #produse=re.findall("Produse si servicii facturate (.*?) Suma facturata \(fara TVA\)|Denumire\/Produs\/Servicii (.*?)\s\d+\.\d{2}\s|[0-9]{1,}\,[0-9]{2}\s[0-9]{1,}\,[0-9]{2}(.*?)[0-9]{1,}\,[0-9]{2}\s[0-9]{1,}\,[0-9]{2}|[0-9]{1,}\,?[0-9]{0,}(.*?)[0-9]{1,}\,[0-9]{2}|[0-9]{1,}\s(.*?)[0-9]{1,}", text)
    #elements=[element for tupl in produse for element in tupl]
    #produse = [string for string in elements if string != ""]
    codclient=re.findall("COD CLIENT\:? ([0-9]{7,})|Cod abonat\:? ([0-9]{10})|Cod client\:? ([0-9]{8})|Cod client\:? ([0-9]{7,})\s", text)
    elements=[element for tupl in codclient for element in tupl]
    codclient = [string for string in elements if string != ""]
    nrfacturii=re.findall("Nr. Facturii\:? ([0-9]{8})|Nr. factură\:? ([0-9]{10,})|Numar factura\:? ([A-Z0-9]{6} [0-9]{6})|Nr. ([0-9]{8})|\s([0-9]{11})\s|Număr factură\:? ([0-9]{6,})|\s([A-Z]{3,}[0-9]{8,})|nr.\s([0-9]{8,})", text)
    elements=[element for tupl in nrfacturii for element in tupl]
    nrfacturii = [string for string in elements if string != ""]
    punctdelucru=re.findall("PUNCT DE LUCRU: (.*?) CHITANTA", text)
    rambursla=re.findall("ramburs la ([A-Z]+ [0-9]+)", text)
    clientulexpeditor=re.findall("(clientul .*?) Tiparit",text)
    amprimitdela=re.findall("Am primit de la +: (.*?) CIF|Am primit de la +: (.*?) Adresa", text)
    elements=[element for tupl in amprimitdela for element in tupl]
    amprimitdela = [string for string in elements if string != ""]
    CI=re.findall("([A-Z]{2}[0-9]{8})\s", text)
    camp=['telefon','postal code','CIF','carte de identitate','seria','nume persoana','perioada facturare',
         'data facturare', 'data scadenta', 'sume de bani','IBAN', 'cod facturare', 'furnizor', 'furnizor','adresa furnizor', 'adresa recipient',
         'cod client', 'nr facturii', 'punct de lucru', 'ramburs la', 'clientul expeditor', 'am primit de la', 'CI','produse']
    valoare=[telefon,postalcode,CIF,cartedeidentitate,seriabuna,numepersoana,perioadafacturare,
         datafacturare, datascadenta, sumedebani,IBAN, codfacturare, furnizor, furnizor2, adresafurnizor, adresa,
         codclient, nrfacturii, punctdelucru, rambursla, clientulexpeditor, amprimitdela, CI, show_entsproduct(doc)]
    table=PrettyTable(['camp','valoare'])
    for x in range(0,len(camp)):
        table.add_row([camp[x],valoare[x]])
    return table
#EXPORT TABLE TO CSV
def test2(table):
      data = table.get_string()
      result = [tuple(filter(None, map(str.strip, splitline))) for line in data.splitlines() for splitline in [line.split("|")] if len(splitline) > 1]
      with open('D:/BusuiocI/Desktop/output.csv', 'w', newline='', encoding="utf-8") as outcsv:
            writer = csv.writer(outcsv)
            writer.writerows(result)

