# pylint: disable=no-member

import cv2 as cv

img = cv.imread(filename='opencv-course-master\Resources\Photos\cats.jpg')
cv.imshow(winname='Gatinhos', mat=img)

# Borrando a imagem pela média
average = cv.blur(src=img, ksize=(7,7))
cv.imshow(winname='Average', mat=average)

# Borrando a imagem pela Gaussian Blur
gauss = cv.GaussianBlur(src=img, ksize=(7,7), sigmaX=0)
cv.imshow(winname='Gaussian Blur', mat=gauss)

# Borrando a imagem pela mediana
median = cv.medianBlur(src=img, ksize=5)
cv.imshow(winname='Mediana', mat=median)

# Bilateral
bilateral = cv.bilateralFilter(src=img, d=5, sigmaColor=15, sigmaSpace=15)
cv.imshow(winname='Bilateral', mat=bilateral)

cv.waitKey(0)