import cv2 as cv
import numpy as np

cap = cv.VideoCapture('videos/moving-crowd.mp4')

ret, f1 = cap.read()
ret, f2 = cap.read()

fgbg = cv.createBackgroundSubtractorKNN(detectShadows=False)

while cap.isOpened():

    fgmask = fgbg.apply(f1)

    dil = cv.dilate(fgmask, (11, 11))
    mb = cv.medianBlur(dil, 7)

    kernel0 = np.ones((5, 5), np.uint8)
    kernel1 = cv.getStructuringElement(cv.MORPH_CROSS, (5, 5))

    close = cv.morphologyEx(mb, cv.MORPH_CLOSE, kernel0)
    conts, _ = cv.findContours(close, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

    for cont in conts:
        if cv.contourArea(cont) < 1000:
            continue
        (x, y, w, h) = cv.boundingRect(cont)
        cv.rectangle(f1, (x, y), (x+w, y+h), (0, 255, 0), 2)

    cv.imshow('rects', f1)

    f1 = f2
    ret, f2 = cap.read()

    if cv.waitKey(25) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
