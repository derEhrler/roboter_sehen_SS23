import cv2
import numpy as np
import abc
from RHMIcv.image import Image

class FilterBase:
    def __init__(self, kernel_size=3):
        self.kernel_size = kernel_size

    @abc.abstractmethod
    def filter(self, image):
        """Filter the passed image."""
        pass
