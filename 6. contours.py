import cv2 as cv
import numpy as np

img = cv.imread('carr.jpg')
# cv.imshow('img', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('gray', gray)

blank = np.zeros(img.shape, dtype='uint8')
# cv.imshow('blank', blank)

blur = cv.GaussianBlur(gray, (11,11), 0)
cv.imshow('blur', blur)

contr,_ = cv.findContours(blur, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
# print(contr)
# cv.drawContours(img, contr, -1, (0,255,0), 2)
# cv.imshow('mm', img)

canny = cv.Canny(blur, 125, 175)
# cv.imshow('canny', canny)

ret, thres = cv.threshold(gray, 200, 255, cv.THRESH_BINARY)
cv.imshow('thres', thres)

contours, hierarchies = cv.findContours(thres, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
# print(contours)

cv.drawContours(blank, contours, -1, (0,0,255), 1)
# cv.imshow('blankk', blank)


cv.waitKey(0)