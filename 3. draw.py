import cv2 as cv
import numpy as np

img = cv.imread('photos/mom.jpg')
# cv.imshow('mom', img)

blank = np.zeros((500,500,3), dtype='uint8')
# cv.imshow('blank', blank)

# 1. Paint the image
# blank[100:200, 200:300] = 0,0,255
# cv.imshow('color', blank)

# 2. draw a rectangle
cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0,255,0), thickness=cv.FILLED)
cv.imshow('rect', blank)

# 3. draw a circle
cv.circle(blank, (250,250), 50, (0,0,255), thickness=-1)
# cv.imshow('circle', blank)

#4. draw a line
cv.line(blank, (0,0), (500,500), (255,255,255), thickness=2)
# cv.imshow('line', blank)

#5. text on a image
cv.putText(blank, "iam sumit bisht", (0,250), cv.FONT_HERSHEY_COMPLEX_SMALL, 2.0, (255,255,255), 2)
cv.imshow('text', blank)

cv.waitKey(0)