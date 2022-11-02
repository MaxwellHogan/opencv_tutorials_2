'''
    In this script we are going to introduce an alternitive way to
    improve image contrast without distorting the colors too much. 

    To do this you will fist need to convert the image into a new 
    colorspace HSV.

    HSV stands for Hugh, saturation, Value (or brightness). 

    The tasks in this script are as follows: 
        - convert the img from BRG to HSV.
        - split the image into color channels
        - equalise the value channel
        - use merge to re-combine the Hue, Saturation and the new equalised value channel. 
'''

### Import OpenCV & numpy #####

import cv2
import numpy as np
import matplotlib.pyplot as plt

#######################
### Read an Image #####
img = cv2.imread('images/blue.jpg')
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

############################
### Convert bgr to hsv #####


#########################
### Split the Image #####



#####################################
####  Equalize the value channel ####



#######################################
### Use merge to combine channels #####


#########################################
### Conver image to rgb for display #####


###############################
##### Display new image #######

fig, [ax1, ax2] = plt.subplots(1,2, figsize = (7,5))

ax1.imshow(img_rgb, vmin = 0, vmax = 256)
ax1.set_title('Original')
ax2.imshow(, vmin = 0, vmax = 256)
ax2.set_title('Equalized')
plt.show()

##Exiting Function######
plt.close()
