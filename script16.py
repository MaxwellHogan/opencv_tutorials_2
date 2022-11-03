'''
    This script will introduce you to the first of the hough transforms
    that we are going to be working with. 

    Here we will be using Hough lines. This operation will detect straight
    lines in an image. For best results we must first apply an edge detection 
    as a pre processing step. You can use the solution in script8 to do this.

    HoughLines takes the following arguements:
        img         :   8-bit, single-channel binary source image (edges)
        rho	        :   Distance resolution of the accumulator in pixels.
        theta	    :   Angle resolution of the accumulator in radians.
        threshold	:   Accumulator threshold parameter. 
                        Only those lines are returned that get enough votes ( >threshold ). 


    HoughLines will return a list of polar coordinates representing the lines
    that was detected. I left some code that can be used to draw the lines on
    the image. 

    https://docs.opencv.org/3.4/d9/db0/tutorial_hough_lines.html
    https://towardsdatascience.com/lines-detection-with-hough-transform-84020b3b1549
    
''' 
### Import OpenCV & numpy #####
import cv2
import numpy as np

### Read an Image #####

img = cv2.imread('images/sudoku.png')
img_gs = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

### Apply edge detection ###

edge = cv2.Canny()

##### APPLY HOUGH LINE ######

lines = cv2.HoughLines()

for line in lines:
    for rho, theta in line:
        a = np.cos(theta)
        b = np.sin(theta)

        x0 = a*rho
        y0 = b*rho

        pt1 = (int(x0 + 500*(-b)), int(y0 + 500*(a)))
        pt2 = (int(x0 - 500*(-b)), int(y0 - 500*(a)))
        cv2.line(img, pt1, pt2, (0,0,255), 2, cv2.LINE_AA)

########################
cv2.imshow('main', img)
cv2.waitKey(0)

##Exiting Function######S
cv2.destroyAllWindows()