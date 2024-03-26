from src.infrastructure.interfaces.imodel import IModel
import torch
from torch2trt import torch2trt
import torchvision
from torch2trt import TRTModule
import os

class Model(IModel):
    def __init__(self, example_frame, modelPath="vgg16_bn_trt.pth"):
        # Check if CUDA is available
        if torch.cuda.is_available():
            if not os.path.exists(modelPath):
                # Load the VGG16_bn model
                self._model =  torchvision.models.vgg16_bn(pretrained=True).cuda().half().eval()
                # Convert to TensorRT with example frame as input
                self._model_trt = torch2trt(self._model, [example_frame], fp16_mode=True)
                # Save the TensorRT model
                torch.save(self._model_trt.state_dict(), modelPath)
            else:
                # Load the pre-converted TensorRT model
                self._model_trt = TRTModule()
                self._model_trt.load_state_dict(torch.load(modelPath))
        else:
            raise RuntimeError("CUDA is not available, cannot use TensorRT")

    def Detect(self, frame):
        # Run inference on the source
        results = self._model_trt(frame).detach().cpu().numpy().flatten()
        return results