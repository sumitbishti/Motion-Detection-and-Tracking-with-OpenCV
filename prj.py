import cv2 as cv

cap = cv.VideoCapture('videos/moving-crowd.mp4')

ret, f1 = cap.read()
ret, f2 = cap.read()

while cap.isOpened():

    diff = cv.absdiff(f1, f2)
    gf = cv.cvtColor(diff, cv.COLOR_BGR2GRAY)
    gf = cv.GaussianBlur(gf, (7,7), 0)
    _, thresh = cv.threshold(gf, 20, 255, cv.THRESH_BINARY)
    dilated = cv.dilate(thresh, None, iterations=2)
    cv.imshow('diff', dilated)
    
    f1 = f2
    ret, f2 = cap.read()

    if cv.waitKey(25) & 0xFF == ord('q'):
        break


cap.release()
cv.destroyAllWindows()

    