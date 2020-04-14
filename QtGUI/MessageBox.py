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
from PyQt5.QtWidgets import QMainWindow,QWidget
from PyQt5 import uic

class Messagewindow:
    
    def __init__(self):
        self.Messagewindow = uic.loadUi("MessageBox.ui")

        self.buttonOk = self.Messagewindow.buttonOk
        self.labelMessage = self.Messagewindow.labelMessage

        def ok_button():
            self.Messagewindow.close()

        self.buttonOk.clicked.connect(ok_button)
    def show_window(self,message):
        self.labelMessage.setText(message)
        self.Messagewindow.show()

        