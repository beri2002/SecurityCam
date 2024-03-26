from src.infrastructure.interfaces.ivideo_handler import IVideoHandler
import cv2
import time

class VideoHandler(IVideoHandler):
    def __init__(self, videoSource=0):
        self._videoSource = videoSource
        self._cap = self.get_video()
        self._fourcc = cv2.VideoWriter_fourcc(*'XVID')

    def get_video(self):
        # Open a video capture object (0 for default camera)
        cap = cv2.VideoCapture(self._videoSource)
        return cap

    def read_frame(self):
        # Read a frame from the camera
        ret, frame = self._cap.read()
        if not ret:
            return ret, None
        
        return ret, frame

    def get_video_properties(self):
        # Get video properties
        width = int(self._cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(self._cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        fps = self._cap.get(cv2.CAP_PROP_FPS)

        return width, height, fps

    def show_video(self, frame, title="Video"):
        # Display the frame
        cv2.imshow(title, frame)

    def __start_recording(self):
        # Start recording 
        self._out = cv2.VideoWriter('output.mp4', self._fourcc, 20.0, (640, 480))

    def __stop_recording(self):
        # Stop recording
        self._out.release()

    def recorder(self, record, recording=False, extra_recording_start_time=0, extra_recording_seconds=5):
        if record:
            if not recording:
                # Start recording
                self.__start_recording()
                recording = True
                extra_recording_start_time = 0  # Reset extra recording start time
        else:
            if recording:
                # Check if extra recording time has elapsed
                if extra_recording_start_time == 0:
                    extra_recording_start_time = time.time()
                elapsed_time = time.time() - extra_recording_start_time
                if elapsed_time >= extra_recording_seconds:
                    # Stop recording
                    self.__stop_recording()
                    recording = False

    def __del__(self):
        # Release the video capture object and close the window
        self._cap.release()
        cv2.destroyAllWindows()
