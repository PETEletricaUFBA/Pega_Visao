import cv2
from time import sleep
import numpy as np


haar = cv2.CascadeClassifier('haar_cascade.xml')
features = np.load('features.npy', allow_pickle=True)
labels = np.load('labels.npy', allow_pickle=True)

face_recognizer= cv2.face.LBPHFaceRecognizer_create()
face_recognizer.read('face.yml') # arquivo resultado do face_trainer.py

people = ['FRED','Neymar','Desconhecido']
key = cv2. waitKey(1)
webcam = cv2.VideoCapture(0)

sleep(2)

while True:
    try:
        check, frame = webcam.read()
        # cv2.imshow("Capturing", frame)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces_detected = haar.detectMultiScale(gray, scaleFactor=1.1 , minNeighbors= 5)

        for (x,y,a,b) in faces_detected:
            face_roi = gray[y:y+b, x:x+a]

            label, confidence  = face_recognizer.predict(face_roi)
            print(f'Label = {people[label]} with confidence of {confidence}')

            cv2.putText(frame, str(people[label]), (20,20), cv2.FONT_HERSHEY_COMPLEX, 1.0, (0,255,0), thickness=2)
            cv2.rectangle(frame, (x,y), (x+a,y+b), (0,255,0), thickness=2)

        cv2.imshow("Capturing", frame)

        key = cv2.waitKey(1)
        if key == ord('q'):
            webcam.release()
            cv2.destroyAllWindows()
            break

    except(KeyboardInterrupt):
        webcam.release()
        print("Program ended.")
        cv2.destroyAllWindows()
        break
