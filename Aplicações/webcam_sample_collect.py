import cv2
from time import sleep
import os
import numpy as np

DIR = r'Exemplos Python OpenCV/Resources/Faces/train/' + 'test' # Especifique a pasta nova

key = cv2.waitKey(1)
webcam = cv2.VideoCapture(0)
haar = cv2.CascadeClassifier('Aplicações/haar_cascade.xml')
os.mkdir(DIR) #talvez precise criar um pasta
os.chdir(DIR)# mude aqui para selecionar a pasta

i = 0
sleep(2)

while True:
    try:
        check, frame = webcam.read()
        cv2.imshow("Capturing", frame)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces_detected = haar.detectMultiScale(gray, scaleFactor=1.1 , minNeighbors= 5)
        
        cv2.imwrite(filename=f'foto{i}.jpg', img=frame)
        i = i + 1

        if(i>= 1000):# altere aqui para escoler o numero de Fotos
            #os.chdir('../')
            os.chdir('../')
            break

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
