import wx
from wx.lib import statbmp
from PIL import Image
import os
import wx.lib.colourdb
import cv2
import os
import numpy as np
import pytesseract
import pandas as pd
from pytesseract import Output
from  PIL import  Image
import re
from unidecode import unidecode
import csv
from pdf2image import convert_from_path
import fancourierdoc1

wildcard = "Python source (*.py)|*.py|" \
            "All files (*.*)|*.*"
class Input_Panel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.SetBackgroundColour("light blue")
         # Input variables
        self.tittle1=wx.StaticText(self, -1, "Input", (250, 10))
        font = wx.Font(18, wx.DECORATIVE, wx.ITALIC, wx.NORMAL)
        self.tittle1.SetFont(font)  
        self.tittle1.SetForegroundColour('black') 
        # Set sizer for the panel content
        self.sizer = wx.GridBagSizer(2, 2)
        self.sizer.Add(self.tittle1, (1, 2))
        
        # create the buttons and bindings
        openFileDlgBtn = wx.Button(self, label="OPEN")
        openFileDlgBtn.Bind(wx.EVT_BUTTON, self.onOpenFile)
        
        # put the buttons in a sizer
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.Add(openFileDlgBtn, 0, wx.ALL|wx.LEFT, 10, 10)
        self.SetSizer(sizer)
        self.currentDirectory = os.getcwd()

    def onOpenFile(self, event):
        #Create and show the Open FileDialog
        dlg = wx.FileDialog(
            self, message="Choose a file",
            defaultDir=self.currentDirectory, 
            defaultFile="",
            wildcard=wildcard,
            style=wx.FD_OPEN | wx.FD_MULTIPLE | wx.FD_CHANGE_DIR
            )
        if dlg.ShowModal() == wx.ID_OK:
            paths = dlg.GetPaths()
            print("You chose the following file(s):")
            for path in paths:
                print(path)
                if path.endswith('.pdf'):
                    pages = convert_from_path(path, poppler_path=r"C:/Users/pc/Desktop/PrelucrareaStatisticaaDatelorText/proiect/try/poppler-0.68.0/bin") 
                    #Saving pdf page in jpeg format
                    for page in pages:
                        path="C:/Users/pc/Desktop/PrelucrareaStatisticaaDatelorText/proiect/try/output.jpg"
                        page.save(path, "JPEG")
                    image = wx.Image(path, wx.BITMAP_TYPE_ANY)
                    image.Rescale(300,450)
                    self.imageBitmap = wx.StaticBitmap(self, wx.ID_ANY, wx.BitmapFromImage(image))
                    self.imageBitmap.Center()
                else:
                    image = wx.Image(path, wx.BITMAP_TYPE_ANY)
                    image.Rescale(300,450)
                    self.imageBitmap = wx.StaticBitmap(self, wx.ID_ANY, wx.BitmapFromImage(image))
                    self.imageBitmap.Center()
        dlg.Destroy()
        

class Output_Panel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.SetBackgroundColour("light steel blue")
        # Output variable
        self.tittle2 = wx.StaticText(self, -1, "Output", (250, 10)) 
        font = wx.Font(18, wx.DECORATIVE, wx.ITALIC, wx.NORMAL)
        self.tittle2.SetFont(font)  
        self.tittle2.SetForegroundColour('black')  
        downloadFileDlgBtn = wx.Button(self, label="DOWNLOAD") 
        downloadFileDlgBtn.Bind(wx.EVT_BUTTON, self.onDownloadFile) 
        
        saveFileDlgBtn = wx.Button(self, label="UPLOAD")
        saveFileDlgBtn.Bind(wx.EVT_BUTTON, self.onSaveFile)
        
        # Set sizer for the panel content
        self.sizer = wx.GridBagSizer(3, 3)
        self.sizer.Add(self.tittle2, (1, 2))
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(saveFileDlgBtn, 0, wx.ALL|wx.LEFT, 10)
        sizer.Add(downloadFileDlgBtn, 0, wx.ALL|wx.LEFT, 10)
        self.SetSizer(sizer)
        
        self.currentDirectory = os.getcwd()

    def onSaveFile(self, event):
        """
        Create and show the Save FileDialog
        """
        dlg = wx.FileDialog(
            self, message="Save file as ...", 
            defaultDir=self.currentDirectory, 
            defaultFile="", wildcard=wildcard, style=wx.FD_SAVE
            )
        if dlg.ShowModal() == wx.ID_OK:
            path = dlg.GetPath()
            print ("You chose the following filename: %s" % path)
            self.tabel=fancourierdoc1.test1(path)
            return self.tabel
        dlg.Destroy()
    def onDownloadFile(self, event):
        try:
            fancourierdoc1.test2(self.tabel)
            path_image="C:/Users/pc/Desktop/PrelucrareaStatisticaaDatelorText/proiect/try/complete-icon.jpg"
            image = wx.Image(path_image, wx.BITMAP_TYPE_ANY)
            image.Rescale(240,250)
            self.imageBitmap = wx.StaticBitmap(self, wx.ID_ANY, wx.BitmapFromImage(image))
            self.imageBitmap.Center()
            out = True
        except: 
            path_image="C:/Users/pc/Desktop/PrelucrareaStatisticaaDatelorText/proiect/try/incomplete-icon.jpg"
            image = wx.Image(path_image, wx.BITMAP_TYPE_ANY)
            image.Rescale(200,250)
            self.imageBitmap = wx.StaticBitmap(self, wx.ID_ANY, wx.BitmapFromImage(image))
            self.imageBitmap.Center()
            out = False
        if out==True:
            print ("Download complete")
        else:
            print ("Download incomplete")

class Main_Window(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title = title, size=(1280,600))
        
        # Set variable panels
        self.splitter = wx.SplitterWindow(self, style = wx.SP_LIVE_UPDATE)
        self.panel1 = Input_Panel(self.splitter)
        self.panel2 = Output_Panel(self.splitter)
        self.splitter.SplitVertically(self.panel1, self.panel2)
        w, h = self.GetSize()
        self.splitter.SetMinimumPaneSize(w/2)

        self.windowSizer = wx.BoxSizer(wx.VERTICAL)
        self.windowSizer.Add(self.splitter, 1, wx.ALL | wx.EXPAND)   

def main():
    app = wx.App(False)
    frame = Main_Window(None, "OCR App")
    frame.Show()
    app.MainLoop()

if __name__ == "__main__" :
    main()