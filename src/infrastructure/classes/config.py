from src.infrastructure.interfaces.iconfig import IConfig
import json

class Config(IConfig):

    def __init__(self, configPath):
        self.configPath = configPath


    def read_config(self):
        """
        Reads the configuration file and returns the parsed JSON data.

        Returns:
            dict: The parsed JSON data from the configuration file.
        """
        with open(self.configPath) as f:
            data = json.load(f)

        return data