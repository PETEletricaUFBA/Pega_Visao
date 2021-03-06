import numpy as np
import cv2 as cv 

haar = cv.CascadeClassifier('Exemplos Python OpenCV/Seção 3/haar_face.xml')

# Carregando as variáveis salvas pelo face_trainer
features = np.load('Exemplos Python OpenCV/Seção 3/features.npy', allow_pickle=True)
labels = np.load('Exemplos Python OpenCV/Seção 3/labels.npy', allow_pickle=True)

face_recognizer= cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('Exemplos Python OpenCV/Seção 3/face_trained.yml')

# Fase de teste 

img = cv.imread('Exemplos Python OpenCV/Resources/Faces/val/ben_afflek/2.jpg')# Coloque aqui o caminho até a imagem/foto que deseja testar
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

cv.imshow('Pessoa', gray)

## Detecção do rosto
faces_detected = haar.detectMultiScale(gray, 1.1 , 4)

for (x,y,a,b) in faces_detected:
    face_roi = gray[y:y+b, x:x+a]

    label, confindence  = face_recognizer.predict(face_roi)
    print(f'Label = {people[label]} with confidence of {confidence}')

    cv.putText(img, str(people[label]), (20,20), cv.FONT_HERSHEY_COMPLEX, 1.0, (0,255,0), thickness=2)
    cv.rectangle(img, (x,y), (x+a,y+b), (0,255,0), thickness=2)

cv.imshow('Detected', img)
cv.waitKey(0)
