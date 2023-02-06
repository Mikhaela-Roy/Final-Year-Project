import cv2
import time
import numpy as np

#---Accessing the phone camera---#
cap = cv2.VideoCapture('https://10.240.7.61:8080/video')
#---Removing the backgorund of the environment---#
subtractor = cv2.createBackgroundSubtractorMOG2(history=100,varThreshold=50,detectShadows=True)
#---Setting up the detector with default parameters---#
detector = cv2.SimpleBlobDetector()
###----------------------Function to threshold colour values in HSV space

####----------------------Variable Decleration
###-----------Color decleration in BGR space beig used to conver into hsv
#Color range begining
blue = [204 ,102, 0]#Working
red = [5, 0, 255]# Working on white background
green = [0, 255, 102]#Working
yellow = [0, 255, 255]# Working 
black = [0,0,0]#?

def get_limits(color):
    # insert the bgr values that you want to convert into hsv
    c = np.uint8([[color]])  
    hsvC = cv2.cvtColor(c, cv2.COLOR_BGR2HSV)

    ###Declare the thresholds for the colour conversions 
    lowerLimit = hsvC[0][0][0] - 10, 100, 100 
    upperLimit = hsvC[0][0][0] + 10, 255, 255

    #Convert into numpy array
    lowerLimit = np.array(lowerLimit, dtype = np.uint8)
    upperLimit = np.array(upperLimit, dtype = np.uint8)

    return lowerLimit, upperLimit

while True:
    ###---CAPTURE AND SHOW FRAME---###
    ret, frame = cap.read()
    #Converting the BGR image into a HSV one 
    hsvImage = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    lowerLimitg, upperLimitg = get_limits(color = green)
    lowerLimity, upperLimity = get_limits(color = yellow)
    lowerLimitb, upperLimitb = get_limits(color = blue)
    lowerLimitr, upperLimitr = get_limits(color = red)
    lowerLimitw, upperLimitw = get_limits(color = black)
    
    #Create a mask for the detected colors
    mask_gr = cv2.inRange(hsvImage ,lowerLimitg, upperLimitg)
    mask_ye = cv2.inRange(hsvImage ,lowerLimity, upperLimity)
    mask_bl = cv2.inRange(hsvImage ,lowerLimitb, upperLimitb)
    mask_red = cv2.inRange(hsvImage ,lowerLimitr, upperLimitr)
    mask_wild = cv2.inRange(hsvImage ,lowerLimitw, upperLimitw)

    #Declare mask variables
    mask_g = cap.fromarray(mask_gr)
    mask_y = cap.fromarray(mask_ye)
    mask_b = cap.fromarray(mask_bl)
    mask_r = cap.fromarray(mask_red)
    mask_w = cap.fromarray(mask_wild)

    #Declare individual bounding boxes 
    bbox_gr = mask_g.getbbox()
    bbox_ye = mask_y.getbbox()
    bbox_bl = mask_b.getbbox()
    bbox_red = mask_r.getbbox()
    bbox_wild = mask_w.getbbox()

    #Tests to see if colors are being detected
    #print("Green",bbox_gr)
    #print("Yellow",bbox_ye)
    #print("Blue",bbox_bl)
    #print("Red",bbox_red)
    #print("Red",bbox_wild)

    #BBox only appears if a particular colour is detected or if they are all detected 
    #Green
    
    if bbox_gr is not None:
        x1,y1,x2,y2 = bbox_gr

        frame = cv2.rectangle(frame, (x1, y1),(x2, y2), (0, 255, 0), 3)
        cv2.putText(frame, 'Green', (x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2 )
        roi_gr = frame[y1:y2, x1:x2]
        cv2.imshow('Green Cropped', roi_gr)

    #Yellow
    elif bbox_ye is not None:
        x1,y1,x2,y2 = bbox_ye

        frame = cv2.rectangle(frame, (x1, y1),(x2, y2), (0, 255, 255), 3)
        cv2.putText(frame, 'Yellow', (x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 255), 2 )
        roi_ye = frame[y1:y2, x1:x2]
        cv2.imshow('Yellow Cropped', roi_ye)

    #Blue
    elif bbox_bl is not None:
        x1,y1,x2,y2 = bbox_bl

        frame = cv2.rectangle(frame, (x1, y1),(x2, y2), (255, 0, 0), 3)
        cv2.putText(frame, 'Blue', (x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2 )
        roi_bl = frame[y1:y2, x1:x2]
        cv2.imshow('Blue Cropped', roi_bl)
    
    #Red
    elif bbox_red is not None:
        x1,y1,x2,y2 = bbox_red

        frame = cv2.rectangle(frame, (x1, y1),(x2, y2), (0, 0, 255), 3)
        cv2.putText(frame, 'Red', (x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2 )
        roi_red = frame[y1:y2, x1:x2]
        cv2.imshow('Red Cropped', roi_red)
