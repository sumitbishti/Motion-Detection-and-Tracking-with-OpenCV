import cv2 as cv
import numpy as np

img = cv.imread('photos/carr.jpg')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

# Simple Thresholding 

threshold, thresh = cv.threshold(gray, 150, 50, cv.THRESH_BINARY)
# threshold, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
cv.imshow('thresh', thresh)
# cv.imshow('thresh_inv', thresh_inv)

# _, thrsh = cv.threshold(gray, 100, 255, cv.THRESH_TRUNC)
# cv.imshow('to zero', thrsh)


# Adaptive Thresholding

adpt_thres = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY,
11, 0)

adp_thrsh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY_INV, 11, 11)
# cv.imshow('adp_thrsh', adp_thrsh)


cv.waitKey(0)