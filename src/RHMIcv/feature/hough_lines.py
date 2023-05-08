import cv2
import math
import numpy as np

from RHMIcv.image import Image
from RHMIcv.feature.feature import FeatureBase

class HoughLinesDetector(FeatureBase):
    def __init__(self):
        FeatureBase.__init__(self)

    def hough_lines_opencv(self, threshold):
        if len(self.orig_img.data.shape) > 2:
            self.orig_img.data = cv2.cvtColor(self.orig_img.data, cv2.COLOR_BGR2GRAY)

        print("detecting lines by opencv")
        # start ...
        print("Need to be implemented")

        # ... end

        cdst = cv2.cvtColor(self.orig_img.data, cv2.COLOR_GRAY2BGR)
        if lines is None:
            print("No lines detected!")
            return Image(cdst)
        for i in range(0, len(lines)):
            rho = lines[i][0][0]
            theta = lines[i][0][1]
            pt1, pt2 = self.angles_to_points(rho, theta, 1000)
            cv2.line(cdst, pt1, pt2, (0, 0, 255), 3, cv2.LINE_AA)
        return Image(cdst)

    def hough_lines_self(self):
        if len(self.orig_img.data.shape) > 2:
            self.orig_img.data = cv2.cvtColor(self.orig_img.data, cv2.COLOR_BGR2GRAY)

        print("detecting lines by my self")
        accumulator, thetas, rhos = self.hough_lines_calc(self.orig_img.data)
        # start ...
        print("Need to be implemented")

        # ... end
        c_dst = cv2.cvtColor(self.orig_img.data, cv2.COLOR_GRAY2BGR)
        cv2.line(c_dst, pt1, pt2, (0, 0, 255), 3, cv2.LINE_AA)
        return Image(c_dst)

    @staticmethod
    def hough_lines_calc(img):
        # start ...
        print("Need to be implemented")

        # Rho and Theta ranges

        # Cache some reusable values

        # Hough accumulator array of theta vs rho

        # Vote in the hough accumulator

        # ... end
        return accumulator, thetas, rhos

    @staticmethod
    def angles_to_points(rho, theta, length):
        # start ...
        print("Need to be implemented")

        # ... end
        return pt1, pt2
