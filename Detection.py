import cv2
import numpy as np

#---Accessing the phone camera---#
#video = cv2.VideoCapture('https://192.168.0.79:8080/video')
video = cv2.VideoCapture(0)

def parameters():
    #Initialising parameters
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
    params.maxArea = 80000

    #Create the parameters
    detector = cv2.SimpleBlobDetector_create(params)

    return detector

def colours(frame):
    #Colour Threshold 
    y_min = (20,120,120)
    y_max = (49,255,255)
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    r_min = (170,50,50)
    r_max = (180,255,255)
    rhsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    
    mask = cv2.inRange(hsv,y_min,y_max)
    r_mask = cv2.inRange(hsv, r_min, r_max)

    final = mask + r_mask

    return final

def centre(frame):
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray,(5,5), cv2.BORDER_DEFAULT)
    ret, thresh = cv2.threshold(blur, 200,255, cv2.THRESH_BINARY_INV)
    contours,hierarchy = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    blank = np.zeros(thresh.shape[:2], dtype = 'uint8')
    cv2.drawContours(blank, contours, -1,(255,0,0),1)
    for i in contours:
        M = cv2.moments(i)
        if M['m00'] != 0:
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])
            cv2.drawContours(frame, [i], -1, (0, 255, 0), 2)
            cv2.circle(frame, (cx, cy), 7, (0, 0, 255), -1)
            cv2.putText(frame, "center", (cx - 20, cy - 20),
                       cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
        print(f"x: {cx} y: {cy}")
        
while True:
    #Initialising video stream
    check, frame = video.read()

    detector =  parameters()
    final = colours(frame)
    #centre(frame)
    
    #To highlight the blobs detected
    reverse = 255 - final

    keypoints = detector.detect(reverse)
    count = len(keypoints)
    text = "Count: " + str(count)
    
    vid_keypoints = cv2.drawKeypoints(frame, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    cv2.putText(vid_keypoints, text, (5,25),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
    
    #cv2.imshow("Camera Feed", frame)
    cv2.imshow("Keypoints", vid_keypoints)


    cv2.waitKey(0)
    
video.release()
cv2.destroyAllWindows()
