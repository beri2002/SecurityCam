from src.infrastructure.interfaces.iclassic_detection import IClassicDetection
import cv2
import numpy as np

class ClassicDetection(IClassicDetection):

    def __init__(self):
        # initialize the HOG descriptor/person detector
        self._hog = cv2.HOGDescriptor()
        self._hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

    def Detect(self, gray_frame):
        # detect people in the image
        # returns the bounding boxes for the detected objects
        boxes, weights = self._hog.detectMultiScale(gray_frame, winStride=(8,8) )

        boxes = np.array([[x, y, x + w, y + h] for (x, y, w, h) in boxes])