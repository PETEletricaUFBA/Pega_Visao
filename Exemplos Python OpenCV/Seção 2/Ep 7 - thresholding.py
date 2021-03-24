#pylint:disable=no-member

import cv2 as cv

# Carregando uma imagem
img = cv.imread(filename='opencv-course-master\Resources\Photos\cats.jpg')
cv.imshow(winname='Gatinhos', mat=img)

# Convertendo BGR para Escala de cinza
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow(winname='Escala de cinza', mat=gray)

# Thresholding simples
threshold, thresh = cv.threshold(src=gray, thresh=150, maxval=255, type=cv.THRESH_BINARY )
cv.imshow(winname='Thresholded Simples', mat=thresh)

threshold, thresh_inv = cv.threshold(src=gray, thresh=150, maxval=255, type=cv.THRESH_BINARY_INV )
cv.imshow(winname='Thresholded Simples Inverso', mat=thresh_inv)

# Thresholding adaptativo5
adaptive_thresh = cv.adaptiveThreshold(src=gray, maxValue=255, adaptiveMethod=cv.ADAPTIVE_THRESH_GAUSSIAN_C, thresholdType=cv.THRESH_BINARY_INV, blockSize=11, C=9)
cv.imshow(winname='Thresholding Adaptativo', mat=adaptive_thresh)

cv.waitKey(0)