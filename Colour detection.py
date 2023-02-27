#The Piano Channel 4
import cv2
import numpy as np

video = cv2.VideoCapture(0)

while True:
    
    check, frame = video.read()

    #Colour Threshold for Yellow
    y_min = (23,7,0)
    y_max = (83,255,255)
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    #Colour Threshold for Red
    r_min = (170,50,50)
    r_max = (180,255,255)
    rhsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    #Colour Threshold for Pink
    p_min = (156, 74, 76)
    p_max = (166, 255, 255)
    phsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    #Colour Threshold for White
    w_min = (0,0,168)
    w_max = (172,111,255)
    whsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    #Threhsold the HSV image to get a specific colour only
    y_mask = cv2.inRange(hsv, y_min,y_max)
    r_mask = cv2.inRange(rhsv, r_min, r_max)
    p_mask = cv2.inRange(phsv, p_min, p_max)
    w_mask =cv2.inRange(whsv, w_min, w_max)

    final = y_mask
    
    #Create a 5x5 8 bit integer matrix
    kernel = np.ones((7,7), np.uint8)
    #Removes unncessary black noises from the white region
    mask = cv2.morphologyEx(final, cv2.MORPH_CLOSE, kernel)
    #Removes white noise from the black regions of the mask
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    #Applies mask on frame in only that region where the mask is True means white
    segment = cv2.bitwise_and(frame, frame, mask = mask)
    #Find all the continous points along the boundary 
    contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    #Draws all the contour points 
    output = cv2.drawContours(frame, contours, -1, (0,0,255), 3)

    #if cv2.contourArea(contours) > 1000 and cv2.contourArea(contours) < 20000:
    cv2.imshow("Colour", output)
    #cv2.imshow('Mask', segment)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
