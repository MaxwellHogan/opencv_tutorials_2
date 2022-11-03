'''
In this script we are going to intorduce the concept of histgram equalisation.
Below is a link to a good tutorial on the subject.

This operation will enhance the contrast in the image by strerching out the 
intensity range. Note: this operation can only be done on greyscale images or
a single color channel at a time.

tutorial: https://docs.opencv.org/4.x/d4/d1b/tutorial_histogram_equalization.html

Tasks to be done in this script:
    - perform histogram equalisation on the image and store the new image as 'equalized'
    - calculate the histgrams for the original image and for 'equalized' (store them as before and after)
    - plot the results by filling in the missing part of the code.

'''
###############################
#### Import OpenCV & numpy ####
import cv2
import numpy as np
import matplotlib.pyplot as plt

#######################
### Read an Image #####

img = cv2.imread('images/thermal_0.png', 0)

plt.imshow(img, cmap="gray", vmin = 0, vmax = 256)
plt.show()

######################################################
##### Perform histogram equalisation Histogram #######

equalized = cv2.equalizeHist()

#############################################
########### Create the Histograms ###########

before = 
after = 

################################################
### Plot the Histogram and display the image ###

## create a 2x2 subplot
fig, axs = plt.subplots(2,2, figsize=(7,7))

## plot the original image in top left
axs[0,0].imshow(, cmap = 'gray', vmin = 0, vmax = 256)
axs[0,0].set_title('original image')

## plot the before histogram in bottom left
axs[1,0].plot(, color = 'k')
axs[1,0].set_title("histogram before equalisation")
axs[1,0].set_ylabel("pixel count")
axs[1,0].set_xlabel("pixel value")

## plot the equalized image in top right
axs[0,1].imshow(, cmap = 'gray', vmin = 0, vmax = 256)
axs[0,1].set_title('equalized image')

## plot the after histogram in bottom right
axs[1,1].plot(, color = 'k')
axs[1,1].set_title("histogram after equalisation")
axs[1,1].set_ylabel("pixel count")
axs[1,1].set_xlabel("pixel value")

plt.show()
##Exiting Function######
plt.close()