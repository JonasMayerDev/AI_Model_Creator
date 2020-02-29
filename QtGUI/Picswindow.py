#!/usr/bin/env python3

import sys
import functools 
import os
from PyQt5.QtCore import Qt,QSize
from PyQt5.QtWidgets import QApplication, QMainWindow,QWidget,QCheckBox,QRadioButton,QScrollArea,QGridLayout
from PyQt5.QtWidgets import QGraphicsView,QGraphicsScene,QSizePolicy,QFileDialog,QGraphicsTextItem
from PyQt5.QtGui import QPixmap,QIcon,QFont
from PyQt5 import uic
import Klassenwindow
from google_images_download import google_images_download 

class Picswindow:
    
    def __init__(self):

        self.klassen = []
        self.imagesSelectet = []

        self.headpath = sys.path[0]+"/.."
        self.picsPaths = os.listdir(self.headpath+"/Pics")
        self.FolderPath = self.headpath+"/Pics"
        
        self.Picswindow = uic.loadUi("Picswindow.ui")
        self.klassenwindow = Klassenwindow.Klassenwindow()
        self.scroll =  self.Picswindow.frame.findChild(QScrollArea,"scrollArea")
        self.buttonChoose = self.Picswindow.pushButton
        self.buttonKlasse = self.Picswindow.pushButton_2
        self.buttonWeiter = self.Picswindow.buttonWeiter
        self.buttonDownload = self.Picswindow.buttonDownload
        self.lineKeyword = self.Picswindow.lineKeyword
        self.lineDic = self.Picswindow.lineDic

        self.update_pics_with_path()

        self.klassenwindow.buttonAdd.clicked.connect(self.AddClass)
        self.klassenwindow.buttonWeiter.clicked.connect(self.WeiterClass)
        self.buttonChoose.clicked.connect(self.buttonChooseClicked)
        self.buttonKlasse.clicked.connect(self.klassenbutton)
        self.buttonDownload.clicked.connect(self.download_images)



    def update_pics_with_path(self):

        self.lineDic.setText(self.FolderPath)
        self.picsPaths=self.filterImgs(self.picsPaths)

        widget=QWidget()
        layout = QGridLayout()
        widget.setLayout(layout)
    
        
        rows = int((len(self.picsPaths)/3))
        if (len(self.picsPaths)%3) > 0:
            rows+=1
        posis = [(j,k) for k in range(3) for j in range(rows)]

        for pos,picPath,i in zip(posis,self.picsPaths,range(len(self.picsPaths))):
            #print()
            picView = QGraphicsView(objectName = "img"+str(i))
            picView.setToolTip(self.FolderPath+"/"+picPath)
            layout.addWidget(picView,*pos)
            scene = QGraphicsScene()

            if QPixmap(self.FolderPath+"/"+picPath).isNull() != True:
                scene.addPixmap(QPixmap(self.FolderPath+"/"+picPath).scaled(140, 140, Qt.KeepAspectRatio))
            else:
                print(picPath)
                scene.addText("Bild konnte nicht\ngeladen werden",QFont("Times", 10)) 

            picView.setScene(scene)
            picView.setFixedSize(150,150)

        
        layout.setVerticalSpacing(10)
        self.scroll.setWidget(widget)
        
        i = 0
        while self.scroll.findChild(QGraphicsView,"img"+str(i)) != None:
            self.scroll.findChild(QGraphicsView,"img"+str(i)).mouseReleaseEvent=functools.partial(self.buttonReleased,i)
            i +=1
        


    def filterImgs(self,pathlist):
        filteredPathlist = []
        for path in pathlist:
            if not(not(path[-4:-1]+path[-1] == "jpeg") and not( path[-3:-1]+path[-1] == "png") and not(path[-3:-1]+path[-1] == "jpg")):
                filteredPathlist.append(path)
        return filteredPathlist
        


    def buttonReleased(self,num,event):
        img = self.scroll.findChild(QGraphicsView,"img"+str(num))
        if img.toolTip() in self.imagesSelectet:
            p = img.palette()
            p.setColor(img.backgroundRole(), Qt.white)
            img.setPalette(p)
            self.imagesSelectet.remove(img.toolTip())
        else:
            p = img.palette()
            p.setColor(img.backgroundRole(), Qt.red)
            img.setPalette(p)
            self.imagesSelectet.append(img.toolTip())

    def buttonChooseClicked(self,*args):
        newPicsPath=QFileDialog.getExistingDirectoryUrl().path()
        if os.path.exists(newPicsPath):
            self.picsPaths = os.listdir(newPicsPath)
            self.FolderPath = newPicsPath
            self.update_pics_with_path()
    
    def klassenbutton(self):
        self.klassenwindow.getClass(self.klassen)



    def AddClass(self,**args):
        if self.klassenwindow.lineName.text != "":
            print(self.klassenwindow.lineName.text())
            self.klassenwindow.comboBox.addItem(QIcon(),self.klassenwindow.lineName.text())
        else:
            print("line is empty")
    
    def WeiterClass(self,**args):
        if self.klassenwindow.comboBox.itemText(self.klassenwindow.comboBox.currentIndex()) == "" or self.klassenwindow.comboBox.itemText(self.klassenwindow.comboBox.currentIndex()) == None:
            print("failed no class")
        else:
            klassenNames = [self.klassen[i][0] for i in range(len(self.klassen))]
            if self.klassenwindow.comboBox.itemText(self.klassenwindow.comboBox.currentIndex()) in klassenNames:
                index=klassenNames.index(self.klassenwindow.comboBox.itemText(self.klassenwindow.comboBox.currentIndex()))
                for path in self.imagesSelectet:
                    self.klassen[index][1].append(path)
            else:
                self.klassen.append((self.klassenwindow.comboBox.itemText(self.klassenwindow.comboBox.currentIndex()),self.imagesSelectet))
            
            for path in self.imagesSelectet:
                self.picsPaths.remove(path.split("/")[-1])

            self.update_pics_with_path()
            self.klassenwindow.Klassenwindow.close()
            self.imagesSelectet = []
            print(self.klassen)
    def download_images(self):
        if self.lineKeyword.text() == "":
            print("Bitte geben sie ein Keyword ein!")
        else:
            response = google_images_download.googleimagesdownload()  
            arguments = {"keywords": self.lineKeyword.text(), #,png,jpeg", 
                 "limit":40, 
                 "print_urls":False,
                 "output_directory":self.FolderPath}
            try:
                paths=response.download(arguments)
                print(paths)
                self.picsPaths = paths[0][self.lineKeyword.text()]
                self.FolderPath = self.FolderPath+"/"+self.lineKeyword.text()
                self.update_pics_with_path()
            except Exception as e:
                print(e)
            
            
            
            #os.rename(path,self.FolderPath+"/"+path.split("/")[-1])
            #newPathes.append(self.FolderPath+"/"path.split("/")[-1])

            
            





            
                  
        


        

