import os
import datetime 
import cv2

persone = 'example'
imgDIRe = ''
DIRe = r'Resources/Faces'#alterar o caminho se necessário

def sign_up(person, imgDIR, DIR):
    if (not (os.path.exists(DIR + person))):
        os.mkdir(DIR + person)

    img = cv2.imread(imgDIR)

    now = datetime.now()
    date_time = now.strftime("%Y%m%d-%H%M%S")

    cv2.imwrite(filename=DIR + '/train/' + f'{date_time}-{person}-SU.jpg', img=img)
