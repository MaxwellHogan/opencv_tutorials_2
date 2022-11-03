'''
In this script we will be using demonstraiting Hough circle detection.
For best results it is good practice to blur the image (unless already
smooth), to that end you should create a blurred the img using cv2.blur.

With this new blurred image you should then apply Hough circles, I have
provided details below about how to used this operation.

The arguments of cv2.HoughCircles are:
    image	8-bit, single-channel, grayscale input image.

    method	The available methods are HOUGH_GRADIENT and HOUGH_GRADIENT_ALT.
            We will use cv2.HOUGH_GRADIENT

    dp	Inverse ratio of the accumulator resolution to the image resolution.
        If dp=1 , the accumulator has the same resolution as the input image. 
        If dp=2 , the accumulator has half as big width and height. 
        We will use 1.
        
    minDist	Minimum distance between the centers of the detected circles. 

    param1	First method-specific parameter. It is the higher threshold of the
            two passed to the Canny edge detector (the lower one is twice smaller). 


    param2	Second method-specific parameter. In case of HOUGH_GRADIENT, it is the accumulator threshold for the circle centers at the detection stage. The smaller it is, the more false circles may be detected. Circles, corresponding to the larger accumulator values, will be returned first. In the case of HOUGH_GRADIENT_ALT algorithm, this is the circle "perfectness" measure. The closer it to 1, the better shaped circles algorithm selects. In most cases 0.9 should be fine. If you want get better detection of small circles, you may decrease it to 0.85, 0.8 or even less. But then also try to limit the search range [minRadius, maxRadius] to avoid many false circles.

    minRadius	Minimum circle radius.
    maxRadius	Maximum circle radius. 

Output of HoughCircles is:
    Circles	Output vector of found circles. Each vector is encoded as 3 or 4
    element floating-point vector (x,y,radius) or (x,y,radius,votes).

'''
### Import OpenCV & numpy #####

import cv2
import numpy as np
import matplotlib.pyplot as plt

### Read an Image #####

img = cv2.imread('images/coins.jpg')
img1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


#####  CIRCLE DETECTION #####################

blurred = cv2.blur(img1, (3,3))

circles = cv2.HoughCircles(

                            )


## plot circles over image 
if circles is not None:
    circles = np.uint16(np.around(circles))

    for pt in circles[0,:]:
        a,b,r = pt[0],pt[1],pt[2]

        cv2.circle(img,(a,b), r,(0,255,0),2)
        cv2.circle(img,(a,b), 1,(0,0,255),2)

########################
cv2.imshow('main', img)
cv2.waitKey(0)




##Exiting Function######

cv2.destroyAllWindows