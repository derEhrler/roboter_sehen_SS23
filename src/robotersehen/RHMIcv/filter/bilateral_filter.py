import cv2
from RHMIcv.filter.filter import FilterBase
from RHMIcv.image import Image

class BilateralFilter(FilterBase):
    def __init__(self, kernel_size=3, sigma_color=75, sigma_space=75):
        self.kernel_size = kernel_size
        self.sigma_color = sigma_color
        self.sigma_space = sigma_space

    def filter(self, image):
        image_copy = image.data.copy()

        image_data = cv2.bilateralFilter(image_copy, self.kernel_size, self.sigma_color, self.sigma_space)

        return Image(image_data)

