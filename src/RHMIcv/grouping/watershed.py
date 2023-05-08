import numpy as np
import cv2

from RHMIcv.image import Image
from RHMIcv.grouping.grouping import GroupingBase

class WaterShed(GroupingBase):
    def __init__(self):
        GroupingBase.__init__(self)
        self.seed_points = []
        self.max_difference = 0

    def set_max_diff(self, diff):
        self.max_difference = diff

    def set_original_image(self, image):
        self.data = image.data

    def mouse_event(self, event, x, y, flags, params):
        if event == cv2.EVENT_LBUTTONDBLCLK:
            print("Got Seed Position:" + str(x) + ", " + str(y))
            s_box = y, x
            self.seed_points.append(s_box)

    def fill(self, start_coords):
        new_image = self.data.copy()
        visited = np.zeros((new_image.shape[0], new_image.shape[1], 1), np.uint8)
        # start ...
        print("Need to be implemented")

        # ... end
        return Image(new_image), Image(visited)
