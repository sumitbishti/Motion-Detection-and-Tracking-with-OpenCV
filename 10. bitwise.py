import cv2 as cv
import numpy as np

img = cv.imread('photos/carr.jpg')

blank = np.zeros((400,400), dtype='uint8')

rect = cv.rectangle(blank.copy(), (30,30), (370,370), 255, -1)
cv.imshow('rect', rect)

circle = cv.circle(blank.copy(), (200, 200), 200,255,-1)
cv.imshow('circle', circle)

# bitwise AND
bit_and = cv.bitwise_and(rect, circle)
# cv.imshow('and', bit_and)

# bitwise OR
bit_or = cv.bitwise_or(rect, circle)
# cv.imshow('or', bit_or)

# bitwise XOR
bit_xor = cv.bitwise_xor(rect, circle)
# cv.imshow('xor', bit_xor)

# bitwise NOT
bit_not = cv.bitwise_not(circle)
cv.imshow('not', bit_not)

cv.waitKey(0)