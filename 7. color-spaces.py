import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('photos/carr.jpg')
# cv.imshow('car', img)

# plt.imshow(img)
# plt.show()

# BGR to Grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('gray', gray)

# BGR to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
# cv.imshow('hsv', hsv)

# BGR to LAB
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('lab', lab)

# BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
# cv.imshow('rgb', rgb)

# HSV to BGR
hsv_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
# cv.imshow('hsv_bgr', hsv_bgr)

# LAB to BGR
lab_bgr = cv.cvtColor(lab, cv.COLOR_Lab2BGR)
cv.imshow('lab_bgr', lab_bgr)

cv.waitKey(0)
