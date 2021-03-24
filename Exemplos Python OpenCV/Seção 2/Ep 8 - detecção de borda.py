#pylint: disable=no-member

import cv2 as cv
import numpy as np

img = cv.imread(filename='../Resources/Photos/park.jpg')
cv.imshow(winname='Park', mat=img)

gray = cv.cvtColor(src=img, code=cv.COLOR_BGR2GRAY)
cv.imshow(winname='Gray', mat=gray)

# Utilizando o Laplacian
lap = cv.Laplacian(src=gray, ddeph=cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow(winname='Laplacian', mat=lap)

# Utilizando o Sobel 
sobelx = cv.Sobel(src=gray, ddeph=cv.CV_64F, dx=1, dy=0)
sobely = cv.Sobel(src=gray, ddeph=cv.CV_64F, dx=0, dy=1)
combined_sobel = cv.bitwise_or(src1=sobelx, src2=sobely)

# Exibindo o Sobel combinado
cv.imshow(winname='Sobel X', mat=sobelx)
cv.imshow(winname='Sobel Y', mat=sobely)
cv.imshow(winname='Combined Sobel', mat=combined_sobel)

# Utilizando a detecção de borda de Canny
canny = cv.Canny(image=gray, threshold1=150, threshold2=175)
cv.imshow(winname='Canny', mat=canny)
cv.waitKey(0)