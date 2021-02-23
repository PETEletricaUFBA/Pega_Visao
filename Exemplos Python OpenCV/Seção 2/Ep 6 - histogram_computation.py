import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread('Exemplos Python OpenCV/Resources/Photos/cats.jpg')
cv.imshow('IMG', img)

blank = np.zeros(img.shape[:2], dtype='uint8')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

circle = cv.circle(blank, (img.shape[1]//2,img.shape[0]//2), 100, 255, -1)
cv.imshow('Circle', circle)

greyMask = cv.bitwise_and(gray,gray, mask=circle)
cv.imshow('Grey Masked', greyMask)

colorMask = cv.bitwise_and(img,img, mask=circle)
cv.imshow('Color Masked', colorMask)

# Grayscale histogram
gray_hist = cv.calcHist([gray], [0], greyMask, [256], [0, 256])

plt.figure(1)
plt.title('Grayscale Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
plt.plot(gray_hist)
plt.xlim([0,256])
# plt.show()

# Color histogram
plt.figure(2)
plt.title('Color Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
colors = ('b', 'g', 'r')
for i,col in enumerate(colors):
    hist = cv.calcHist([img], [i], None, [256], [0, 256])
    plt.plot(hist, color=col)
    plt.xlim([0,256])


plt.show()


cv.waitKey(0)