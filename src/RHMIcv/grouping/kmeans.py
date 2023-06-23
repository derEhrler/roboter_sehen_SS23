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

    def group(self, k, max_iterations=1000, dimension=2, Trials=10):
        # start ...
        print("Need to be implemented")
        if self.all_points == None:
            return []

        # Limit iterations
        self.trials = Trials
        self.variance = []
        np.array(self.variance)

        for episodes in range(self.trials):                             # Main Loop for finding optimal cluster Centers
            self.cluster_centers = random.choice(self.all_points, k)    # Pick k new random cluster centers
            self.cluster = np.arange(k)                                 # Initialize k new cluster
            variancesum = 0

            for step in range(max_iterations):                          # Subloop for each Episode
                for i in range(len(datapoints)):                        # Do for each Datapoint
                    idx = np.argmin(math.dist(self.cluster_centers, datapoints[i])) # Find min distance to cluster center
                    self.cluster[idx].np.append(datapoints[i])          # Add to corresponding cluster

                self.cluster_centers = np.mean(self.cluster)            # Calculate new cluster centers

            for x in self.cluster:                                      # Add variance for each cluster center
                variancesum += np.var(self.cluster[x])
            
            self.variance.append(variancesum)                           # Add variance for this episode to array

        print("Best Cluster centers with lowest variance are", self.cluster[np.argmax(self.variance)])  # Output cluster with lowest variance


        return [self.cluster, np.array(self.cluster_centers)]
    

    def group2(self, k, max_iterations=1000, dimension=2, Trials = 10):
        self.centroids = random.choice(self.all_points) 
        iteration = 0
        prev_centroids = None
        for episodes in range(Trials):
            
            variancesum = 0

            while np.not_equal(self.centroids, prev_centroids).any() and iteration < self.max_iter:
                if iteration >= max_iterations:
                    break
                sorted_points = [[] for _ in range(self.n_clusters)]
                for x in self.all_points:
                    dists = math.dist(x, self.centroids)
                    centroid_idx = np.argmin(dists)
                    sorted_points[centroid_idx].append(x)         
                prev_centroids = self.centroids
                self.centroids = [np.mean(cluster, axis=0) for cluster in sorted_points]
                for i, centroid in enumerate(self.centroids):
                    if np.isnan(centroid).any():  
                        self.centroids[i] = prev_centroids[i]
                iteration += 1
            
            for x in self.cluster:                                      # Add variance for each cluster center
                variancesum += np.var(self.cluster[x])
            
            self.variance.append(variancesum)                           # Add variance for this episode to array

        print("Best Cluster centers with lowest variance are", self.cluster[np.argmax(self.variance)])  # Output cluster with lowest variance

        return [self.cluster, np.array(self.cluster_centers)]
if __name__ == "__init__":  # Konnte noch nicht getestet werden
    KMeansAgent = KMeans()
    datapoints = list(random.random() for i in range (20))
    [cluster, cluster_centers] = KMeansAgent.group(3)
    print(cluster_centers)
