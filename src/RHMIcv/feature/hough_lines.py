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

        # start ...
        #lines = cv2.HoughLines(self.orig_img.data, threshold)
        #lines = cv2.HoughLines(self.orig_img.data, rho, 180, threshold)
        lines = cv2.HoughLines(self.orig_img.data, 1,np.pi/180,threshold)
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
        index = np.argmax(accumulator)

        rho = rhos[int(index / accumulator.shape[0])]
        theta = thetas[index % accumulator.shape[1]]

        pt1, pt2 = self.angles_to_points(rho, theta, 1000)

        # ... end
        c_dst = cv2.cvtColor(self.orig_img.data, cv2.COLOR_GRAY2BGR)
        cv2.line(c_dst, pt1, pt2, (0, 0, 255), 3, cv2.LINE_AA)
        return Image(c_dst)

    @staticmethod
    def hough_lines_calc(img):
        # start ...
        # Rho and Theta ranges
        thetas = np.deg2rad(np.arange(-90.0, 90.0))
        width, height = img.shape
        diag_len = np.ceil(np.sqrt(width * width + height * height))   # max_dist
        rhos = np.linspace(int(-diag_len), int(diag_len), int(diag_len * 2.0))

        # Cache some resuable values
        cos_t = np.cos(thetas)
        sin_t = np.sin(thetas)
        num_thetas = len(thetas)

        # Hough accumulator array of theta vs rho
        accumulator = np.zeros((int(2 * diag_len), int(num_thetas)), dtype=np.uint64)
        y_idxs, x_idxs = np.nonzero(img)  # (row, col) indexes to edges

        # Vote in the hough accumulator
        for i in range(len(x_idxs)):
            x = x_idxs[i]
            y = y_idxs[i]

            for t_idx in range(num_thetas):
                # Calculate rho. diag_len is added for a positive index
                rho = round(x * cos_t[t_idx] + y * sin_t[t_idx]) + diag_len
                accumulator[int(rho), int(t_idx)] += 1

        return accumulator, thetas, rhos

    @staticmethod
    def angles_to_points(rho, theta, length):
        # start ...
        y1 = rho * np.sin(theta)
        x1 = rho * np.cos(theta)

        nx = y1 / rho * length
        ny = -x1 / rho * length

        y2 = y1 + ny
        x2 = x1 + nx

        pt1 = (int(x1), int(y1))
        pt2 = (int(x2), int(y2))

        # ... end
        return pt1, pt2
