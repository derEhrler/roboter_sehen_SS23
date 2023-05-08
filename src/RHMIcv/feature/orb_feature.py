import cv2

from RHMIcv.image import Image
from RHMIcv.feature.feature import FeatureBase

class ORBFeature(FeatureBase):
    def __init__(self):
        FeatureBase.__init__(self)
        self.orb = cv2.ORB_create()
        self.keypoints = []

    def set_features(self, num_features):
        # start ...
        print("Need to be implemented")

        # ... end

    def calc_keypoints(self):
        # start ...
        print("Need to be implemented")

        # ... end

    def draw_points(self, draw_orientation=False):
        if draw_orientation is False:
            result_image = cv2.drawKeypoints(self.orig_img.data, self.keypoints, None)
        else:
            result_image = cv2.drawKeypoints(self.orig_img.data,
                                             self.keypoints, None, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

        return Image(result_image)
