import cv2 as cv
import numpy as np

img = cv.imread('photos/carr.jpg')
# cv.imshow('img', img)

# 1. Translation
transMat = np.float32([[1, 0, 100], [0, 1, -100]])
dimensions = (img.shape[1], img.shape[0])

translated = cv.warpAffine(img, transMat, dimensions)
# cv.imshow('translated', translated)

# 2. Rotation
h, w = img.shape[:2]

rotMat = cv.getRotationMatrix2D((w/2, h/2), 45, 0.5)
rotated = cv.warpAffine(img, rotMat, (w,h))
# cv.imshow('rotated', rotated)

# 3. Resizing
resized = cv.resize(img, (500,500), interpolation=cv.INTER_AREA)
# cv.imshow('resized', resized)

# 4. Fliping
flipped = cv.flip(img, 0)
cv.imshow('flipped', flipped)

# 5. Cropping
cropped = img[100:500, 0:300]
cv.imshow('cropped', cropped)


cv.waitKey(0)
