
#REGEX UNIVERSAL
import re
telephone=re.findall("Număr telefon/cont: (0\d{9}\s)| (0\d{9}\s)|(0\d{4} \d{2} \d{2} \d{2}\s)| (0\d{9})\s|Voce: ([0-9]{10})", text)
postalcodesender=re.findall("\s\d{6}\s|\s\d{6}\,", text)
CIF=re.findall("\s[A-Z][A-Z]\d{4,10}\s|\s[A-Z][A-Z]\d{6,10}\s|\sR\d{9}\s|\sR\d{9}|Cod de inregistrare fiscala: +([A-z0-9]{9})|CIF:\s([A-Z][A-Z]\d{4,10})", text)
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
IBAN=re.findall("Cod IBAN:\s([A-Z]{2}[0-9]{2}\s[a-zA-Z0-9]{4}\s[a-zA-Z0-9]{4}\s[a-zA-Z0-9]{4}\s[a-zA-Z0-9]{4}\s[a-zA-Z0-9]{4})\s|\s([A-Z0-9]{24})\s|\s([A-Z0-9]{11}\s[0-9]{13})|([A-Z]{2}[0-9]{2}\s[a-zA-Z0-9]{4}\s[a-zA-Z0-9]{4}\s[a-zA-Z0-9]{4}\s[a-zA-Z0-9]{4}\s[a-zA-Z0-9]{4})\s", text)
codfacturare=re.findall("\s([0-9]{14})\s", text)
furnizor=re.findall("[0-9]+ (.*? S.A.)|FURNIZOR: (.*? SRL)|(FIRMA .*?) Cumparator|(.*? SA)|(.*? SRL)|(.*? S.A.)", text)
adresafurnizor=re.findall("(Oras:.*?)Cui|SRL (.*?) Capital social|S.A. (.*?) FACTURA|Str\.\s(.*?)\n", text)
adresadestinatar=re.findall("Adresa: (.*?)suma de|([A-Z]+\.[A-Z]+ NR.[0-9]{2,4}[A-Z])|Str\.\s(.*?)\n", text)
produse=re.findall("Produse si servicii facturate (.*?) Suma facturata \(fara TVA\)|Denumire\/Produs\/Servicii (.*?)\s\d+\.\d{2}\s", text)
codclient=re.findall("COD CLIENT: ([0-9]{9})|Cod abonat: ([0-9]{10})|Cod client: ([0-9]{8})", text)
nrfacturii=re.findall("Nr. Facturii: ([0-9]{8})|Nr. factură: ([0-9]{13})|Numar factura. ([A-Z0-9]{6} [0-9]{6})|Nr. ([0-9]{8})", text)
punctdelucru=re.findall("PUNCT DE LUCRU: (.*?) CHITANTA", text)
rambursla=re.findall("ramburs la ([A-Z]+ [0-9]+)", text)
clientulexpeditor=re.findall("(clientul .*?) Tiparit",text)
amprimitdela=re.findall("Am primit de la +: (.*?) CIF|Am primit de la +: (.*?) Adresa", text)
CI=re.findall("[A-Z]{2}[0-9]{8}", text)
cartedeidentitate=re.findall("([A-Z]{2}[0-9]{6})\n", text)
