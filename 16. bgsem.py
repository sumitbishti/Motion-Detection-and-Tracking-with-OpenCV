import cv2 as cv
import numpy as np

cap = cv.VideoCapture('videos/moving-crowd.mp4')

ret, f1 = cap.read()
ret, f2 = cap.read()

fgbg = cv.createBackgroundSubtractorKNN(detectShadows=False)

while cap.isOpened():
    
    fgmask = fgbg.apply(f1)
    cv.imshow('vid', fgmask)

    kernel0 = np.ones((5,5), np.uint8)
    kernel1 = cv.getStructuringElement(cv.MORPH_ELLIPSE, (5,5))
    kernel3 = cv.getStructuringElement(cv.MORPH_CROSS, (5,5))

    close = cv.morphologyEx(fgmask, cv.MORPH_CLOSE, kernel3, iterations=3)
    cv.imshow('close', close)


    f1 = f2
    ret, f2 = cap.read()

    if cv.waitKey(25) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()