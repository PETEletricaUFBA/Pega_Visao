import cv2
from time import sleep
key = cv2. waitKey(1)
webcam = cv2.VideoCapture(0)
sleep(2)
while True:

    try:
        check, frame = webcam.read()
        #print(check) #prints true se webcam está ativa
        #print(frame) #prints matrix de cada frame
        cv2.imshow("Capturing", frame)
        key = cv2.waitKey(1)
        if key == ord('s'):
            cv2.imwrite(filename='Aplicações/saved_img.jpg', img=frame)
            webcam.release()

            img_ = cv2.imread('Aplicações/saved_img.jpg', cv2.IMREAD_ANYCOLOR)

            gray = cv2.cvtColor(img_, cv2.COLOR_BGR2GRAY)
            img_ = cv2.resize(gray,(28,28))

            img_resized = cv2.imwrite(filename='Aplicações/saved_img-normalized.jpg', img=img_)
            print("Image saved!")

            break

        elif key == ord('q'):
            webcam.release()
            cv2.destroyAllWindows()
            break

    except(KeyboardInterrupt):
        webcam.release()
        print("Program ended.")
        cv2.destroyAllWindows()
        break
