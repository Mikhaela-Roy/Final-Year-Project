import cv2
import time
import numpy as np

#---Accessing the phone camera---#
video = cv2.VideoCapture(0)
#---Setting the IP address of the video stream on the phone---#
address = "https://10.240.7.61:8080/video"
video.open(address)

#---Setting up the detector with default parameters---#
detector = cv2.SimpleBlobDetector()
#---Detects blob---#
keypoints = detector.detect(video)
#---Draw the detected blobs as red circles---#
vid_with_keypoints = cv2.drawKeypoints(video. keypoints, np.array([]), (0,0,255),
                                       cv2.DRAW_,MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

#---AFTER DETECTING BLOBS IN THE ENVIRONMENT
#---FILTER THE BLOBS BY COLOUR, SIZE AND SHAPE
#---TO DO THIS SET THE PARAMETERS

#---Setup SimpleBlobDetector paramters---#
params = cv2.SimpleBlobDetector_Params()
#---Change Threshold---#
params.minThreshold = 10
params.maxThreshold = 200
#---Filtering by parameters---#
params.filterByArea = True
params.minArea = 1500
#---Filter by Circularity---#
params.filterByCircularity = True
params.minCircularity = 0.1
#---Filter by Convexity---#
params.filterByConvexity = True
params.minConvexity = 0.07
#---Filter by Inertia---#
params.filterByInertia = True
params.minInertiaRatio = 0.01

while True:
    check, frame = video.read()
    cv2.imshow("Camera Feed", frame)

    #---Create a detector with parameters---#
    ver = (cv2.__version__).split('.')
    if int(ver[0])<3:
        detector = cv2.SimpleBlobDetector(params)
    else:
        dettector = cv2.SimpleblobDetector_create(params)

    key = cv2.waitKey(1)
    
video.release()
cv2.destroyAllWindows()
