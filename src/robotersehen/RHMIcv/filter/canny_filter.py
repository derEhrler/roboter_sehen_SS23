import cv2

from RHMIcv.image import Image
from RHMIcv.filter.filter import FilterBase

class CannyFilter(FilterBase):
    def __init__(self):
        FilterBase.__init__(self)
        self.lower_bound = 0
        self.upper_bound = 0

    def set_parameter(self, lower_bound, upper_bound, kernel_size):
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound
        self.kernel_size = kernel_size

    def filter(self, image):
        if image.data.size is 0:
            return image

        image_data = image.data.copy()
        # start ...
        print("Need to be implemented")

        # ... end

        return Image(output_image)
