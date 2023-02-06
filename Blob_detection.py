import cv2
import time
import numpy as np

#---Accessing the phone camera---#
#video = cv2.VideoCapture('https://10.240.7.61:8080/video')
video = cv2.VideoCapture(0)
#---Removing the backgorund of the environment---#
subtractor = cv2.createBackgroundSubtractorMOG2(history=100,varThreshold=50,detectShadows=True)
#---Setting up the detector with default parameters---#
detector = cv2.SimpleBlobDetector()

#---Detects blob---#
#keypoints = detector.detect(video)
#---Draw the detected blobs as red circles---#
#blank = np.zeros((1,1))
#blobs = cv2.drawKeypoints(video, keypoints, blank(0,255,255),cv2.DRAW_,MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

#---AFTER DETECTING BLOBS IN THE ENVIRONMENT
#---FILTER THE BLOBS BY COLOUR, SIZE AND SHAPE
#---TO DO THIS SET THE PARAMETERS

#---Setup SimpleBlobDetector paramters---#
#params = cv2.SimpleBlobDetector_Params()
#---Change Threshold---#
##params.minThreshold = 10
##params.maxThreshold = 200
###---Filtering by parameters---#
##params.filterByArea = True
##params.minArea = 1500
###---Filter by Circularity---#
##params.filterByCircularity = True
##params.minCircularity = 0.1
###---Filter by Convexity---#
##params.filterByConvexity = True
##params.minConvexity = 0.07
###---Filter by Inertia---#
##params.filterByInertia = True
##params.minInertiaRatio = 0.01

'''
YELLOW
LH = 20
LS = 120
LV = 120
UH = 49
US =255
UV = 255
'''

'''
RED
LH =
LS =
LV =
UH =
US =
UV =
'''

while (1):
    check, frame = video.read()
    #---Removes the background of the environment---#
    rm_back = subtractor.apply(frame)
    #---Defines the colours---#
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    l_yellow = np.array([20,120,120])
    u_yellow = np.array([49,255,255])
    l_red = np.array([110,50,50])
    u_red = np.array([130,255,255])
    l_green = np.array([50,20,20])
    u_green = np.array([100,255,255])

    #---
    yellow = cv2.inRange(hsv, l_yellow,u_yellow)
    red = cv2.inRange(hsv,l_red,u_red)
    green = cv2.inRange(hsv,l_green, u_green)

    full_colours = yellow + red + green
    final = cv2.bitwise_and(frame,frame,mask=full_colours)

    kernel = np.ones((3,3),np.uint8)

    mask = cv2.morphologyEx(final,cv2.MORPH_CLOSE,kernel)
    mask = cv2.morphologyEx(final,cv2.MORPH_OPEN,kernel)

    #---Adding contours in the video stream---#
    contours, hierarchy = cv2.findContours(final.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    output = cv2.drawContours(final, contours, -1, (0,0,255),3)
    
    #---Create a detector with parameters---#

    #cv2.imshow("Camera Feed", mask)
    cv2.imshow("Mask Feed", output)
   # cv2.imshow("Coloured Feed", edges)
    
    key = cv2.waitKey(30)
    if key == 27:
        break
    
video.release()
cv2.destroyAllWindows()
