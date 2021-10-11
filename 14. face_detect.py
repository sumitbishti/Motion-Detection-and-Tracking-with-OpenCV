import cv2 as cv

face_cascade = cv.CascadeClassifier('haar_face.xml')
cap = cv.VideoCapture(0)

while cap.isOpened():

    ret, frame = cap.read()
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    faces_rect = face_cascade.detectMultiScale(gray, 1.1, 3)
    for (x,y,w,h) in faces_rect:
        cv.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 2)

    cv.imshow('faces', frame)

    if cv.waitKey(25) == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
