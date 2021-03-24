import os
import numpy as np 
import cv2 as cv 

DIR = r'Exemplos Python OpenCV/Resources/Faces/train'#alterar o caminho se necessário
people = []
for i in os.listdir(DIR):
    people.append(i)

features = []
labels = []
haar_cascade = cv.CascadeClassifier('Exemplos Python OpenCV/Seção 3/haar_face.xml')

def createTrain():
    for person in people:
        path = os.path.join(DIR, person)
        label = people.index(person)

        for img in os.listdir(path):
            img_path = os.path.join(path, img)

            img_array = cv.imread(img_path)
            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)

            faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)

            for(x, y, w, h) in faces_rect:
                faces_roi = gray[y:y+h, x:x+w]
                features.append(faces_roi)
                labels.append(label)

createTrain()

features = np.array(features, dtype='object')
labels = np.array(labels)

print(f'Length of features = {len(features)}')
print(f'Length of labels = {len(labels)}')

face_recognizer = cv.face.LBPHFaceRecognizer_create()

face_recognizer.train(features,labels)

face_recognizer.save('Exemplos Python OpenCV/Seção 3/face_trained.yml')
np.save('Exemplos Python OpenCV/Seção 3/features.npy', features)
np.save('Exemplos Python OpenCV/Seção 3/labels.npy', labels)
