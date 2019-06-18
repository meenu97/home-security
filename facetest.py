import cv2
import numpy as np

def facedetect(img):
    profile_face_cascade=cv2.CascadeClassifier('/usr/local/share/OpenCV/haarcascades/haarcascade_frontalface_default.xml')
    face_cascade = cv2.CascadeClassifier('/home/pi/face_recognizer/haarcascade_frontalface_default.xml')
    face_cas = cv2.CascadeClassifier('/usr/local/share/OpenCV/haarcascades/haarcascade_eye_tree_eyeglasses.xml')
    face_ca = cv2.CascadeClassifier('/usr/local/share/OpenCV/haarcascades/haarcascade_frontalface_alt2.xml')
    
    
    faces = face_cascade.detectMultiScale(img, 1.3, 5,minSize=(100,100))
    face2=profile_face_cascade.detectMultiScale(img,1.3,5,minSize=(100,100))
    faces1 = face_cas.detectMultiScale(img, 1.3, 5,minSize=(100,100))
    faces4 = face_ca.detectMultiScale(img, 1.3, 5,minSize=(100,100))
    
    for (x,y,w,h) in faces:
         return [[x,y,w,h]]       
    for (x,y,w,h) in faces1:
         return [[x,y,w,h]]       
    for (x,y,w,h) in face2:
         return [[x,y,w,h]]       
    for (x,y,w,h) in faces4:
         return [[x,y,w,h]]       
                        

    return 
    cv2.namedWindow('image',cv2.WINDOW_NORMAL)
    cv2.resizeWindow('image',600,600);
    cv2.imshow('image',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    