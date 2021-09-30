import cv2 as cv

img = cv.imread('photos/carr.jpg')
cv.imshow('car', img)

# Averaging
average = cv.blur(img, (7,7))
cv.imshow('average', average)

# Gaussian Blur
gauss = cv.GaussianBlur(img, (7,7), 0)
cv.imshow('gauss', gauss)

# Median Blur
median = cv.medianBlur(img, 7)
cv.imshow('medain', median)

# Bilateral Blur
grayy = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
bilateral = cv.bilateralFilter(img, 20, 35, 35)
cv.imshow('bilateral', bilateral)

cv.waitKey(0)