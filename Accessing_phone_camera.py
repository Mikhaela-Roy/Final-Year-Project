import cv2
import time

video = cv2.VideoCapture("https://192.168.0.79:8080/video")

while True:
    check, frame = video.read()
    cv2.imshow("Phone Camera", frame)

    key = cv2.waitKey(1)
    
video.release()
cv2.destroyAllWindows()
