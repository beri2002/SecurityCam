from abc import ABC, abstractmethod

class IPreProcess(ABC):

    @abstractmethod
    def __canny_edge_detect(self, image):
        pass

    @abstractmethod
    def __gray_scale(self, image):
        pass

    @abstractmethod
    def __resize(self, image):
        pass

    @abstractmethod
    def __blur(self, image):
        pass