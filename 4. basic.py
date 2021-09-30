import cv2 as cv

img = cv.imread('photos/car.jpg')
# cv.imshow('mom', img)

# 1. convert to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('gray', gray)

# 2. blur an image
blur = cv.GaussianBlur(img, (7, 7), cv.BORDER_DEFAULT)
# cv.imshow('blur', blur)

# 3. create a edge cascade
canny = cv.Canny(img, 150, 160)
cv.imshow('canny', canny)

# 4. dilate an image
dilated = cv.dilate(img, (7,7), iterations=5)
cv.imshow('dilated', dilated)

# 5. eroding
eroded = cv.erode(dilated, (3,3), iterations=3)
cv.imshow('eroded', eroded)

# 6. resize
resized = cv.resize(img, (500,300), interpolation=cv.INTER_AREA)
# cv.imshow('resized', resized)

# 7. Crop
img = img[100:200, 250:350]
# cv.imshow('imgg', img)

cv.waitKey(0)
