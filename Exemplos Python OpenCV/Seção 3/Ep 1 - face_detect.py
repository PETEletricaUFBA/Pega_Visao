import cv2 as cv

img = cv.imread('Exemplos Python OpenCV/Resources/Photos/group 2.jpg')
cv.imshow('IMG', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

haar_cascade = cv.CascadeClassifier('Exemplos Python OpenCV/Seção 3/haar_face.xml')

faces_rect = haar_cascade.detectMultiScale(gray,scaleFactor=1.1, minNeighbors=3)

print(f'Number of faces found = {len(faces_rect)}')

for (x,y,w,h) in faces_rect:
    cv.rectangle(img, (x,y), (x+w, y+h), (0, 0, 255), thickness=2)
cv.imshow('IMG', img)

cv.waitKey(0)