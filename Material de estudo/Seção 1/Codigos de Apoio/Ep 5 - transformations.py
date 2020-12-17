#pylint:disable=no-member

import cv2 as cv
import numpy as np

img = cv.imread('Photos/park.jpg')
cv.imshow('Park', img)

# para fazer transformações deveremos criar algumas funções a parte a biblioteca

#Translação
def translate(img,x,-y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1], img.shape[0]) # img.shape[1] = largura img.shap[0] = altura
    return cv.warpAffine(img,transMat,dimensions)
# x --> direita
# -x --> esquerda
# y --> acima
# -y --> abaixo
# vale notar que o deslocamento na verdade é uma adição de pixels em brano a imagem
translated = translate(img, -100, 100)
cv.imshow('Translated', translated)

#Rotação
def rotate(img,angle,rotPoint=None):
    (altura,largura) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (largura//2,altura//2)#centro da imagem

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)# esse 1.0 indica se queremos aumentar a imagem dps da rotação
    dimensions = (largura,altura)

    return cv.warpAffine(img,rotMat,dimensions)
# a rotação acontece no sentido anti-horário para valores positivos
rotated = rotate(img, -45)
cv.imshow('Rotated', rotated)

rotated_rotated = rotate(img, -90)
cv.imshow('Rotated Rotated', rotated_rotated)

# Resizing/Redimensionar igual ao arquivo resize.py
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)

# Flip/espelhamento
flip = cv.flip(img, 0)
cv.imshow('Flip', flip)
# 0 = espelha imagem em torno do eixo x
# 1 = espelha em torno do eixo y
# -1 = espelha em torno de ambos os eixos

# Cropping/Corte
cropped = img[200:400, 300:400] #indique os pontos onde deseja cortar a imagem
cv.imshow('Cropped', cropped)


cv.waitKey(0)
