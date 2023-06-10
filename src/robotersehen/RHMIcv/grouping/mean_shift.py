import numpy as np

from RHMIcv.grouping.grouping import GroupingBase

class MeanShift(GroupingBase):
    def __init__(self, radius=0.5):
        GroupingBase.__init__(self)
        self.radius = radius  # How far to look for neighbours.

    def fit(self):
        centroids = {}

        # set start cluster from each point
        for i in range(len(self.all_points)):
            centroids[i] = self.all_points[i]

        # start ...
        print("Need to be implemented")

        # ... end
        return centroids
