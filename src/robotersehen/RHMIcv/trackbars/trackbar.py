import cv2

from RHMIcv.image import Image

class Trackbar:
    def __init__(self, filter_class, win_name="trackbar"):
        self.window_name = win_name
        self.filter_class = filter_class
        self.orig_img = Image()

    def set_image(self, input_image):
        self.orig_img = input_image

    def trackbar_setup(self, bar_name, on_trackbar_function, min_val=1, max_val=700):
        cv2.namedWindow(self.window_name, cv2.WINDOW_NORMAL)
        cv2.resizeWindow(self.window_name, self.orig_img.data.shape[1], self.orig_img.data.shape[0])
        cv2.createTrackbar(bar_name, self.window_name, min_val, max_val, on_trackbar_function)
