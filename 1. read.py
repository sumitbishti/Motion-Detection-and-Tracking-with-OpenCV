import cv2 as cv

img = cv.imread('photos/mom.jpg')
cv.imshow('mom', img)

def rescaleFrame(frame, scale=0.75):
    #for images, videos or live videos
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


res_img = rescaleFrame(img, scale=0.2)
cv.imshow('img', res_img)

capture = cv.VideoCapture('videos/Compressed.mp4')

while capture.isOpened():

    ret, frame = capture.read()
    if not ret:
        break

    res_frame = rescaleFrame(frame, 0.3)
    cv.imshow('video', frame)
    cv.imshow('video resized', res_frame)

    if cv.waitKey(25) & 0xFF == ord('q'):
        break

capture.release()
cv.destroyAllWindows()

cv.waitKey(0)