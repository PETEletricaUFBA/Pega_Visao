import cv2
from time import sleep
key = cv2. waitKey(1)
webcam = cv2.VideoCapture(0)
haar = cv2.CascadeClassifier('Aplicações/haar_cascade.xml')
sleep(2)

while True:
    try:
        check, frame = webcam.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces_detected = haar.detectMultiScale(gray, scaleFactor=1.1 , minNeighbors= 5)
        for (x,y,a,b) in faces_detected:
            cv2.rectangle(frame, (x,y), (x+a,y+b), (0,255,0), thickness=2)
        cv2.imshow("Detected Face", frame)

        key = cv2.waitKey(1)

        if key == ord('q'):
            webcam.release()
            cv2.destroyAllWindows()
            break

    except(KeyboardInterrupt):
        webcam.release()
        print("Program ended.")
        cv2.destroyAllWindows()
        break
