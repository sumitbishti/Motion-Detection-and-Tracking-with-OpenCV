import cv2 as cv
import numpy as np

img = cv.imread('photos/carr.jpg')
# cv.imshow('img', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('gray', gray)

blank = np.zeros(img.shape, dtype='uint8')
# cv.imshow('blank', blank)

blur = cv.GaussianBlur(img, (5,5), cv.BORDER_DEFAULT)
# cv.imshow('blur', blur)

canny = cv.Canny(blur, 125, 175)
cv.imshow('canny', canny)

ret, thres = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
# cv.imshow('thres', thres)

contours, hierarchies = cv.findContours(thres, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)

cv.drawContours(blank, contours, -1, (0,0,255), 1)
cv.imshow('blankk', blank)


cv.waitKey(0)