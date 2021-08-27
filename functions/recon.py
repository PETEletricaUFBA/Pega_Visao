import cv2
import os
from datetime import datetime
import numpy as np

DIRe = r'Resources/Faces'#alterar o caminho se necessário
imgDIRe = r'Resources/Faces/val/ben_afflek/5.jpg'

def recon(imgDIR, DIR):

    img = cv2.imread(imgDIR)

    people = []
    for i in os.listdir(DIR + '/train'):
        people.append(i)

    haar = cv2.CascadeClassifier(DIR + '/haar_face.xml')
    features = np.load(DIR + '/features.npy', allow_pickle=True)
    labels = np.load(DIR + '/labels.npy', allow_pickle=True)

    face_recognizer= cv2.face.LBPHFaceRecognizer_create()
    face_recognizer.read(DIR + '/face_trained.yml') # arquivo resultado do face_trainer.py

    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    faces_detected = haar.detectMultiScale(gray, 1.1 , 4)

    for (x, y, w, h) in faces_detected:
        faces_roi = gray[y:y+h, x:x+w]

        label, confidence  = face_recognizer.predict(faces_roi)
        print(f'Label = {people[label]} with confidence of {confidence}')

    now = datetime.now()
    date_time = now.strftime("%Y%m%d-%H%M%S")

    cv2.imwrite(filename=DIR + '/waiting/' + f'{date_time}-{label}-{confidence}.jpg', img=img)

    return label, confidence
