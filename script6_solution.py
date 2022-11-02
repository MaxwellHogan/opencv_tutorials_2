'''
In this script we are going to continue the theme of investigating 
opencv's built in functions. Specifically we are going to look at 
the bluring operations availiable.

These include:
    - Gaussian Blur
    - Median Blur

If you have reached this point by yourself, I suggest looking into 
the hint for how to use these functions. On of these functions will 
be important in the final exercise so I suggest reading the details.

hint: https://docs.opencv.org/4.x/d4/d13/tutorial_py_filtering.html
'''
#############################
### Import OpenCV & numpy ###
import cv2
import numpy as np


#######################
### Read an Image #####
img = cv2.imread('images/robot2.jpg')

####################################
######### Gaussian Blur ############
kernel_size = 5
blur = cv2.GaussianBlur(img,(kernel_size,kernel_size),0)


####################################
########## Median Blur###############
kernel_size = 5
median = cv2.medianBlur(img,kernel_size)

###########################
### Display the results ###

cv2.imshow('Main', img)
cv2.waitKey(0)

cv2.imshow('Gaussian', blur)
cv2.waitKey(0)

cv2.imshow('Median', median)
cv2.waitKey(0)

########################
##Exiting Function######

cv2.destroyAllWindows()

########################