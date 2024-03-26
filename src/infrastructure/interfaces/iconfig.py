from abc import ABC, abstractmethod

class IConfig(ABC):

    @abstractmethod
    def read_config(self, configPath):
        pass