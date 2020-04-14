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
syspath0=sys.path[0]
exec(open(sys.path[0]+"/../VirtualPython3/bin/activate_this.py").read(), {'__file__': sys.path[0]+"/../VirtualPython3/bin/activate_this.py"})
sys.path.append(sys.path[0])
sys.path[0] = syspath0
import os
from PyQt5.QtWidgets import QApplication, QMainWindow,QWidget,QCheckBox,QRadioButton
from PyQt5 import uic
from PyQt5.QtCore import QThread, QObject,pyqtSignal
import functools
import TrainModel
from torch import nn,optim,utils,exp,stack,autograd,save,load

class Trainer(QObject):

    signalProgressBar = pyqtSignal(int)
    signalLossTrain = pyqtSignal(float)
    signalProgressBarTrain = pyqtSignal(int)
    signalLossTest = pyqtSignal(float)
    signalProgressBarTest = pyqtSignal(int)
    
    
    def startTraining(self,modelnumber,batchsize,evals,saveName="test"):
        os.system("mkdir "+sys.path[0]+"/../Models/"+saveName)
        model = TrainModel.make_model(modelnumber,os.listdir(sys.path[0]+"/../TrainPics/train"))
        picsLoadedTrain,picsLoadedTest,classes = TrainModel.load_train_test_pics(sys.path[0]+"/../TrainPics",batchsize)
        
        for i in range(evals):
            
            model,loss = TrainModel.train_one_eval(model,picsLoadedTrain)
            print("Loss bei eval "+str(i)+" ist: "+str(float(loss.data)))
            self.signalProgressBar.emit(int((i/evals)*100))
            self.signalLossTrain.emit(float(loss.data))
            self.signalProgressBarTrain.emit((float(loss.data)**(1/4))*100)
            if i % 10 ==0:
                save({
                    "model":model,
                    "classes":classes
                },sys.path[0]+"/../Models/"+saveName+"/"+saveName+"_CheckPoint_"+str(i)+".pt")
                loss,NamesOut,NamesLabel=TrainModel.test_model(model,picsLoadedTest,classes)
                print("Die Bilder wurden als:  "+str(NamesOut)+"  und sollten so sein:  "+str(NamesLabel)+"  Deshalb gilt der Fehler: "+str(float(loss)))
                self.signalProgressBarTest.emit((float(loss.data)**(1/4))*100)
                self.signalLossTest.emit(float(loss.data))

        self.signalProgressBar.emit(int(100))
        save({
            "model":model,
            "classes":classes
        },sys.path[0]+"/../Models/"+saveName+"/"+saveName+".pt")


class TrainModelwindow:
    
    def __init__(self):
        self.TainModelwindow = uic.loadUi("TrainModelwindow.ui")
        self.progressBar = self.TainModelwindow.progressBar
        self.numberLossTrain = self.TainModelwindow.lcdNumber
        self.numberLossTest = self.TainModelwindow.lcdNumber2
        self.progressBarTrain = self.TainModelwindow.progressBar1
        self.progressBarTest = self.TainModelwindow.progressBar2

        self.buttonWeiter = self.TainModelwindow.weiter
        self.buttonStop = self.TainModelwindow.stop

        self.sucessLabel = self.TainModelwindow.sucessLabel
        self.sucessLabel.setVisible(False)
        self.buttonWeiter.setVisible(False)
        self.buttonStop.setVisible(False)
        self.progressBarTest.setValue(100)
        self.progressBarTrain.setValue(100)
        
    def startTraining(self,modelnumber,batchsize,evals,savename):
        self.TainModelwindow.show()
        self.progressBar.setValue(0)
        self.obj = Trainer()  #starte nebenprocesse 
        self.obj.signalProgressBar.connect(self.update_progressbar)
        self.obj.signalLossTrain.connect(self.update_numberLossTrain)
        self.obj.signalProgressBarTrain.connect(self.update_progressbarTrain)
        self.obj.signalLossTest.connect(self.update_numberLossTest)
        self.obj.signalProgressBarTest.connect(self.update_progressbarTest)
        self.thread = QThread()  
        self.obj.moveToThread(self.thread)
        self.thread.started.connect(functools.partial(self.obj.startTraining,modelnumber,batchsize,evals+10,savename)) #TOD0 add Params    
        self.thread.start()

    def update_progressbar(self,val):
        if val == 100:
            self.sucessLabel.setVisible(True)
            self.buttonWeiter.setVisible(True)
            self.buttonStop.setVisible(True)
        self.progressBar.setValue(val)
    def update_numberLossTrain(self,val):
        self.numberLossTrain.display(val)
    def update_numberLossTest(self,val):
        self.numberLossTest.display(val)
    def update_progressbarTrain(self,val):
        self.progressBarTrain.setValue(val)
    def update_progressbarTest(self,val):
        self.progressBarTest.setValue(val)
    

            
        
        
