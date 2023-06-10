import cv2
import matplotlib.pyplot as plt

from RHMIcv.image import Image

from RHMIcv.grouping.kmeans import KMeans
from RHMIcv.grouping.watershed import WaterShed
from RHMIcv.grouping.mean_shift import MeanShift

KMEANS2D = True
KMEANSIMAGE = False
WATERSHED = False
MEANSHIFT = False

def main():

    if KMEANS2D is True:
        kmean = KMeans()
        # kmean.load_2d_data("data/2Ddata/aggregation.csv")
        # kmean.load_2d_data("data/2Ddata/d31.csv")
        # kmean.load_2d_data("data/2Ddata/spiral.csv")
        kmean.load_2d_data("data/2Ddata/r15.csv")

        cluster, centroids = kmean.group(8)  # test different number of centers

        # Plot the data and the centers generated as random
        plt.scatter(kmean.all_points[:, 0], kmean.all_points[:, 1], c=cluster, s=10)
        plt.scatter(centroids[:, 0], centroids[:, 1], marker='*', c='y', s=100)
        plt.show()

    if KMEANSIMAGE is True:
        orig_img = Image("data/small_kmeans.jpg", 0)
        orig_img.display("original image")

        kmean = KMeans()
        kmean.load_image_data(orig_img.get_array())

        cluster, centroids = kmean.group(5, dimension=1)
        new_image = Image(kmean.groups_to_image(cluster, centroids, orig_img.data))
        new_image.display("K-Means image")

    if WATERSHED is True:
        # load and show the image
        orig_img = Image("data/Panda_Arm.jpg", 0)
        # orig_img = Image("data/IMG_6960.JPG", 0)
        resized = Image(cv2.resize(orig_img.data, (640, 480)))

        watershed = WaterShed()  # initialize WaterShed
        watershed.set_original_image(resized)
        watershed.set_max_diff(15)

        resized.display("WaterShed original image", False)
        cv2.setMouseCallback("WaterShed original image", watershed.mouse_event, 0)
        print("Left mouse double click to define start position, press key to start WaterShed.")
        cv2.waitKey()

        print("Starting region growing based on last click")
        print(watershed.seed_points)
        new_image, visited = watershed.fill(watershed.seed_points[-1])

        new_image.display("tested")
        visited.display("visited")
        cv2.destroyAllWindows()

    if MEANSHIFT is True:
        radius = 0.3

        mean_shift = MeanShift(radius)
        # mean_shift.load_2d_data("data/2Ddata/aggregation.csv")
        # mean_shift.load_2d_data("data/2Ddata/d31.csv")
        # mean_shift.load_2d_data("data/2Ddata/spiral.csv")
        mean_shift.load_2d_data("data/2Ddata/r15.csv")
        centroids = mean_shift.fit()

        plt.scatter(mean_shift.all_points[:, 0], mean_shift.all_points[:, 1], s=10)
        for c in centroids:
            plt.scatter(centroids[c][0], centroids[c][1], color='k', marker='*', s=150)
        plt.show()

if __name__ == '__main__':
    main()
