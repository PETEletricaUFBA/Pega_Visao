import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('Exemplos Python OpenCV/Resources/Photos/park.jpg')
cv.imshow('IMG', img)

rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB', rgb)

plt.imshow(rgb)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)

lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('LAB', lab)

plt.show()
cv.waitKey(0)