from abc import ABC, abstractmethod

class IPostProcess(ABC):    

    @abstractmethod
    def postprocess(self, faces, frame):
        pass
