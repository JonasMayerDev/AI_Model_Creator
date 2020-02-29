import sys
syspath0=sys.path[0]
exec(open(sys.path[0]+"/../VirtualPython3/bin/activate_this.py").read(), {'__file__': sys.path[0]+"/../VirtualPython3/bin/activate_this.py"})
sys.path.append(sys.path[0])
sys.path[0] = syspath0
from torch import nn,optim,utils,exp,stack,autograd,save,load
from torchvision import transforms,models,datasets
import os
import time
from PIL import Image

def load_train_test_pics(path,batchSize):
    
    #model2 = models.squeezenet1_0(pretrained=True)
    #model_out = 1000

    normalize = transforms.Normalize(
        mean=[0.485,0.456,0.406],
        std=[0.229,0.224,0.225]
    )

    transformTrain = transforms.Compose([
        transforms.RandomRotation(30),
        transforms.RandomResizedCrop(224),
        transforms.RandomHorizontalFlip(),
        transforms.ToTensor(),
        normalize
    ])


    transformTest = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(256),
        transforms.ToTensor(),
        normalize
    ])

    testImages=[]
    trainImages=[]

    testImages = datasets.ImageFolder(path+"/test/",transform=transformTest)
    trainImages = datasets.ImageFolder(path+"/train/",transform=transformTrain)
    classes=testImages.classes
    
    testImages=utils.data.DataLoader(testImages,batch_size=batchSize)
    trainImages=utils.data.DataLoader(trainImages,batch_size=batchSize,shuffle=True)
    return (trainImages,testImages,classes)


def make_model(modelnum,classes):
    model = models.vgg16(pretrained=True)
    
    if modelnum == 6:
        model = models.vgg16(pretrained=True)

    for parameter in model.parameters():
        parameter.requires_grad = False

    classifier = nn.Sequential(
        
        nn.Linear(25088,200),
        nn.ReLU(),
        nn.Dropout(p=0.5),
        nn.Linear(200,len(classes)),
        nn.LogSoftmax(dim=1))
    model.classifier = classifier
    
    return model
    
def train_one_eval(model,trainImages,learnrate=0.0001):

    criterion = nn.NLLLoss()
    optimizer = optim.Adam(model.classifier.parameters(),lr=learnrate)

    model.train()
    for image,label in iter(trainImages):
        optimizer.zero_grad()
        output = model.forward(image)
                    
        loss = criterion(output,label)
        loss.backward()
        optimizer.step()
        
    return (model,loss)

def test_model(model,testImages,classes):
    model.eval()
    criterion = nn.NLLLoss()
    loss = 0
    namenTest=[]
    namenLabel=[]
    for images,labels in iter(testImages):
        
        output = model.forward(images)
        loss2 = criterion(output,labels)
        print(loss2)
        loss += loss2
        output = exp(output)
        
        for i in range(len(output)):
            namenTest.append("None")
            a =0
            for proz in output[i]:
                if float(proz)>0.8:
                    namenTest[i]=classes[a]
		    
                a=a+1
        for i in range(len(labels)):
            namenLabel.append(classes[int(labels[i])])
           

    loss = loss/len(iter(testImages))
    return (loss,namenTest,namenLabel)
