'''
This script is going to introduce you to some more concepts.
Specifically, how to access specfic color channels

The tasks the you need to do are:
    - import the required packages (in this case opencv)
    - read the image (the image's filename is "images/mix.jpg")
    - print the shape of the image.
    - access each color channel and store them as new, seperate images. 
    - display each color channel.
    - call the functions to keep the program from closing and to cleanup.

Hint: https://numpy.org/doc/stable/user/basics.indexing.html#dimensional-indexing-tools
'''

### Import OpenCV #####
import cv2


#######################
### Read an Image #####

img = cv2.imread("images/rgb.png")

###############################
### Print the Image Shape #####

print(img.shape)

###############################################
#### Split images into 3 colour spaces BGR ####

blue = img[:,:,0]
red = img[:,:,2]
green = img[:,:,1]

##################################
### Display the color channels ###

cv2.imshow("img", img)
cv2.imshow("blue", blue)
cv2.imshow("red", red)
cv2.imshow("green", green)


########################
#### Call waitKey ######

cv2.waitKey(0)

########################
##Exiting Function######
cv2.destroyAllWindows()