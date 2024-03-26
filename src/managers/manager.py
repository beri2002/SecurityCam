import cv2
import time
from src.infrastructure.classes.model import Model
from src.infrastructure.classes.postprocess import PostProcess
from src.infrastructure.classes.preprocess import PreProcess
from src.infrastructure.classes.video_handler import VideoHandler
from src.managers.config_manager import ConfigManager

class Manager():
    def __init__(self, configPath="config/config.json"):
        # Initialize configuration manager
        self._config_manager = ConfigManager(configPath)
        # Read configuration data
        config_data = self._config_manager.read_config()
        
        # Initialize preprocessing, postprocessing, and video handling objects
        self._preprocess = PreProcess()
        self._postprocess = PostProcess()
        self._video_handler = VideoHandler(config_data["VideoHandler"]["videoSource"])
        
        # Read the first frame from the video source and preprocess it
        ret, self._frame = self._video_handler.read_frame()
        self._frame = self._preprocess.preprocess(self._frame)
        
        # Initialize the model
        self._model = Model(self._frame, config_data["Model"]["ModelPath"])

    def detect_frame(self):
        """
        Process a single frame: preprocess, detect objects, postprocess, and display.
        Returns True if objects are detected in the frame, False otherwise.
        """
        start = time.time()
        
        # Read a frame from the video source
        ret, self._frame = self._video_handler.read_frame()

        if not ret:
            print("Failed to read frame")
            return False

        # Preprocess the frame
        self._frame = self._preprocess.preprocess(self._frame)

        # Detect objects in the frame
        results = self._model.Detect(self._frame)

        # Postprocess the results

        # Display the processed frame
        self._video_handler.show_video(self._frame)

        end = time.time()
        time_difference = end - start
        fps = 1 / time_difference

        # Display processing time and FPS
        print("Processing Time:", round(time_difference * 1000, 2), "milliseconds")
        print("FPS:", round(fps, 2))

        # Return True if objects are detected, False otherwise
        return True if results else False

    def detect_video(self):
        """
        Continuously process frames from the video source,
        detect objects, and handle recording.
        """
        while True:
            # Detect objects in the frame
            record = self.detect_frame()
            
            # Handle recording based on detection results
            self._video_handler.recorder(record)
            
            # Check for user input to quit the loop
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # Clean up resources
        self._video_handler.__del__()
