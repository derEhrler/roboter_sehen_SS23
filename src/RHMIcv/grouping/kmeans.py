import numpy as np
import random

import cv2

from RHMIcv.grouping.grouping import GroupingBase

class KMeans(GroupingBase):
    def __init__(self):
        GroupingBase.__init__(self)
        self.gts = []
        self.all_points = []

    def groups_to_image(self, cluster, centroids, image):
        new_points = self.all_points
        if len(image.shape) > 2:
            image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        for i in range(0, len(new_points + 1)):
            new_points[i] = centroids[cluster[i]]
        return np.reshape(new_points, (image.shape[0], image.shape[1]))

    def group(self, k, max_iterations=1000, dimension=2):
        # start ...
        print("Need to be implemented")

        # Limit iterations

        # Randomly Choose Centers for the Clusters

        # ... end
        return [cluster, np.array(cluster_centers)]
