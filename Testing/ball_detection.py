import cv2
import numpy as np;

# Font to write text overlay
font = cv2.FONT_HERSHEY_SIMPLEX

# Create lists that holds the thresholds
hsvMin = (20,120,120)
hsvMax = (49,255,255)

# Read test image
frame = cv2.imread("blob5.jpg")

# Convert to HSV
hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

# Apply HSV thresholds 
mask = cv2.inRange(hsv, hsvMin, hsvMax)

# Erode and dilate
mask = cv2.erode(mask, None, iterations=3)
mask = cv2.dilate(mask, None, iterations=3)

# Adjust detection parameters
params = cv2.SimpleBlobDetector_Params()
 
# Change thresholds
params.minThreshold = 0;
params.maxThreshold = 100;
 
# Filter by Area.
params.filterByArea = True
params.minArea = 400
params.maxArea = 20000
 
# Filter by Circularity
params.filterByCircularity = False
params.minCircularity = 0.1
 
# Filter by Convexity
params.filterByConvexity = False
params.minConvexity = 0.5
 
# Filter by Inertia
params.filterByInertia = False
params.minInertiaRatio = 0.5

# Detect blobs
detector = cv2.SimpleBlobDetector_create(params)

# Invert the mask
reversemask = 255-mask

# Run blob detection
keypoints = detector.detect(reversemask)

# Get the number of blobs found
blobCount = len(keypoints)

# Write the number of blobs found
text = "Count=" + str(blobCount) 
cv2.putText(frame, text, (5,25), font, 1, (0, 255, 0), 2)

if blobCount > 0:
    # Write X position of first blob
    blob_x = keypoints[0].pt[0]
    text2 = "X=" + "{:.2f}".format(blob_x )
    cv2.putText(frame, text2, (5,50), font, 1, (0, 255, 0), 2)

    # Write Y position of first blob
    blob_y = keypoints[0].pt[1]
    text3 = "Y=" + "{:.2f}".format(blob_y)
    cv2.putText(frame, text3, (5,75), font, 1, (0, 255, 0), 2)        

    # Write Size of first blob
    blob_size = keypoints[0].size
    text4 = "S=" + "{:.2f}".format(blob_size)
    cv2.putText(frame, text4, (5,100), font, 1, (0, 255, 0), 2)    

    # Draw circle to indicate the blob
    cv2.circle(frame, (int(blob_x),int(blob_y)), int(blob_size / 2), (0, 255, 0), 2) 

# Show image
cv2.imshow("Blob detection", frame)
cv2.waitKey(0)
cv2.destroyAllWindows()
