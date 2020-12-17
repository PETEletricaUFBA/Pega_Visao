#pylint:disable=no-member

import cv2 as cv

img = cv.imread('Material de estudo/Resources/Photos/cat_large.jpg')

cv.imshow('Cat', img)

#Função de resdimesionamento
def rescaleFrame(frame, scale=0.75):#o objeto frame tem alguns valores associados a ele, notoriamente, frame.shape[0] indica a largura do objeto e frame[1] indica a altura.
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)# o método de interpolação altera o modo que o python realiza o redmensionamento
                                                                    # use INTER_LINEAR ou INTER_CUBIC caso queira aumentar a imagem com um melhor resultado
                                                                    # use INTER_AREA caso queira diminuir a imagem com um melhor resultado
resized = rescaleFrame(img, scale=0.25)

cv.imshow ('Resized', resized)

capture = cv.VideoCapture('Videos/dog.mp4')#segue o mesmo esquema do objeto frame

def changeRes(width, height):
    capture.set(3, width)
    capture.set(4, height)

while True:
    isTrue, frame = capture.read()
    
    frameResized = rescaleFrame(frame, 0.75)
    
    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frameResized)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows


cv.waitKey(0)

