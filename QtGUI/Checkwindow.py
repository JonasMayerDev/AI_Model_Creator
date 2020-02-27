#!/usr/bin/env python3
import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow,QWidget,QCheckBox,QRadioButton
from PyQt5 import uic
from PyQt5.QtCore import QThread, QObject,pyqtSignal


#progressBarInstall = None
checkBoxROS = None


class Installer(QObject):
    progressBarInstall = pyqtSignal(int)
    
    def startInstalling(self):
        global checkBoxROS

        self.progressBarInstall.emit(1)

        if checkBoxROS.isChecked():
            answerRos=os.system("/bin/bash "+sys.path[0]+"/../"+"InstallRos.bash "+sys.path[0]+"/..")
            self.progressBarInstall.emit(50)
            awnserRosVP3=os.system("/bin/bash "+sys.path[0]+"/../"+"InstallRosVP3.bash "+sys.path[0]+"/..")
        else: 
            print("Bitte wählen sie eine Option")
        self.progressBarInstall.emit(100)
        


class Checkwindow:
    
    def __init__(self):
        
        global checkBoxROS

        self.Checkwindow = uic.loadUi("Checkwindow.ui")
        self.buttonAutoInstall = self.Checkwindow.pushButtonAuto
        self.buttonManuelInstall = self.Checkwindow.pushButtonManuel
        self.buttonWeiter = self.Checkwindow.pushButtonWeiter
        self.progressBarInstall =  self.Checkwindow.progress_bar

        checkBoxROS = self.Checkwindow.frame_2.findChild(QCheckBox,"check_box_ros")
        
        self.allInstallesComplet = True

        def update_progressbar(val):
            self.progressBarInstall.setValue(val)
            if val == 100:
                self.allInstallesComplet = True
            else:
                self.allInstallesComplet = False


        def test():
            self.buttonAutoInstall.setVisible(False)
            self.progressBarInstall.setVisible(True)
            self.progressBarInstall.setValue(0)
            self.obj = Installer()  #starte nebenprocesse 
            self.obj.progressBarInstall.connect(update_progressbar)
            self.thread = QThread()  
            self.obj.moveToThread(self.thread)
            self.thread.started.connect(self.obj.startInstalling)    
            self.thread.start()

            
        
        self.progressBarInstall.setVisible(False)
        self.buttonAutoInstall.clicked.connect(test)
        


    
    
        #print(dir(checkBoxUseKamera))
