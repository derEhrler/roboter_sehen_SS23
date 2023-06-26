from RHMIcv.trackbars.trackbar import Trackbar

class HoughTrackbar(Trackbar):
    def __init__(self, filter_class, win_name="test"):
        Trackbar.__init__(self, filter_class, win_name)
        self.threshold_1 = 50
        self.threshold_2 = 50
        self.min_rad = 100
        self.max_rad = 500

    def execute_detector(self):
        self.filter_class.set_parameter(self.threshold_1, self.threshold_2, self.min_rad, self.max_rad)
        self.filter_class.set_image(self.orig_img)
        detected_circles = self.filter_class.hough_circles()
        output_image = self.filter_class.draw_circles(detected_circles)
        output_image.display(self.window_name, False)
        print("found circles:" + str(self.filter_class.count_circles(detected_circles)))

    def on_trackbar_threshold_1(self, val):
        if val <= 0:
            return
        self.threshold_1 = val
        self.execute_detector()

    def on_trackbar_threshold_2(self, val):
        if val <= 0:
            return
        self.threshold_2 = val
        self.execute_detector()

    def on_trackbar_min_radius(self, val):
        self.min_rad = val
        self.execute_detector()

    def on_trackbar_max_radius(self, val):
        self.max_rad = val
        self.execute_detector()
