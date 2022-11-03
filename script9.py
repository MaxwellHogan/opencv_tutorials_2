'''
In this script we are going to being looking into histogram representation.

This is where we visualise the distribution of pixel values, sometimes refered to 
as the tonal distribution. 

In order to plot the histogram we will be using a new package - matplotlib. If
you look below I have left some example code for plotting the image and the 
histogram in the same window. There is no waitkey operation in matplotlib so in 
order to continue the program to the end, exit the window.

'''

### Import OpenCV & numpy #####
import cv2
import numpy as np
import matplotlib.pyplot as plt

#######################
### Read an Image #####

img = cv2.imread('images/robot1.jpg')

###############################################
######### Convert img to grayscale ############
gray = 

############################################
########### Create the Histogram ###########
hist = cv2.calcHist()

################################################
### Plot the Histogram and display the image ###

fig, [ax1, ax2] = plt.subplots(1,2, figsize=(10,4))

ax1.plot(hist, color = 'k')
ax1.set_ylabel("pixel count")
ax1.set_xlabel("pixel value")

ax2.imshow(gray, cmap = 'gray')
ax2.set_title('grey image')

plt.show()

##Exiting Function######
plt.close()