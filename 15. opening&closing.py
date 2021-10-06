import cv2 as cv
import numpy as np

img = cv.imread('photos/manoj.jpg')

gf = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gf', gf)

gb = cv.GaussianBlur(gf, (11,11), 0)
_, th = cv.threshold(gb, 150, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C)
cv.imshow('th', th)

# Dilation
dil = cv.dilate(gf, (7,7), iterations=5)
# cv.imshow('dil', dil)

# Erosion
ero = cv.erode(gf, (7,7), iterations=5)
# cv.imshow('erode', ero)

# Morphological Transformations
ker0 = np.ones((9,9), np.uint8)
cm = cv.erode(gf, ker0, iterations=3)
# cv.imshow('cm', cm)



cv.waitKey(0)