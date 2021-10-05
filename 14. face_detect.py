import cv2 as cv

img = cv.imread('photos/manoj.jpg')
# cv.imshow('manoj', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('gray', gray)

haar_cascade = cv.CascadeClassifier('haar_face.xml')

faces_rect = haar_cascade.detectMultiScale(gray, 1.1, 6)
# faces_rect -> list of coordinates of rectangles around faces

print(len(faces_rect))

for (x,y,w,h) in faces_rect:
    cv.rectangle(img, (x,y), (w, h), (0,255,0), thickness=2)

cv.imshow('detect', img)



cv.waitKey(0)