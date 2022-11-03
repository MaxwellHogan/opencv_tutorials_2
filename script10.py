'''
In this script we are going to continue looking into histogram representation,
this time we will be plotting a histgram for each color channel, as opposed to
a greyscale image. We will continue using matplotlib to display the images,
so the first step will be to convert the image from RGB to BGR.

For this we will need to adapt the code from the last script and also make
use of a for loop to iterate over three color channels.

I have provided some code below to assist you. 
'''

### Import OpenCV & numpy #####

import cv2
import numpy as np
import matplotlib.pyplot as plt


#######################
### Read an Image #####
img = cv2.imread('images/snow.jpg')

#########################################
######### Convert img to RGB ############


## plot the image to makesure that the colors are correct
plt.imshow(img)
plt.show()

###########################################
######## Plot histograms Histogram ########

fig, axs = plt.subplots(1,3, figsize=(15,4))
titles = ['red', 'green', 'blue']

for idx, ax in enumerate(axs):
    pass


##Exiting Function######
plt.close()

cv2.destroyAllWindows()
