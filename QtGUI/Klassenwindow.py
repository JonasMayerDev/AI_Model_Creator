#!/usr/bin/env python3
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow,QWidget,QCheckBox,QRadioButton,QSlider
from PyQt5.QtGui import QPixmap,QIcon

from PyQt5 import uic

class Klassenwindow:
    
    def __init__(self):
        self.Klassenwindow = uic.loadUi("Klassenwindow.ui")
        self.comboBox= self.Klassenwindow.comboBox
        self.buttonAdd= self.Klassenwindow.buttonAdd
        self.lineName = self.Klassenwindow.lineName
        self.buttonWeiter = self.Klassenwindow.buttonWeiter
        self.Class = ""
    def getClass(self,klassen):
        self.comboBox.clear()
        for klasse in klassen:
            self.comboBox.addItem(QIcon(),klasse[0])
        self.Klassenwindow.show()
        
    
    



    