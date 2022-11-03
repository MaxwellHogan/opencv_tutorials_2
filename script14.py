'''
    HSV represents color in a very simplistic way. In this notebook 
    we are going to take andvantage of this to filter an image based
    on a specifc color. In this specific example you are going to 
    filter the image to only show the butterfly.
    
    To do this we will need to first create a 'mask' which will 
    determine which pixels to keep and which pixels to discard.

    This is a complex process which will require some tuning of 
    parameters, namely the lower and upper bounds that we are going
    to use to create the mask. 

    To decide the lower and upper limits you need to first use 
    cv2.imshow to display each color channel of the HSV image. When
    this the window opens you can hover your curser over parts of 
    the image and it will display the pixel value in the bottom 
    corner. 

'''

### Import OpenCV & numpy #####
import cv2
import numpy as np

######################
### Read an Image ####

img = cv2.imread('images/mix.jpg')
## convert to hsv
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

## take a look at the image
cv2.imshow('Butterfly', img)
cv2.waitKey(0)

##########################################################
##### use cv2.imshow to display each channel of hsv ######


cv2.waitKey(0)

#################################################
##### Calculate the lower and upper limits ######

## Note lower and upper are expected to be numpy arrays 
lower = np.array([ 90,  9, 248])
upper = np.array([130, 68, 255])

######################################
##### create and apply the mask ######

# use inRange with the lower and upper limits defined above to create the mask  
mask = 

## apply mask to the image using bitwise_and
result = 

###############################
##### Display the images ######

cv2.imshow('main', img)
cv2.imshow('mask', mask)
cv2.imshow('masked img', result)
cv2.waitKey(0)

##Exiting Function######
cv2.destroyAllWindows()