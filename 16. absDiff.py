import cv2 as cv
import numpy as np

capture = cv.VideoCapture('videos/moving-crowd.mp4')

if capture.isOpened() == False:
    print("Error loading video file!")

background = None
back_cont = None

while capture.isOpened():

    ret, frame = capture.read()
    gray_frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    gray_frame = cv.GaussianBlur(gray_frame, (21,21), 0)

    if ret == False:
        break

    if background is None:
        background = gray_frame
        _, thresh = cv.threshold(background, 150, 255, cv.THRESH_BINARY_INV)
        back_cont, _ = cv.findContours(thresh, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
        # cv.drawContours(background, back_cont, -1, (0,255,0), 2)
        # cv.imshow('back', background)
        continue

    diff = cv.absdiff(background, gray_frame)
    cv.imshow("diff", diff)
    _, thresh = cv.threshold(diff, 70, 255, cv.THRESH_BINARY)
    # cv.imshow("thresh", thresh)
    contours,_ = cv.findContours(thresh, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    # print(contours)

    for contour in contours:
        if cv.contourArea(contour) < 500:
            continue
        (x, y, w, h) = cv.boundingRect(contour)
        cv.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 2) 

    # cv.imshow('Frame', frame)

    if cv.waitKey(25) & 0xFF == ord('q'):
        break

# Releases the video Capture object
capture.release()
# Closes all the frames
cv.destroyAllWindows()


