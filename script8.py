'''
This week we will be undertaking more complex operations, the first of
which is canny edge detection.

Like many of the operations we will cover this week, you may need to do
some hyperparameter tuning. The link below will take you to canny in the 
documentation to help you understand these hyperparamters. 

documentation: https://docs.opencv.org/4.x/dd/d1a/group__imgproc__feature.html#ga04723e007ed888ddf11d9ba04e2232de

'''
#############################
### Import OpenCV & numpy ###
import cv2
import numpy as np


#######################
### Read an Image #####
img = cv2.imread('images/robot2.jpg')


#####################################
######### Edge Detection ############


###########################
### Display the results ###

cv2.imshow('main', img)
cv2.waitKey(0)


cv2.imshow('edges',)
cv2.waitKey(0)

########################
### Exiting Function ###
cv2.destroyAllWindows()
