#!/usr/bin/env python3
import sys,os
syspath0=sys.path[0]
exec(open(sys.path[0]+"/../VirtualPython3/bin/activate_this.py").read(), {'__file__': sys.path[0]+"/../VirtualPython3/bin/activate_this.py"})
sys.path.append(sys.path[0])
sys.path[0] = syspath0
from PyQt5.QtWidgets import QApplication
app = QApplication(sys.argv)
import shutil
from google_images_download import google_images_download 
import Checkwindow
import ErkennungsWindow
import MessageBox
import Picswindow
import TrainModelWindow
sys.path.append(sys.path[0]+"/../RealtimeDetection/QtGui")
import Launchwindow

Headpath = sys.path[0]+"/.."

checkwindow = Checkwindow.Checkwindow()
choosewindow = ErkennungsWindow.Choosewindow()
picswindow = Picswindow.Picswindow()
trainModelWindow = TrainModelWindow.TrainModelwindow()
messagewindow = MessageBox.Messagewindow()
LaunchWindow=Launchwindow.Launchwindow()
ModelNumber,batchsize,evals,savename = 6,64,50,"test"



def weiter_checkwindow():
    if Checkwindow.AllInstalled:
        #choosewindow.Choosewindow.show()
        checkwindow.Checkwindow.close()
    else:
        messagewindow.show_window("Warte bis die Installation <br>beendet ist!")

        

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
    checkwindow.Checkwindow.show()
def stop_trainModel():
    trainModelWindow.TainModelwindow.close()
    
    


choosewindow.buttonWeiter.clicked.connect(weiter_choosewindow)
checkwindow.buttonWeiter.clicked.connect(weiter_checkwindow)
picswindow.buttonWeiter.clicked.connect(weiter_picswindow)
trainModelWindow.buttonWeiter.clicked.connect(weiter_trainModel)
trainModelWindow.buttonStop.clicked.connect(weiter_trainModel)

choosewindow.Choosewindow.show()
LaunchWindow.Launchwindow.show()

app.exec_()
