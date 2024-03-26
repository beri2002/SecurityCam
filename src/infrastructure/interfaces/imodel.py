from abc import ABC, abstractmethod

class IModel(ABC):

    @abstractmethod
    def Detect(self, gray_img):
        pass
