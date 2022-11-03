'''
In this script we will be demoing Harris corners which was covered in the
lecture 3.

The first step for you will be to apply the cv2.cornerHarris operation to the image.
The required arguments for cv2.cornerHarris are as follows:
    img - Input image. It should be grayscale and float32 type.
    blockSize - It is the size of neighbourhood considered for corner detection
    ksize - Aperture parameter of the Sobel derivative used.
    k - Harris detector free parameter in the equation (use 0.07)

The operation will then return a map where the maxima are the location of the 
corners in the image. We want you to be able to highlight the corners in the
original image, to do this you will need to apply a threshold to only keep the
maximum values. 

'''

### Import OpenCV & numpy #####
import cv2
import numpy as np
import matplotlib.pyplot as plt

### Read an Image #####

img = cv2.imread('images/sudoku.png')

###############################
### Pre-process the image #####


###############################
##### Apply Harris Corner #####

corner = cv2.cornerHarris()

# corner = cv2.dilate(corner, None)

###############################
##### Set a value for thr #####

# Threshold for an optimal value, it may vary depending on the image.
thr = 
img[corner > thr * corner.max()] = [0,0,255]

########################
cv2.imshow('main', img)
cv2.imshow('corner', corner)
cv2.waitKey(0)


##Exiting Function######

cv2.destroyAllWindows()