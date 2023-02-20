import cv2
import numpy as np

#---Reference---#
#---https://karooza.net/blob-detection-and-tracking---#
#---https://learnopencv.com/blob-detection-using-opencv-python-c/---#

#---Accessing the phone camera using an IP address from app---#
#---IP address for Wi-Fi connection at university---#
#video = cv2.VideoCapture('https://10.240.7.61:8080/video')
#---IP address for Wi-Fi connection at home---#
#video = cv2.VideoCapture('https://192.168.0.79:8080/video')
#---Using the laptop's camera stream---#
video = cv2.VideoCapture(0)

#---Defining the parameters for a specific blob detection---#
def parameters():
    
    #Initialising parameters
    params = cv2.SimpleBlobDetector_Params()

    #Change thresholds
    params.minThreshold = 120;
    params.maxThreshold = 255;
     
    #Filter by Circularity
    params.filterByCircularity = False
    params.minCircularity = 0.1
    
    #Filter by Area
    params.filterByArea = True
    params.minArea = 400

    #Create the parameters
    detector = cv2.SimpleBlobDetector_create(params)

    return detector

#---Function to detect the desired colours of the object---#
def colours(frame):
    
    #Colour Threshold for Yellow
    y_min = (20,120,120)
    y_max = (49,255,255)
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    #Colour Threshold for Red
    r_min = (170,50,50)
    r_max = (180,255,255)
    rhsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    #Colour Threshold for Pink
    p_min = (156, 74, 76)
    p_max = (166, 255, 255)
    phsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    y_mask = cv2.inRange(hsv, y_min,y_max)
    r_mask = cv2.inRange(rhsv, r_min, r_max)
    p_mask = cv2.inRange(phsv, p_min, p_max)

    final = y_mask + r_mask + p_mask

    return final

#---Detecting the centre of a circular object using contours---#
def centre(frame):
    #---Used for contouring to find the centre point of the circular object---#
    ret, thresh = cv2.threshold(frame, 127, 255, 0)
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    cnt = contours[0]

    cv2.drawContours(frame, contours, -1,(0,255,0),-1)
    
    M =  cv2.moments(cnts)

    cx = int(M['m10']/M['m00'])
    cy = int(M['m01']/M['m00'])

    (cx,cy), radius = cv2.minEnclosingCircle(cnt)
    center  = (int(x), int(y))
    radius = int(radius)
    
    cv2.circle(frame, center, radius, (0,0,255),2)
    cv2.putText(frame, 'Center', (cx,cy), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255))
    
    cv2.imshow('Centroid', frame)
    
while True:
    #---Capturing the video frame-by-frame---#
    check, frame = video.read()
    #---Calling the function to run whilst passing through a parameter---#
    final = colours(frame)
    detector = parameters()
    #---To highlight the blobs detected
    reverse = 255 - final
    #---
    centre(frame)
    keypoints = detector.detect(reverse)
    #---Find length---#
    count = len(keypoints)
    text = "Count: " + str(count)
    #---Draw the boundary circle of the detetced blob---#
    video_keypoints = cv2.drawKeypoints(frame, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    cv2.putText(video_keypoints, text, (5,25),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
    #---When a circular ball is detected, find the contour---#
    if count > 0:
        #---Finding the size of the object and display---#
        size = keypoints[0].size
        text = "S = " + "{:.2f}".format(size)
        cv2.putText(frame, text, (0,100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 1)
        #---Find the contour of the specified object---#
        contour_list = []
        for contour in contours:
            approx = cv2.approxPolyDP(contour,0.01*cv2.arcLength(contour,True),True)
            area = cv2.contourArea(contour)
            if ((len(approx) > 8) & (area > 30) ):
                contour_list.append(contour)
        
        cv2.drawContours(frame, contour_list, -1, (0,255,0),2)
        
    cv2.imshow("Camera Feed", frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
video.release()
cv2.destroyAllWindows()
