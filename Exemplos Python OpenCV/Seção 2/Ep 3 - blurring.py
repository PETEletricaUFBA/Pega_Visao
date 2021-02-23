import cv2 as cv

img = cv.imread('Exemplos Python OpenCV/Resources/Photos/cats.jpg')
cv.imshow('IMG', img)

#  Averaging (Media)
average = cv.blur(img,(7,7))
cv.imshow('Average Blur', average)

# Gaussian Blur
gaussian = cv.GaussianBlur(img, (7,7), 0)
cv.imshow('Gaussian Blur', gaussian)

# Median (Mediana)
median = cv.medianBlur(img, 7)
cv.imshow('Median Blur', median)

# Bilateral
bilateral = cv.bilateralFilter(img, 10, 35, 35)
cv.imshow('Bilateral Blur', bilateral)

cv.waitKey(0)