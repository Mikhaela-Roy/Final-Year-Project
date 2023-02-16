import cv2
import numpy as np

#---Reference---#
#---https://karooza.net/blob-detection-and-tracking---#
#---https://learnopencv.com/blob-detection-using-opencv-python-c/---#
#---https://www.youtube.com/watch?v=RaCwLrKuS1w---#

#---Accessing the phone camera using an IP address from app at university---#
video = cv2.VideoCapture('https://10.240.7.61:8080/video')
#---Accesing the phone camera using an IP address from app at home---#
#video = cv2.VideoCapture('https://192.

#
previous = None
#
distance = lambda x1, y1, x2, y2: (x1-x2)**2+(y1-y2)**2

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

    #
    y_mask = cv2.inRange(hsv, y_min,y_max)
    r_mask = cv2.inRange(rhsv, r_min, r_max)
    p_mask = cv2.inRange(phsv, p_min, p_max)

    #Combining the colours to be detected
    final = y_mask + r_mask + p_mask

    return final

while True:
    ret, frame = video.read()

    #final = colours(frame)

    if not ret: break
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (17,17), 0)

    circles = cv2.HoughCircles(blur, cv2.HOUGH_GRADIENT, 1.2,100, param1 = 100, param2 = 30,
                               minRadius = 75, maxRadius = 400)

    if circles is not None:
        circles = np.uint16(np.around(circles))
        chosen = None
        for i in circles[0, :]:
            if chosen is None: chosen = i
            if previous is not None:
                if distance(chosen[0],chosen[1],previous[0],previous[1]) <= distance(i[0],i[1],previous[0],previous[1]):
                    chosen = i
                    
        cv2.circle(frame, (chosen[0],chosen[1]), 1, (0,100,100),3)
        cv2.circle(frame, (chosen[0], chosen[1]), chosen[2], (255,0,255),3)
        previous = chosen
        
    cv2.imshow('Circles', frame)
                
    if cv2.waitKey(1) & 0xFF == ord('q'): break

video.release()
cv2.destroyAllWindows()
