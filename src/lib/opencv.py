import cv2
import numpy as np


class OpenCV(object):
    def __init__(self):
        self.face_detector = cv2.CascadeClassifier('lib/haarcascade_frontalface_default.xml')

    def extract_faces_from_buffer(self, data):
        img_array = np.asarray(bytearray(data.read()), dtype=np.uint8)

        img = cv2.imdecode(img_array, 0)
        cv2.imwrite('test.jpg', img)

    def extract_faces(self, img_file):
        img = cv2.imread(img_file)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = self.face_detector.detectMultiScale(
            gray, 
            scaleFactor=1.2, 
            minNeighbors=5,
            minSize=(20, 20)
        )

        i_face = 1
        face_catalog = []
        for (x,y,w,h) in faces:
            filename = '{}-{}'.format(i_face, img_file)
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
            cv2.imwrite(filename, gray[y:y+h,x:x+w])
            #face_catalog.append(gray[y:y+h,x:x+w])
            face_catalog.append(filename)
            i_face = i_face + 1

        return face_catalog

    def identify_faces(self, img_file):
        img = cv2.imread(img_file)

        # img = cv2.flip(img, -1)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.2,
            minNeighbors=5,
            minSize=(20, 20)
        )

        i_face = 1
        face_catalog = []
        for (x,y,w,h) in faces:
            filename = '{}-{}'.format(i_face, img_file)
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
            roi_color = img[y:y+h, x:x+w]
            cv2.imwrite(filename, roi_color)
            #face_catalog.append(roi_color)
            face_catalog.append(filename)
            i_face = i_face + 1

        return face_catalog
