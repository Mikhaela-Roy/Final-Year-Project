import cv2
import time
import numpy as np

#---Accessing the phone camera---#
video = cv2.VideoCapture('https://192.168.0.79:8080/video')
#---Setting the IP address of the video stream on the phone---#
params = cv2.SimpleBlobDetector_Params()
# Change thresholds
params.minThreshold = 120;
params.maxThreshold = 255;
 
# Filter by Circularity
params.filterByCircularity = False
params.minCircularity = 0.1

#Filter by Area
params.filterByArea = True
params.minArea = 400
params.maxArea = 20000

detector = cv2.SimpleBlobDetector_create(params)


while True:
    
    check, frame = video.read()
    
    hsvmin = (20,120,120)
    hsvmax = (49,255,255)
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv,hsvmin,hsvmax)

  
    #To highlight the blobs detected
    reverse = 255 - mask

    keypoints = detector.detect(reverse)
    count = len(keypoints)
    text = "Count: " + str(count)
    vid_keypoints = cv2.drawKeypoints(frame, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    cv2.putText(frame, text, (5,25),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
    cv2.imshow("Camera Feed", frame)
    cv2.imshow("Keypoints", vid_keypoints)


    cv2.waitKey(1)
    
video.release()
cv2.destroyAllWindows()
