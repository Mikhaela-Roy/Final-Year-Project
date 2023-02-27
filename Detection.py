import cv2
import numpy as np

'''APP USED IS IP CAMERA ON ANDROID. USING YOUR OWN DEVICE, CHANGE IP ADDRESS. 

#---Reference---#
#---https://karooza.net/blob-detection-and-tracking---#
#---https://learnopencv.com/blob-detection-using-opencv-python-c/---#

'''
#---Accessing the phone camera using an IP address from app---#
#---IP address for Wi-Fi connection at university---#
#video = cv2.VideoCapture('https://10.240.7.61:8080/video')
#---IP address for Wi-Fi connection at home---#
video = cv2.VideoCapture('https://192.168.0.79:8080/video')
#---Using the laptop's camera stream---#
#video = cv2.VideoCapture(0)

#---Function to detect the desired colours of the object---#
def colours(frame):
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

    final = w_mask + y_mask

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

    return final, contours

#---Detecting the centre of a circular object using contours---#
def centre(frame):
    #---Used for contouring to find the centre point of the circular object---#
    #final, contours = colours(frame)

    cnt = contours[0]
    M =  cv2.moments(cnt)

    if M["m00"] != 0:
        cx = int(M['m10']/M['m00'])
        cy = int(M['m01']/M['m00'])
    else:
        cx,xy = 0,0

    (cx,cy), radius = cv2.minEnclosingCircle(cnt)
    center  = (int(cx), int(cy))
    radius = int(radius)
    print("Radius", radius)
    print("Center", center)
    
    cv2.circle(frame, center, radius, (0,0,255), 2)
    #cv2.putText(frame, 'center', center, cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)
    #cv2.putText(frame, 'radius', (5,100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)
    #cv2.drawContours(frame, contours, -1,(0,255,0),-1)

while True:
    #---Capturing the video frame-by-frame---#
    check, frame = video.read()
    #---Calling the function to run whilst passing through a parameter---#
    final = colours(frame)
    #---When a circular ball is detected, find the contour---#

    #---Find the contour of the specified object---#
    centre(frame)
    #cv2.imshow("Camera Feed", frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
video.release()
cv2.destroyAllWindows()
