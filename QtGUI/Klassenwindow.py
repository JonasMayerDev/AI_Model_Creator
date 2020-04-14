#!/usr/bin/env python3

#AI_Model_Creator; an easy to use AI cumputer vision model creator.
#Copyright (C) 2020  Jonas Mayer

#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by    
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.

#You should have received a copy of the GNU General Public License
#along with this program.  If not, see <https://www.gnu.org/licenses/>.
#You can contact me by mail: bysuxaxofficial@gmail.com

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
        
    
    



    