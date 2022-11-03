'''
Using what we learned in the last script, we are going to equilise an RGB
image. 

We want to be able to see the before and after so we don't want to do this 
operation in place - we want to instead make a copy of the image and then
perform the equalisation on that.

We are also going to make use of two built in functions from opencv, split
and merge.

'''
### Import OpenCV & numpy #####
import cv2
import numpy as np
import matplotlib.pyplot as plt

#######################
#### Read an Image ####

img = cv2.imread('images/blue.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(img, vmin = 0, vmax = 256)
plt.show()

#######################
### Split the Image ###

# split will return a list of mats - one mat for each color channel.


###################################
#####  Equalize each channel  #####



###################################################
### Merge the equalised channels into new image ###


####################################
########## plot histogram ##########

fig, axs = plt.subplots(1,3, figsize = (10,5))

for i, col in enumerate(['r','g','b']):


plt.show()


###################################
###### Display the Equalized ######

fig, [ax1, ax2] = plt.subplots(1,2, figsize = (7,5))

ax1.imshow(, vmin = 0, vmax = 256)
ax1.set_title('Original')
ax2.imshow(, vmin = 0, vmax = 256)
ax2.set_title('Equalized')
plt.show()
plt.show()

##Exiting Function######
plt.close()