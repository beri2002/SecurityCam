from src.infrastructure.interfaces.ipreprocess import IPreProcess
import cv2
import numpy as np
import torchvision
import torch

class PreProcess(IPreProcess):

    def __init__(self):
        self._device = torch.device('cuda')
        self._mean = 255.0 * np.array([0.485, 0.456, 0.406])
        self._stdev = 255.0 * np.array([0.229, 0.224, 0.225])

        self._normalize = torchvision.transforms.Normalize(self._mean, self._stdev)

    def __resize(self, image, size=(244, 244)):
        # Resize the image
        return cv2.resize(image, size)

    def __BGR2RGB(self, image):
        # Convert the frame from BGR to RGB
        return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    def __transpose(self, image):
        # Transpose the image array
        return image.transpose((2, 0, 1))

    def __to_tensor(self, image):
        # Convert the numpy array to a PyTorch tensor
        return torch.from_numpy(image).float()

    def __normalize(self, image):
        # Normalize the image
        return self._normalize(image)

    def __move_to_device(self, image):
        # Move the image tensor to the specified device
        return image.to(self._device)

    def __add_batch_dimension(self, image):
        # Add a batch dimension to the image tensor
        return image[None, ...]
    
    def __half_precision(self, image):
        # Convert image tensor to half precision (float16)
        return image.half()

    def preprocess(self, image):
        # Resize the image
        image = self.__resize(image)
        # Convert BGR to RGB
        image = self.__BGR2RGB(image)
        # Transpose dimensions
        image = self.__transpose(image)
        # Convert to PyTorch tensor
        image = self.__to_tensor(image)
        # Normalize
        image = self.__normalize(image)
        # Move to device
        image = self.__move_to_device(image)
        # Add batch dimension
        image = self.__add_batch_dimension(image)
        # Convert to half precision
        image = self.__half_precision(image)
        
        return image
