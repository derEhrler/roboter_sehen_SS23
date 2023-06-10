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
        output_image = cv2.Sobel(src=img, ddepth=cv2.CV_64F, dx=self.direction_x, dy=self.direction_y, ksize=self.kernel_size) # Combined X and Y Sobel Edge Detection 

        # ... end
        return Image(output_image)

    def filter_both_sides(self, image, image_type=cv2.CV_64F):
        img = image.data.copy()
        # start ...
        sobel_x = cv2.Sobel(src=img, ddepth=cv2.CV_64F, dx=1, dy=0, ksize=self.kernel_size) # Combined X and Y Sobel Edge Detection 

        sobel_y = cv2.Sobel(src=img, ddepth=cv2.CV_64F, dx=0, dy=1, ksize=self.kernel_size)
        # care of absolute values



        # ... end

        return Image(abs(sobel_x) + abs(sobel_y))
