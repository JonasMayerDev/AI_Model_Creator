#!/usr/bin/env python3
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow,QWidget,QCheckBox,QRadioButton,QSlider
from PyQt5 import uic


class Choosewindow:
    
    def __init__(self):
        self.Choosewindow = uic.loadUi("ErkennungsWindow.ui")

        self.buttonName = self.Choosewindow.buttonName
        self.buttonNormal = self.Choosewindow.buttonNormal
        self.buttonWeiter = self.Choosewindow.buttonWeiter

        self.lineEditName = self.Choosewindow.lineEditName

        self.sliderEval = self.Choosewindow.sliderEval
        self.sliderModel = self.Choosewindow.sliderModel
        self.sliderRAM = self.Choosewindow.sliderRAM

        
        self.buttonName.setText("Model Name Speichern")
        self.sliderModel.setValue(8)
        self.sliderRAM.setValue(64)
        self.sliderEval.setValue(250)
        self.wasNameSet = False
        def lock_name():
            #print(dir(self.buttonName))
            if self.buttonName.text() == "Model Name Speichern":
                
                self.lineEditName.setEnabled(False)
               
                self.buttonName.setText("Edit Model Name")
                self.wasNameSet = True
            else:
                self.lineEditName.setEnabled(True)
                #TODO check if alredy exist!
                
                self.buttonName.setText("Model Name Speichern")
                self.wasNameSet = False


        self.buttonName.clicked.connect(lock_name)

