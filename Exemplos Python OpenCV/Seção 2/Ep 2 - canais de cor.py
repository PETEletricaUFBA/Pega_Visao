# pylint: disable=no-member

import numpy as np
import cv2 as cv

img = cv.imread(filename='opencv-course-master/Resources/Photos/park.jpg')
cv.imshow(winname='Parque', mat=img)

blank = np.zeros(shape=img.shape[:2], dtype='uint8')

# Utilizamos o cv.split para conseguir obter cada imagens em escala de cinza de cada cor separadamente 
b,g,r = cv.split(img)

# O cv.merge serve para unir imagens. Neste caso estamos unindo nossa imagem Azul em Escala de cinza com duas outras imagens vazias.
blue = cv.merge([b, blank, blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])

cv.imshow(winname='Azul', mat=blue)
cv.imshow(winname='Verde', mat=green)
cv.imshow(winname='Vermelho', mat=red)

merged = cv.merge([b,g,r])
cv.imshow(winname='Junção BGR', mat=merged)

print("Shape da imagem: ", img.shape)
print("Blue Shape: ", b.shape)
print("Green Shape: ", g.shape)
print("Red Shape: ", r.shape)

cv.waitKey(0)