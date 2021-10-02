import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('photos/carr.jpg')
cv.imshow('carr', img)

# Grayscale Histogram

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('gray', gray)

blank = np.zeros(img.shape[:2], dtype='uint8')
# # cv.imshow('blank', blank)

circle = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 200, 255, -1)
# # cv.imshow('circle', circle)

mask = cv.bitwise_and(gray, blank)
cv.imshow('mask',mask)

# hist = cv.calcHist([img], [0], mask, [256], [0,256])

# plt.figure()
# plt.title("Grayscale histogram")
# plt.xlabel('Bins')
# plt.ylabel('no. of pixels')
# plt.plot(hist)
# plt.show()


# Color Histogram
plt.figure()
plt.title('Colored Histogram')
plt.xlabel('Bins')
plt.ylabel('No. of pixels')
colors = ('b', 'g', 'r')

for i,col in enumerate(colors):
    hist = cv.calcHist([img], [i], mask, [256], [0,256])
    plt.plot(hist, color=col)

plt.show()


cv.waitKey(0)
