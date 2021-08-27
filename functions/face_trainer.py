import os
import numpy as np 
import cv2 as cv 


DIRec = r'Resources/Faces'

def face_trainer(DIR):
    people = []
    for i in os.listdir(DIR + '/train'):
        people.append(i)

    features = []
    labels = []
    haar_cascade = cv.CascadeClassifier(DIR + '/haar_face.xml')

    def createTrain():
        for person in people:
            path = os.path.join(DIR + '/train', person)
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

    face_recognizer.save(DIR + '/face_trained.yml')
    np.save(DIR + '/features.npy', features)
    np.save(DIR + '/labels.npy', labels)
