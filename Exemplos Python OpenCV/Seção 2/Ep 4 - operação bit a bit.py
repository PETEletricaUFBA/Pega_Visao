#pylint: disable=no-member

import cv2 as cv
import numpy as np

# Cria uma imagem vazia
blank = np.zeros(shape=(400,400), dtype='uint8')

# Cria um objeto retangular branco em uma imagem vazia
rectangle = cv.rectangle(img=blank.copy(), pt1=(30,30), pt2=(370,370), color=255, thickness=-1)

# Cria um objeto circular branco em uma imagem vazia
circle = cv.circle(img=blank.copy(), center=(200,200), radius=200, color=255, thickness=-1)

# Exibe as duas imagens criadas
cv.imshow(winname='Retangulo', mat=rectangle)
cv.imshow(winname='Circulo', mat=circle)

# bitwise AND --> intersecta as regiões
bitwise_and = cv.bitwise_and(src1=rectangle, src2=circle)
cv.imshow(winname='Bitwise AND', mat=bitwise_and)

# bitwise OR --> União das regiões
bitwise_or = cv.bitwise_or(src1=rectangle, src2=circle)
cv.imshow(winname='Bitwise OR', mat=bitwise_or)

# bitwise XOR --> Regiões não intesectadas
bitwise_xor = cv.bitwise_xor(src1=rectangle, src2=circle)
cv.imshow(winname='Bitwise XOR', mat=bitwise_xor)

# bitwise NOT --> Região não preenchida
bitwise_not = cv.bitwise_not(src=circle)
cv.imshow(winname='Circle NOT', mat=bitwise_not)


cv.waitKey(0)