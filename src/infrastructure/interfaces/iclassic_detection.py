from abc import ABC, abstractmethod

class IClassicDetection(ABC):

    @abstractmethod
    def Detect(self, frame):
        pass
