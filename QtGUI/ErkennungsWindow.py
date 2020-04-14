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

