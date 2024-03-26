from src.infrastructure.interfaces.ipostprocess import IPostProcess
import cv2

class PostProcess(IPostProcess):

    def __init__(self):
        pass

    def postprocess(self, rslt, frame):
        # Iterating through rectangles of detected faces 
        for (x, y, w, h) in rslt: 
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2) 
