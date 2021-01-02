# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 20:53:44 2020

@author: Andre
"""
import cv2
import os
import numpy as np
import pytesseract
import pandas as pd
from pytesseract import Output
from  PIL import  Image
pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'
img=cv2.imread("D:\BusuiocI\Documents/Bibliografie/Anul 2, Sem I/Statistical processing of textual data/Baza de date Analiza text/Facturi Analiza text-Ilinca/romtelecom/20201026_182941.jpg",0)

custom_config = r'-l ron --dpi 600 --oem 1 --psm 12 '
img_path='D:\BusuiocI\Documents/Bibliografie/Anul 2, Sem I/Statistical processing of textual data/Baza de date Analiza text/Facturi Analiza text-Ilinca/romtelecom/20201026_182941.jpg'
        
import tempfile

IMAGE_SIZE = 1800
BINARY_THREHOLD = 180

def process_image_for_ocr(file_path):
    # TODO : Implement using opencv
    temp_filename = set_image_dpi(file_path)
    im_new = remove_noise_and_smooth(temp_filename)
    return im_new

def set_image_dpi(file_path):
    im = Image.open(file_path)
    length_x, width_y = im.size
    factor = max(1, int(IMAGE_SIZE / length_x))
    size = factor * length_x, factor * width_y
    # size = (1800, 1800)
    im_resized = im.resize(size, Image.ANTIALIAS)
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.jpg')
    temp_filename = temp_file.name
    im_resized.save(temp_filename, dpi=(300, 300))
    return temp_filename

def image_smoothening(img):
    ret1, th1 = cv2.threshold(img, BINARY_THREHOLD, 255, cv2.THRESH_BINARY)
    ret2, th2 = cv2.threshold(th1, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    blur = cv2.GaussianBlur(th2, (1, 1), 0)
    ret3, th3 = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    return th3

def remove_noise_and_smooth(file_name):
    img = cv2.imread(file_name, 0)
    filtered = cv2.adaptiveThreshold(img.astype(np.uint8), 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 41,
                                     3)
    kernel = np.ones((1, 1), np.uint8)
    opening = cv2.morphologyEx(filtered, cv2.MORPH_OPEN, kernel)
    closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel)
    img = image_smoothening(img)
    or_image = cv2.bitwise_or(img, closing)
    return or_image

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

text= pytesseract.image_to_string(img,config=custom_config)
text_file = open("Output.txt", "w", encoding='utf-8')
text_file.write(text)
text_file.close()

#text=text.split('\n')
from nltk import ngrams
n = 2
bigrams = ngrams(text.split(), n)

for grams in bigrams:
  print(grams)
  
text= pytesseract.image_to_string(process_image_for_ocr(img_path),config=custom_config)
text=text.split('\n')

text= pytesseract.image_to_string(set_image_dpi(img_path),config=custom_config)
text=text.split('\n')

text= pytesseract.image_to_string(image_smoothening(img),config=custom_config)
text=text.split('\n')

text= pytesseract.image_to_string(remove_noise_and_smooth(img_path),config=custom_config)
text=text.split('\n')

text= pytesseract.image_to_string(gray(img),config=custom_config)
text=text.split('\n')

text= pytesseract.image_to_string(blur(img),config=custom_config)
text=text.split('\n')

text= pytesseract.image_to_string(threshhold(img),config=custom_config)
text=text.split('\n')

import rowordnet as rwn
wn = rwn.RoWordNet()
word = 'bancă'
synset_ids = wn.synsets(literal=word)
for i in synset_ids:
    print(wn(i))
synset_object = wn('ENG30-13398469-n')
synset_object

