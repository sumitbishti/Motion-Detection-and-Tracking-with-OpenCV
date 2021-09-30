import cv2 as cv
import numpy as np

img = cv.imread('photos/carr.jpg')
cv.imshow('img', img)

blank = np.zeros(img.shape[:2], dtype='uint8')
# cv.imshow('blank', blank)

circ = cv.circle(blank.copy(), (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
rect = cv.rectangle(blank.copy(), (100,100), (300,300), 255, -1)
# cv.imshow('mask', mask)

mask = cv.bitwise_not(circ, rect)

masked = cv.bitwise_and(img, img, mask=mask)
cv.imshow('masked', masked)

cv.waitKey(0)