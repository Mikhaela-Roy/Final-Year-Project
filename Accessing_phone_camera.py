import cv2
import time

video = cv2.VideoCapture(0)
address = "https://10.240.7.61:8080/video"
video.open(address)

while True:
    check, frame = video.read()
    cv2.imshow("Phone Camera", frame)

    key = cv2.waitKey(1)
    
video.release()
cv2.destroyAllWindows()
