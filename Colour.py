import cv2
import numpy
import matplotlib.pyplot as plt

img = cv2.imread('./Images/Mid.jpg')

cv2.imshow('Image', img)
print("Shape of the image: ", img.shape)
print("Accessing pixels for every rows of all the 3 RGB scale: ", img[0][0])

def hue_histogram(image):
    img_HSV = cv2.cvtColor(image, cv2.COLOR_BGR2HSV);
    plt.figure()
    plt.xlim(0, 180)
    cm = plt.cm.get_cmap('hsv')
    n, bins, patches = plt.hist(img_HSV[:,:,0].ravel(), 256)
    for i, p in enumerate(patches):
        plt.setp(p, 'facecolor', cm(i/256))
    plt.show()

hue_histogram(img)

