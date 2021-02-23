import cv2 as cv
import numpy as np

img = cv.imread('Exemplos Python OpenCV/Resources/Photos/cats 2.jpg')
cv.imshow('IMG', img)

blank = np.zeros(img.shape[:2], dtype='uint8')
cv.imshow('Blank', blank)

circle = cv.circle(blank.copy(), (img.shape[1]//2 + 45,img.shape[0]//2), 100, 255, -1)
rectangle = cv.rectangle(blank.copy(), (30,30), (370,370), 255, -1)

mask = cv.bitwise_or(circle, rectangle)
cv.imshow('Mask', mask)

# Masking a Img
masked = cv.bitwise_and(img, img, mask=mask)
cv.imshow('Masked IMG', masked)

cv.waitKey(0)