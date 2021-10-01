import cv2 as cv

img = cv.imread('photos/carr.jpg')
cv.imshow('car', img)
# canny = cv.Canny(img, 40, 50)
# cv.imshow('canny', canny)

# Averaging
avg = cv.blur(img, (15,15))
# cv.imshow('average', avg)
# canny = cv.Canny(avg, 70, 80)
# cv.imshow('canny', canny)

# Gaussian Blur
gauss = cv.GaussianBlur(img, (21,21),0)
# cv.imshow('gauss', gauss)
# canny = cv.Canny(gauss, 70, 80)
# cv.imshow('canny', canny)

# Median Blur
median = cv.medianBlur(img, 11)
# cv.imshow('medain', median)
# canny = cv.Canny(median, 70, 80)
# cv.imshow('canny', canny)

# Bilateral Blur
# grayy = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
bilateral = cv.bilateralFilter(img, 7, 75, 75)
cv.imshow('bilateral', bilateral)
canny = cv.Canny(bilateral, 70, 80)
cv.imshow('canny', canny)

cv.waitKey(0)