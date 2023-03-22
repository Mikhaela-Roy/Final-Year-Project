import cv2
import numpy as np
from PIL import Image
import serial
import time

video = cv2.VideoCapture(0)
#arduino = serial.Serial('COM3', '9600', timeout = 2)

def blob_detection():
    # Set our filtering parameters
    # Initialize parameter setting using cv2.SimpleBlobDetector
    params = cv2.SimpleBlobDetector_Params()

    # Set Area filtering parameters
    params.filterByArea = True
    params.minArea = 400
    params.maxArea = 80000

    # Set Circularity filtering parameters
    params.filterByCircularity = True
    params.minCircularity = 0.9
     
    # Set Convexity filtering parameters
    params.filterByConvexity = True
    params.minConvexity = 0.2
            
    # Set inertia filtering parameters
    params.filterByInertia = True
    params.minInertiaRatio = 0.01

    # Create a detector with the parameters
    detector = cv2.SimpleBlobDetector_create(params)

    return detector

def colour_detection(frame):
    blur = cv2.GaussianBlur(frame, (11,11), 0)
    
    y_min = (23,50,20)
    y_max = (50,255,255)
    hsv = cv2.cvtColor(blur,cv2.COLOR_BGR2HSV)

    y_mask = cv2.inRange(hsv, y_min,y_max)

    g_min = (29, 86, 6)
    g_max = (64, 255, 255)
    g_hsv = cv2.cvtColor(blur,cv2.COLOR_BGR2HSV)
    
    g_mask = cv2.inRange(g_hsv, g_min, g_max)

    final = y_mask + g_mask
    
    return final

while True:
    ret, frame = video.read()
    
    final = colour_detection(frame)
    
    detector = blob_detection()
    reverse = 255 - final
    # Detect blobs
    keypoints = detector.detect(reverse)

    # Draw blobs on our image as red circles
    blobs = cv2.drawKeypoints(frame, keypoints, np.array([]), (0, 0, 255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

    number_of_blobs = len(keypoints)
    text = "Number of Circular Blobs: " + str(len(keypoints))
    cv2.putText(blobs, text, (20, 550), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 100, 255), 2)

    # Show blobs
    cv2.imshow("Filtering Circular Blobs Only", blobs)
    if cv2.waitKey(1) & 0xFF == ord('q'): break

video.release()
cv2.destroyAllWindows()
