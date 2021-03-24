# pylint: disable=no-member

import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread(filename='opencv-course-master/Resources/Photos/park.jpg')
cv.imshow(winname='Park', mat=img)

# A função plt.imshow() esperaa uma imagem em RGB. Já o cv2.imshow() espera uma imagem BGR.
#plt.imshow(X=img)
#plt.show()

# BGR para Escala de Cinza
gray = cv.cvtColor(src=img, code=cv.COLOR_BGR2GRAY)
cv.imshow(winname='Escala de cinza', mat=gray)

# BGR para HSV
hsv = cv.cvtColor(src=img, code=cv.COLOR_BGR2HSV)
cv.imshow(winname='HSV', mat=hsv)

# BGR para L*a*b
lab = cv.cvtColor(src=img, code=cv.COLOR_BGR2LAB)
cv.imshow(winname='LAB', mat=lab)

# BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow(winname='RGB', mat=rgb)

# HSV to BGR
lab_bgr = cv.cvtColor(lab, cv.COLOR_LAB2BGR)
cv.imshow(winname='LAB para BGR', mat=lab_bgr)

cv.waitKey(0)
