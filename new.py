#!/usr/bin/python

# Import the required modules
import cv2, os
import numpy as np
from facetest import facedetect
from emailpic import mail
from led import lock
# For face detection we will use the Haar Cascade provided by OpenCV.

    
cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier('/home/pi/face_recognizer/haarcascade_frontalface_default.xml')
dict={}
# For face recognition we will the the LBPH Face Recognizer 
recognizer = cv2.face.createLBPHFaceRecognizer()
def atoi(s):
    c=0
    for i in s:
        c+=ord(i)
    dict[c]=s;    
    return c    
    

def get_images_and_labels(path):
    # Append all the absolute image paths in a list image_paths
    # We will not read the image with the .sad extension in the training set
    # Rather, we will use them to test our accuracy of the training
    image_paths = [os.path.join(path, f) for f in os.listdir(path)]
    # images will contains face images
    images = []
    # labels will contains the label that is assigned to the image
    labels = []
    for image_path in image_paths:
        # Read the image and convert to grayscale
        imagep = cv2.imread(image_path)
        # Convert the image format into numpy array
        gray = cv2.cvtColor(imagep, cv2.COLOR_BGR2GRAY)
        image = np.array(gray, 'uint8')
        
        # Get the label of the image
        nbr =atoi(os.path.split(image_path)[1].split(".")[0])
        # Detect the face in the image
        faces = facedetect(gray)
        
        faces1 = faceCascade.detectMultiScale(gray,1.3,5,minSize=(100,100))
        
        # If face is detected, append the face to images and the label to labels
        for (x, y, w, h) in faces1:
            images.append(image[y: y + h, x: x + w])
            labels.append(nbr)
            cv2.imshow("Adding faces to traning set...", image[y: y + h, x: x + w])
            cv2.waitKey(50)
        if faces==None:
             continue
        for (x, y, w, h) in faces:
            images.append(image[y: y + h, x: x + w])
            labels.append(nbr)
            cv2.imshow("Adding faces to traning set...", image[y: y + h, x: x + w])
            cv2.waitKey(50)
        
            
    # return the images list and labels list
    return images, labels

def facerecognizer():
# Path to the Yale Dataset
    path = './faces'
# Call the get_images_and_labels function and get the face images and the 
# corresponding labels
    images, labels = get_images_and_labels(path)
    fl=0
    cv2.destroyAllWindows()

# Perform the tranining
    recognizer.train(images, np.array(labels ))
    path2='./detectedfaces'

    image_paths = [os.path.join(path2, f) for f in os.listdir(path2)]
    for image_path in image_paths:
        predict_imagep = cv2.imread(image_path)
        gray = cv2.cvtColor(predict_imagep, cv2.COLOR_BGR2GRAY)
        predict_image = np.array(predict_imagep, 'uint8')
        faces = facedetect(gray)
        faces1 = faceCascade.detectMultiScale(gray,1.3, 5,minSize=(100,100))
        for (x, y, w, h) in faces1:
            nbr_predicted, conf = recognizer.predict(gray[y: y + h, x: x + w])
            nbr_actual = os.path.split(image_path)[1].split(".")[0]
            print (nbr_predicted)
            if conf>110:
                print("unkown")
            elif nbr_predicted in dict:
                      print ("Recognized {} with confid {}".format(dict[nbr_predicted],conf))
                      name=dict[nbr_predicted]
                      if dict[nbr_predicted]=="meenu":
                          lock()
                      fl=1
            cv2.imshow("Recognizing Face", predict_image[y: y + h, x: x + w])
            cv2.waitKey(1000)
        if fl==1:
            break
        for (x, y, w, h) in faces:
            nbr_predicted, conf = recognizer.predict(gray[y: y + h, x: x + w])
            nbr_actual = os.path.split(image_path)[1].split(".")[0]
            print (nbr_predicted)
            if conf>100:
                print("unkown")
                cv2.imwrite("unknown"+".jpg",predict_image[y: y + h, x: x + w])
            elif nbr_predicted in dict:
                      print ("Recognized {} with confid {}".format(dict[nbr_predicted],conf))
                      if dict[nbr_predicted]=="meenu":
                          lock()
                      name=dict[nbr_predicted]    
                      
            cv2.imshow("Recognizing Face", predict_image[y: y + h, x: x + w])
            cv2.waitKey(1000)
            cv2.destroyAllWindows()
    mail(name)    
    

cv2.destroyAllWindows()
