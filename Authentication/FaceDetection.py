import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime
import sys
from SysPaths import *
 
def findEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList

def TimeSec():
    now = datetime.now()
    return now.second+(now.minute*60)+(now.hour*60*60)

def Login(ID):
    with open(os.path.join(AuthPath,'LoginRecord.csv'),'a') as f:
        now = datetime.now()
        dateStr = now.strftime('%d-%m-%y')
        dtString = now.strftime('%H:%M:%S')
        f.writelines(f'{ID},{dtString},{dateStr}\n')

def detectFace():
    name = "Not Found"
    path = os.path.join(AuthPath, "LoginFaces")
    print(path)
    images = []
    classNames = []
    myList = [x for x in os.listdir(path) if '.jpg' in x]
    for cl in myList:
        curImg = cv2.imread(os.path.join(path, cl))
        images.append(curImg)
        classNames.append(os.path.splitext(cl)[0])
    
    encodeListKnown = findEncodings(images)
    print('Encoding Complete')
    
    cap = cv2.VideoCapture(0)
    notMatched = True
    initial = TimeSec()
    Timer = True
    while notMatched and Timer:
        success, img = cap.read()
        imgS = cv2.resize(img,(0,0),None,0.25,0.25)
        imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)
        
        facesCurFrame = face_recognition.face_locations(imgS)
        encodesCurFrame = face_recognition.face_encodings(imgS,facesCurFrame)
        
        for encodeFace,faceLoc in zip(encodesCurFrame,facesCurFrame):
            matches = face_recognition.compare_faces(encodeListKnown,encodeFace)
            faceDis = face_recognition.face_distance(encodeListKnown,encodeFace)
            matchIndex = np.argmin(faceDis)
        
            if matches[matchIndex]:
                name = classNames[matchIndex]
                y1,x2,y2,x1 = faceLoc
                y1, x2, y2, x1 = y1*4,x2*4,y2*4,x1*4
                cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
                cv2.rectangle(img,(x1,y2-35),(x2,y2),(0,255,0),cv2.FILLED)
                cv2.putText(img,name,(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
                Login(name)
                notMatched = False
                break
            
        cv2.imshow('Webcam',img)
        cv2.waitKey(1)
        Timer = TimeSec()-initial<5
    return name