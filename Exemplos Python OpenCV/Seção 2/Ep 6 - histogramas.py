#pylint:disable=no-member

import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

# Carregando e exibindo uma imagem
img = cv.imread('opencv-course-master/Resources/Photos/park.jpg')
cv.imshow('Parque',img)

# Criando uma imagem vazia do tamanho da imagem carregada
blank = np.zeros(shape=(img.shape[0],img.shape[1]), dtype='uint8')

# Convertendo a imagem para Escala de cinza
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)

# Criando um círculo numa imagem vazia
mask = cv.circle(img=blank,center=(img.shape[1]//2,img.shape[0]//2), radius=100, color=255, thickness=-1)

# Criando uma máscara utilizando o círculo criado como forma
masked = cv.bitwise_and(src1=img,src2=img,mask=mask)
cv.imshow(winname='Mask', mat=masked)

# GRayscale histogram
# gray_hist = cv.calcHist([gray], [0], mask, [256], [0,256] )

# plt.figure()
# plt.title('Grayscale Histogram')
# plt.xlabel('Bins')
# plt.ylabel('# of pixels')
# plt.plot(gray_hist)
# plt.xlim([0,256])
# plt.show()

# Plotando o histograma de cores
plt.figure()
plt.title(label='Colour Histogram')
plt.xlabel(xlabel='Bins')
plt.ylabel(ylabel='# of pixels')
colors = ('b', 'g', 'r')
for i,col in enumerate(colors):
    hist = cv.calcHist(images=[img], channels=[i], mask=mask, histSize=[256], ranges=[0,256])
    plt.plot(hist, color=col)
    plt.xlim([0,256])

# Exibindo o plot
plt.show()

cv.waitKey(0)