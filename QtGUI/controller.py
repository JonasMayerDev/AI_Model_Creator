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

import sys,os
syspath0=sys.path[0]
exec(open(sys.path[0]+"/../VirtualPython3/bin/activate_this.py").read(), {'__file__': sys.path[0]+"/../VirtualPython3/bin/activate_this.py"})
sys.path.append(sys.path[0])
sys.path[0] = syspath0
from PyQt5.QtWidgets import QApplication
app = QApplication(sys.argv)
import shutil
from google_images_download import google_images_download 
import ErkennungsWindow
import MessageBox
import Picswindow
import TrainModelWindow


Headpath = sys.path[0]+"/.."


choosewindow = ErkennungsWindow.Choosewindow()
picswindow = Picswindow.Picswindow()
trainModelWindow = TrainModelWindow.TrainModelwindow()
messagewindow = MessageBox.Messagewindow()

ModelNumber,batchsize,evals,savename = 6,64,50,"test"

        

def weiter_choosewindow():
    global evals
    global batchsize
    global ModelNumber
    global savename
    if choosewindow.wasNameSet:
        picswindow.Picswindow.show()
        choosewindow.Choosewindow.close()
        evals = choosewindow.sliderEval.value()
        batchsize = choosewindow.sliderRAM.value()
        ModelNumber = choosewindow.sliderModel.value()
        savename = choosewindow.lineEditName.text()

    else:
        messagewindow.show_window("Du musst einen Namen wählen <b>UND</b> <br>den Speichern button drücken")
        
def weiter_picswindow():
    global evals
    global batchsize
    global ModelNumber
    global savename
    if not picswindow.klassen == []:
        picswindow.Picswindow.close()
        klassen = picswindow.klassen
        
        if not "TrainPics" in os.listdir(Headpath):
            os.mkdir(Headpath+"/TrainPics")
            os.mkdir(Headpath+"/TrainPics/test")
            os.mkdir(Headpath+"/TrainPics/train")
        else:
            shutil.rmtree(Headpath+"/TrainPics")
            os.mkdir(Headpath+"/TrainPics")
            os.mkdir(Headpath+"/TrainPics/test")
            os.mkdir(Headpath+"/TrainPics/train")
    
        for klasse in klassen:
            testPics = klasse[1][::10]
            trainPics = klasse[1].copy()
            for testPic in testPics:
                trainPics.remove(testPic)

            Klasspath = Headpath+"/TrainPics/test/"+klasse[0]
            os.mkdir(Klasspath)
            

            for filepath in testPics:
                filename = filepath.split("/")[-1]
                shutil.copyfile(filepath,Klasspath+"/"+filename)

            Klasspath = Headpath+"/TrainPics/train/"+klasse[0]
            os.mkdir(Klasspath)

            for filepath in trainPics:
                filename = filepath.split("/")[-1]
                shutil.copyfile(filepath,Klasspath+"/"+filename)

        picswindow.Picswindow.close()
        trainModelWindow.startTraining(ModelNumber,batchsize,evals,savename)

    else:
        messagewindow.show_window("Du musst mindestens eine Klasse erstelen!")

def weiter_trainModel():
    trainModelWindow.TainModelwindow.close()
    if not "Realtime_Detect" in os.listdir(sys.path[0]+"/.."):
        cmd = "cd "+sys.path[0]+"/.. && git clone https://github.com/BySuxax/Realtime_Detect.git"
        os.system(cmd)
    sys.path.append(sys.path[0]+"/../Realtime_Detect/QtGui")
    import Launchwindow
    import Checkwindow
    LaunchWindow=Launchwindow.Launchwindow()
    checkwindow = Checkwindow.Checkwindow()
    
    def weiter_checkwindow():
        if checkwindow.allInstallesComplet:
            #choosewindow.Choosewindow.show()
            LaunchWindow.Launchwindow.show()
            checkwindow.Checkwindow.close()
        else:
            messagewindow.show_window("Warte bis die Installation <br>beendet ist!")
    checkwindow.buttonWeiter.clicked.connect(weiter_checkwindow)
    checkwindow.Checkwindow.show()
def stop_trainModel():
    trainModelWindow.TainModelwindow.close()
    exit()
    
    


choosewindow.buttonWeiter.clicked.connect(weiter_choosewindow)

picswindow.buttonWeiter.clicked.connect(weiter_picswindow)
trainModelWindow.buttonWeiter.clicked.connect(weiter_trainModel)
trainModelWindow.buttonStop.clicked.connect(stop_trainModel)

choosewindow.Choosewindow.show()


app.exec_()
