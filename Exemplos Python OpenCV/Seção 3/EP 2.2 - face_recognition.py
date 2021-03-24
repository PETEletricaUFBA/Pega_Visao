import numpy as np
import cv2 as cv 
import os

haar_cascade = cv.CascadeClassifier('Exemplos Python OpenCV/Seção 3/haar_face.xml')

DIR = r'Exemplos Python OpenCV/Resources/Faces/train'#alterar o caminho se necessário
people = []
for i in os.listdir(DIR):
    people.append(i)

print(people)
# Carregando as variáveis salvas pelo face_trainer
features = np.load('Exemplos Python OpenCV/Seção 3/features.npy', allow_pickle=True)
labels = np.load('Exemplos Python OpenCV/Seção 3/labels.npy', allow_pickle=True)

face_recognizer= cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('Exemplos Python OpenCV/Seção 3/face_trained.yml')

# Fase de teste 

img = cv.imread(r'Exemplos Python OpenCV/Resources/Faces/val/ben_afflek/3.jpg')# Coloque aqui o caminho até a imagem/foto que deseja testar
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

cv.imshow('Person', gray)

## Detecção do rosto
faces_detected = haar_cascade.detectMultiScale(gray, 1.1 , 4)

for (x, y, w, h) in faces_detected:
    faces_roi = gray[y:y+h, x:x+w]

    label, confidence  = face_recognizer.predict(faces_roi)
    print(f'Label = {people[label]} with confidence of {confidence}')

    cv.putText(img, str(people[label]), (20,20), cv.FONT_HERSHEY_COMPLEX, 1.0, (0,255,0), thickness=2)
    cv.rectangle(img, (x,y), (x+w,y+h), (0,255,0), thickness=2)

cv.imshow('Detected', img)
cv.waitKey(0)
