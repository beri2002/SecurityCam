from abc import ABC, abstractmethod

class IVideoHandler(ABC):

    @abstractmethod
    def get_video(self, videoPath):
        pass

    @abstractmethod
    def read_frame(self, cap):
        pass

    @abstractmethod
    def get_video_properties(self, cap):
        pass

    @abstractmethod
    def show_video(self, frame, headline):
        pass

    @abstractmethod
    def __del__(self, cap):
        pass
