import os
import numpy as np 
import cv2 as cv 

people = ['Neymar', 'Not Neymar']
DIR = r'C:\Users\user\Desktop\3KOI\py\OPCV\Fotos'#alterar o caminho se necessário

haar = cv.CascadeClassifier('haar_cascade.xml')

features=[]
labels=[]

def train_see():
    for person in people:
        path = os.path.join(DIR, person)
        label = people.index(person)

        for img in os.listdir(path):
            img_path = os.path.join(path,img)

            img_array = cv.imread(img_path)
            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)

            faces_detected = haar.detectMultiScale(gray, scaleFactor=1.1 , minNeighbors= 4)

            for (x,y,a,b) in faces_detected:
                face_roi = gray[y:y+b, x:x+a]
                features.append(face_roi)
                labels.append(label)

train_see()

features = np.array(features, dtype='object')
labels = np.array(labels)

print(f'Length of features = {len(features)}')
print(f'Length of labels = {len(labels)}')

face_recognizer= cv.face.LBPHFaceRecognizer_create()

face_recognizer.train(features,labels)

face_recognizer.save('face_neymar.yml')
np.save('features.npy', features)
np.save('labels.npy', labels)
