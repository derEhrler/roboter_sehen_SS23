from RHMIcv.trackbars.trackbar import Trackbar

class CannyTrackbar(Trackbar):
    def __init__(self, filter_class, win_name="test"):
        Trackbar.__init__(self, filter_class, win_name)
        self.kernel_size = 3
        self.lower_bound = 1
        self.upper_bound = 1

    def execute_filter(self):
        # start ...
        
        self.filter_class.set_parameter(self.lower_bound, self.upper_bound, self.kernel_size)
        filtered_image = self.filter_class.filter(self.orig_img)
        filtered_image.display(self.window_name, False)
        # ... end

    def on_trackbar_kernel(self, val):   
        self.kernel_size = val
        self.execute_filter()

    def on_trackbar_min(self, val):
        self.lower_bound = val
        self.execute_filter()

    def on_trackbar_max(self, val):
        self.upper_bound = val
        self.execute_filter()
