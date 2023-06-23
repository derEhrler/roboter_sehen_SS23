import numpy as np
import random
import math

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

    def group(self, k, max_iterations=1000, dimension=2, datapoints=None, Trials=10):
        # start ...
        print("Need to be implemented")
        if datapoints == None:
            return []

        # Limit iterations
        self.trials = Trials
        self.variance = []
        np.array(self.variance)

        for episodes in range(self.trials):
            self.cluster_centers = random.choice(datapoints, k)
            self.cluster = np.arange(k)
            variancesum = 0

            for step in range(max_iterations):
                for i in range(len(datapoints)):
                    idx = np.argmin(math.dist(self.cluster_centers, datapoints[i]))
                    self.cluster[idx].np.append(datapoints[i])
            
            for x in cluster:
                variancesum += self.cluster[x]
            
            self.variance.append(variancesum)

        print("Best Cluster points, with lowest variance is cluster", self.cluster[np.argmax(self.variance)])

        # Randomly Choose Centers for the Clusters

        # ... end
        return [self.cluster, np.array(self.cluster_centers)]
    
if __name__ == "__init__":  # Konnte noch nicht getestet werden
    KMeansAgent = KMeans()
    datapoints = list(random.random() for i in range (20))
    [cluster, cluster_centers] = KMeansAgent.group(3)
    print(cluster_centers)
