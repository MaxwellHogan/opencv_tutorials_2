'''
This is where stuff will start to get tricky! We are going to do some operations between images.
These operations are not themselves challenging. However, we as you learned in class,
each pixel in an image can be a value between 0 and 255. Hence, there is risk that 
by summing or subtracting we may create a new image outside this range. 

You will see in this notepad I have filled in some blanks for you to get you started.

The tasks are outlined below.

'''
### Import OpenCV & numpy #####
import cv2
import numpy as np

#######################
### Read an Image #####

img1 = cv2.imread('images/wb1.jpg')
img2 = cv2.imread('images/wb2.jpg')

##########################################################
### Convert the images to float for further operations ###
### hint: https://numpy.org/doc/stable/reference/generated/numpy.ndarray.astype.html

img1 = img1.astype(float)
img2 = img2.astype(float)

#####################
#### Add Images #####
img_add = img1 + img2


###################################
##### Subtract img1 from img2 #####
img_subtract = img1 - img2


###########################
##### Multiply Images #####
img_multiply = img1 * img2

####################################################
##### Normalise the new images between 0 - 255 #####
## hint: https://stats.stackexchange.com/questions/70801/how-to-normalize-data-to-0-1-range

img_add = (img_add - img_add.min())/(img_add.max() - img_add.min())*255

img_subtract = (img_subtract - img_subtract.min())/(img_subtract.max() - img_subtract.min())*255

img_multiply = (img_multiply - img_multiply.min())/(img_multiply.max() - img_multiply.min())*255

#############################################
#### convert all images back to np.uint8 ####

img1 = img1.astype(np.uint8)
img2 = img2.astype(np.uint8)
img_add = img_add.astype(np.uint8)
img_subtract = img_subtract.astype(np.uint8)
img_multiply = img_multiply.astype(np.uint8)

#########################
### Display the results ###

cv2.imshow('Image 1', img1)
cv2.waitKey(0)

cv2.imshow('Image 2', img2)
cv2.waitKey(0)

cv2.imshow('Added', img_add)
cv2.waitKey(0)

cv2.imshow('Subtract', img_subtract)
cv2.waitKey(0)

cv2.imshow('Multiply', img_multiply)
cv2.waitKey(0)

########################
##Exiting Function######
cv2.destroyAllWindows()

########################