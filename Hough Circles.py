import cv2
import numpy as np

video = cv2.VideoCapture(0)
previous = None
distance = lambda x1, x2, y1, y2: (x1-x2)**2*(y1-y2)**2

while True:
    check, frame = video.read()
    
    if not check: break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (17,17), 0)

    circles = cv2.HoughCircles(blur, cv2.HOUGH_GRADIENT, 1.2, 100,
                               param1 = 100, param2 = 30, minRadius = 75, maxRadius = 400)

    if circles is None:
        circles = np.uint16(np.round(circles))
        chosen = None
        for i in circles[0, :]:
            if chosen is None: chosen = i
            if previous is not None:
                if distance(chosen[0], chosen[1], previous[0], previous[1]) <= distance(i[0], i[1], previous[0], previoys[1]):
                    chosen = i

        cv2.circle(frame, (chosen[0], chosen[1]), 1, (0,100,100), 3)
        cv2.circle(frame, (chosen[0], chosen[1]), chosen[2], (255,0,255), 3)
        previous = chosen

    cv2.imshow("Circles", frame)
        
    if cv2.waitKey(1) & 0xFF == ord('q'): break

video.release()
cv2.destroyAllWindows
