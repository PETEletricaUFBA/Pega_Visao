#pylint:disable=no-member

import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype='uint8')
cv.imshow('Blank', blank)

# 1. Paint the image a certain colour
blank[200:300, 300:400] = 0,255,0 #Todas as funções do OPENCV seguem o esquema BGR (blue,green.red)
cv.imshow('Green', blank)

# 2. Draw a Rectangle
cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0,255,0), thickness=0) #(img de desenho, (ponto inicial), (ponto final), (cor), grossura da "borda")
cv.imshow('Rectangle', blank)

# 3. Draw A circle
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0,0,255), thickness=-1) #(img de desenho, (ponto inicial), raio, (cor), grossura da "borda")
cv.imshow('Circle', blank)

# 4. Draw a line
cv.line(blank, (100,250), (300,400), (255,255,255), thickness=3) #(img de desenho, (ponto inicial), (ponto final), (cor), grossura da "borda")
cv.imshow('Line', blank)

# 5. Write text
cv.putText(blank, 'Hello, my name is [REDACTED]!!!', (0,225), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,0,255), 2) #(img de desenho, 'TEXTO', (ponto inicial), cv.fonte, (cor), grossura da "borda")
cv.imshow('Text', blank)

cv.waitKey(0)
