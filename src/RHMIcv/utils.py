import cv2
import numpy as np
from matplotlib import pyplot as plt
import glob
from RHMIcv.image import Image

def display_images(image1, image2, window_name="default"):
    numpy_horizontal_concat = np.concatenate((image1, image2), axis=1)
    cv2.imshow(window_name, numpy_horizontal_concat)
    cv2.waitKey(0)
    cv2.destroyWindow(window_name)

def display_map(plot_map, name):
    plt.title(str(name))
    plt.imshow(plot_map)
    plt.colorbar()
    plt.pause(0.01)
    plt.show()

def read_captured_images():
    filenames = glob.glob("data/capture/*")
    filenames.sort()
    images = []
    for filename in filenames:
        img = Image()
        img.load(filename, cv2.IMREAD_GRAYSCALE)
        images.append(img)

    print("loaded %d images" %len(images))
    return images
