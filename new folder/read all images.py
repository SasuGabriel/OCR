# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import os
import cv2
def load_images_from_folder(folder):
    images = []
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder,filename))
        if img is not None:
            images.append(img)
    return images

load_images_from_folder('D:/BusuiocI/Documents/Bibliografie/Anul 2, Sem I/Statistical processing of textual data/Baza de date Analiza text/Facturi Analiza text-Ilinca/eon')
