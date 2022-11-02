'''
    HSV represents color in a very simplistic way. In this notebook 
    we are going to take andvantage of this to filter an image based
    on a specifc color. 
'''

### Import OpenCV & numpy #####
import cv2
import numpy as np
import matplotlib.pyplot as plt

######################
### Read an Image ####

img = cv2.imread('images/mix.jpg')
## convert to hsv
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

###############################################
#####  FILTER AN OBJECT BASED ON COLOUR #######

## define upper and lower bounds 
lower = np.array([ 90,  9, 248])
upper = np.array([130, 68, 255])

## call inRange create the mask


## apply mask to the image


########################

cv2.imshow('main', img)
cv2.imshow('mask', mask)
cv2.imshow('masked img', result)
cv2.waitKey(0)




##Exiting Function######

cv2.destroyAllWindows()
