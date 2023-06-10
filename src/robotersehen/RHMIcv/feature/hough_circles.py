import cv2

import numpy as np

from RHMIcv.image import Image
from RHMIcv.feature.feature import FeatureBase

class HoughCirclesDetector(FeatureBase):
    def __init__(self):
        FeatureBase.__init__(self)
        self.threshold_1 = 50
        self.threshold_2 = 50
        self.min_rad = 100
        self.max_rad = 500

    def set_parameter(self, par1=50, par2=50, min_radius=100, max_radius=500):
        self.threshold_1 = par1
        self.threshold_2 = par2
        self.min_rad = min_radius
        self.max_rad = max_radius

    def hough_circles(self):
        if len(self.orig_img.data.shape) > 2:
            self.orig_img.data = cv2.cvtColor(self.orig_img.data, cv2.COLOR_BGR2GRAY)

        # start ...
        print("Need to be implemented")

        # ... end

        return circles

    def draw_circles(self, circles):
        if circles is not None:
            circles = np.uint16(np.around(circles))
            image_to_draw = self.orig_img.data.copy()
            for i in circles[0, :]:
                # draw the outer circle
                cv2.circle(image_to_draw, (i[0], i[1]), i[2], (0, 255, 0), 2)
                # draw the center of the circle
                cv2.circle(image_to_draw, (i[0], i[1]), 2, (0, 0, 255), 3)
            return Image(image_to_draw)
        else:
            return Image(self.orig_img.data.copy())

    @staticmethod
    def count_circles(circles):
        if circles is not None:
            number = len(circles[0, :])
            return number
        else:
            return 0
