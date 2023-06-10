from RHMIcv.image import Image

class FeatureBase:
    def __init__(self):
        self.orig_img = Image()

    def set_image(self, input_image):
        self.orig_img = input_image
