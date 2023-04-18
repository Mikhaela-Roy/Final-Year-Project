#!/usr/bin/env python3
import cv2
import numpy as np
import serial
import time
import imutils
import sys
import argparse
from collections import deque
from imutils.video import VideoStream

#Reference
#https://pyimagesearch.com/2015/09/14/ball-tracking-with-opencv/

video = cv2.VideoCapture(0)
arduino = serial.Serial('COM4', 9600)

def arguments():
    ap = argparse.ArgumentParser()
    ap.add_argument("-b", "--buffer", type=int, default=64,
            help="max buffer size")
    args = vars(ap.parse_args())
    pts = deque(maxlen=args['buffer'])

    return pts

def  colour_contouring(frame, pts):

    blur = cv2.GaussianBlur(frame, (11,11), 0)
    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    thresh = cv2.threshold(frame, 175, 255, cv2.THRESH_BINARY)[1]
    
    y_min = (23,50,20)
    y_max = (50,255,255)
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    g_min = (29, 86, 6)
    g_max = (64, 255, 255)
    g_hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    y_mask = cv2.inRange(hsv, y_min,y_max)
    g_mask = cv2.inRange(g_hsv, g_min, g_max)

    final = y_mask + g_mask

    mask = cv2.erode(final, None, iterations=2)
    mask = cv2.dilate(final, None, iterations=2)
    
    contours = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours = imutils.grab_contours(contours)
    center = None

    for cnt in contours:
        perimeter = cv2.arcLength(cnt, True)
        area = cv2.contourArea(cnt)
        
        c = max(contours, key = cv2.contourArea)
        ((x, y), radius) = cv2.minEnclosingCircle(c)
        x, y = (x,y)
        
        #Checks the x value on the frame and sends a command yo arduino to control motors. 
        if x > 360:
            print('left')
            cmd = "left"
            #time.sleep(0.1)
            #arduino.write(cmd.encode()) 
        elif x < 340:
            print('right')
            cmd = "right"
            #time.sleep(0.1)
            #arduino.write(cmd.encode())
        elif x  >= 350 or x <= 360:
            print('centre')
            cmd = "straight"
            #time.sleep(0.1)
            
        time.sleep(0.1)
        cmd = cmd +'\r'
        arduino.write(cmd.encode())
            
        
        
        M = cv2.moments(c)
        center = (int(M['m10']/M['m00']), int(M['m01']/M['m00']))

        if radius > 3:
            cv2.circle(frame, (int(x), int(y)), int(radius), (0, 255, 255), 2)
            text = "X: " + str(int(x)) + " Y: " + str(int(y))
            cv2.putText(frame, text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
            cv2.circle(frame, center, 5, (0,0,255), -1)
            #count = np.sum(np.where(thresh == final))
            #print('count = ', count)
           
                
        pts.appendleft(center)

while True:
    ret, frame = video.read()
    pts = arguments()
    colour_contouring(frame, pts)

    
    
    cv2.imshow('Camera', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'): break

video.release()
cv2.destroyAllWindows()
