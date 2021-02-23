import cv2 as cv
import numpy as np

img = cv.imread('Exemplos Python OpenCV/Resources/Photos/park.jpg')
cv.imshow('IMG', img)

blank = np.zeros(img.shape[:2], dtype='uint8')

b, g, r = cv.split(img)

cv.imshow('Blue', b)
blueMerged = cv.merge([b, blank, blank])
cv.imshow('Blue merged', blueMerged)

cv.imshow('Green', g)
greenMerged = cv.merge([blank, g, blank])
cv.imshow('Green merged', greenMerged)

cv.imshow('Red', r)
redMerged = cv.merge([blank, blank, r])
cv.imshow('Red merged', redMerged)

merged = cv.merge([b,g,r])
cv.imshow('Merged', merged)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)
print(merged.shape)

cv.waitKey(0)