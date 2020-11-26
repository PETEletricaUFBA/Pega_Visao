#pylint:disable=no-member

import cv2 as cv

img = cv.imread('Photos/cat_large.jpg')

cv.imshow('Cat', img)

def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

resized = rescaleFrame(img, scale=0.25)

cv.imshow ('Resized', resized)

capture = cv.VideoCapture('Videos/dog.mp4')

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

