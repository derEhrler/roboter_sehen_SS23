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

        while True:
            new_centroids = []
            for i in centroids:
                in_bandwidth = []
                centroid = centroids[i]
                for featureset in self.all_points:
                    if np.linalg.norm(featureset-centroid) < self.radius:
                        in_bandwidth.append(featureset)

                new_centroid = np.average(in_bandwidth,axis=0)
                new_centroids.append(tuple(new_centroid))

            uniques = sorted(list(set(new_centroids)))
            prev_centroids = dict(centroids)

            centroids = {}
            for i in range(len(uniques)):
                centroids[i] = np.array(uniques[i])

            optimized = True

            for i in centroids:
                if not np.array_equal(centroids[i], prev_centroids[i]):
                    optimized = False
                if not optimized:
                    break
                
            if optimized:
                break

        self.centroids = centroids
        return centroids
