import cv2
import numpy as np
from RHMIcv.filter.filter import FilterBase
from RHMIcv.image import Image

class SobelFilter(FilterBase):
    def __init__(self, kernel_size=3):
        FilterBase.__init__(self, kernel_size)
        self.direction_x = 1
        self.direction_y = 0

    def set_directions(self, x, y):
        self.direction_x = x
        self.direction_y = y

    def filter(self, image, image_type=cv2.CV_64F):
        img = image.data.copy()
        # start ...
        print("Need to be implemented")

        # ... end
        return Image(output_image)

    def filter_both_sides(self, image, image_type=cv2.CV_64F):
        # start ...
        print("Need to be implemented")

        # care of absolute values

        # ... end

        return Image(image_x + image_y)
