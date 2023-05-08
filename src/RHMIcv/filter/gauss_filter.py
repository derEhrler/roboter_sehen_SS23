import cv2
import numpy as np
from RHMIcv.filter.filter import FilterBase
from RHMIcv.image import Image

class GaussFilter(FilterBase):
    def __init__(self, kernel_size=3, sigma_x=0, sigma_y=0):
        self.kernel_size = kernel_size
        self.sigma_x = sigma_x
        self.sigma_y = sigma_y

    def filter(self, image):
        image_copy = image.data.copy()

        image_data = cv2.GaussianBlur(image_copy, (self.kernel_size, self.kernel_size), self.sigma_x, self.sigma_y)

        return Image(image_data)
