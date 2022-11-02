##########################Excercise####################################
#                                                                     #
# As an Engineer working with OpenCV, Tesla Company Contracted you    #
# to help resolve a vision based problem where their Camera often     #
# pick up a salt and pepper noise while at high speed.                #
# You have been provided with an image of dimension 716 X 295.        #
# This image must fit into a custom vehicle detection neural network  #
# with an input layer of size 600 X 250.                              #
# Please write a short pre-processing program that will clear up      #
# the noise and also match the input layer of the DNN                 #
#                                                                     #
# Hint: Use one of the bluring technique                              #
#       Choose a suitable kerne_size.                                 #
#                                                                     #
#  mahmoud.abdulsalam@city.ac.uk                                      #
#######################################################################


### Import OpenCV & numpy #####

import cv2
import numpy as np
from skimage.util import random_noise

#######################
### Read an Image #####
img = cv2.imread("images/dashcam.jpeg")

##############################################
############### Salt & Pepper ################

## DO NOT CHANGE
img = random_noise(img,mode="s&p",amount=0.3)
noise = np.array(255*img, dtype= 'uint8')

#########################################
##########  Your Solution ###############

kernel_size = 5

denoised = cv2.medianBlur(noise, kernel_size)

new_dim = (600,250)

img_out = cv2.resize(denoised, new_dim, interpolation=cv2.INTER_AREA)

###########################
### Display the results ###

cv2.imshow('Noisy', noise)
cv2.waitKey(0)


cv2.imshow('Solution', img_out)
cv2.waitKey(0)

########################
##Exiting Function######
cv2.destroyAllWindows()

