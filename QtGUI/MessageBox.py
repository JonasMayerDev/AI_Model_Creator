#!/usr/bin/env python3
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

        