#pylint:disable=no-member

import cv2 as cv
import numpy as np

img = cv.imread('Material de estudo/Resources/Photos/cats.jpg')
cv.imshow('Cats', img)

blank = np.zeros(img.shape, dtype='uint8')
cv.imshow('Blank', blank)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY) # colocando em preto-branco
cv.imshow('Gray', gray)

#blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT) # se vc usar o borramento o número de contornos tende a cair, pq vc "eliminou" algumas bordas
#cv.imshow('Blur', blur)

canny = cv.Canny(img, 125, 175) # descobrindo as "bordas"(edges)
cv.imshow('Canny Edges', canny)

# ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY) # binarização da imagem (branco=1/preto=0)
# cv.imshow('Thresh', thresh)

contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE) # contornos, hierarquia (entre os contornos) = (função borda, cv.metodo de retorno, cv.metodo de aproximação)
print(f'{len(contours)} contour(s) found!')

cv.drawContours(blank, contours, -1, (255,255,255), 1) # desenho dos contornos da imagem
cv.imshow('Contours Drawn', blank)

cv.waitKey(0)
