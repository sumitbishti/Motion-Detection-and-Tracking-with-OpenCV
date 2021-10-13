import cv2 as cv

face_cascade = cv.CascadeClassifier('haar_face.xml')
eye_cascade = cv.CascadeClassifier('haar_eye.xml')
cap = cv.VideoCapture(0)

while cap.isOpened():

    ret, frame = cap.read()
    if ret == False:
        break

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    faces_rect = face_cascade.detectMultiScale(gray, 1.1, 5)

    for (x,y,w,h) in faces_rect:
        cv.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 3)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]

        eyes_rect = eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes_rect:
            cv.rectangle(roi_color, (ex,ey), (ex+ew, ey+eh), (0,255,0), 3)

    cv.imshow('faces', frame)

    if cv.waitKey(25) == ord('q'):
        break

cap.release()
cv.destroyAllWindows()