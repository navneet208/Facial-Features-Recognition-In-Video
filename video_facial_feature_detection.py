#In this program, we will try to detect eyes in a video using the HAAR CASCADE FACE DETECTION CLASSIFIER
import cv2

#face detection algorithm, which is predefined and we don't have to make it.
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eyes_cascade = cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')

cap = cv2.VideoCapture(0)

while cap.isOpened():
    #capturing frames
    _, img = cap.read()

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #face var will be the rect with detected faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x,y), (x+w, y+h), (255, 0, 0), 3)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]

        eyes = eyes_cascade.detectMultiScale(roi_gray)

        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 5)

    #show the input image
    cv2.imshow('img', img)
    if cv2.waitKey(1) & 0xFF == 27:
        print("Closing video....")
        break
    #cv2.imwrite('copy.png', img)
#cv2.imwrite('video.mp4', cap)
cap.release()