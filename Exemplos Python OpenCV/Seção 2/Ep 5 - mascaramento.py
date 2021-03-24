#pylint: disable=no-member

import cv2 as cv
import numpy as np

# Carrega uma imagem e a exibe
img = cv.imread(filename='opencv-course-master\Resources\Photos\cats.jpg')
cv.imshow(winname='Gatinhos', mat=img)

# Cria uma imagem vazia e a exibe
blank = np.zeros(shape=(img.shape[0],img.shape[1]), dtype='uint8')
cv.imshow(winname='Imagem Vazia', mat=blank)

# Cria um objeto circular branco em uma imagem vazia
circle = cv.circle(img=blank.copy(), center=(img.shape[1]//2 + 40, img.shape[0]//2), radius=100, color=255, thickness=-1)

# Cria um objeto retangular branco em uma imagem vazia
rectangle = cv.rectangle(img=blank.copy(), pt1=(30,30), pt2=(370,370), color=255, thickness=-1)

# Realiza uma operação bit a bit “and” entre “circle” e “rectangle” # e a exibe
weird_shape = cv.bitwise_and(src1=circle, src2=rectangle)
cv.imshow(winname='Mascaramento', mat=weird_shape)

# Cria uma máscara através operação bit a bit “and” com a imagem carregada inicialmente e a forma criada “weird_shape”
masked = cv.bitwise_and(src1=img, src2=img, mask=weird_shape)
cv.imshow(winname='Imagem Mascarada com o Mascaramento', mat=masked)

cv.waitKey(0)