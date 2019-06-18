import cv2
import numpy as np
from new import facerecognizer

def facedetect():
    profile_face_cascade=cv2.CascadeClassifier('/usr/local/share/OpenCV/haarcascades/haarcascade_profileface.xml')
    face_cascade = cv2.CascadeClassifier('/usr/local/share/OpenCV/haarcascades/haarcascade_frontalface_default.xml')
    face_cas = cv2.CascadeClassifier('/usr/local/share/OpenCV/haarcascades/haarcascade_eye_tree_eyeglasses.xml')
    face_ca = cv2.CascadeClassifier('/usr/local/share/OpenCV/haarcascades/haarcascade_frontalface_alt2.xml')
    img = cv2.imread('/home/pi/detectedfaces/new.jpg')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5,minSize=(100,100))
    face2=profile_face_cascade.detectMultiScale(gray,1.3,5,minSize=(100,100))
    faces1 = face_cas.detectMultiScale(gray, 1.3, 5,minSize=(100,100))
    faces4 = face_ca.detectMultiScale(gray, 1.3, 5,minSize=(100,100))
    label=[];
    for (x,y,w,h) in faces:
         label.append((x,y,w,h))   
    for (x,y,w,h) in faces1:
         label.append((x,y,w,h))
    for (x,y,w,h) in face2:
         label.append((x,y,w,h))
    for (x,y,w,h) in faces4:
         label.append((x,y,w,h))
    for (x,y,w,h) in label:
        img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        subface=img[y:y+h,x:x+w]
        facename="unknown"+str(y)+".jpg"
        cv2.imwrite(facename,subface)
    print (label)
    if label!=[]:
         facerecognizer()
    cv2.namedWindow('image',cv2.WINDOW_NORMAL)
    cv2.resizeWindow('image',600,600);
    cv2.imshow('image',img)
    cv2.waitKey(100)
    cv2.destroyAllWindows()
    print("after end")
    return