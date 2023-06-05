import os
import cv2
import numpy as np
from matplotlib import pyplot as plt

class Image:
    def __init__(self, image=None, variant=-1):
        if image is None:
            self.data = np.zeros((1, 1), int)
        elif isinstance(image, str) and os.path.isfile(image):
            self.load(image, variant)
        else:
            self.data = image
        self.K = np.identity(3)
        self.dist_coeffs = 0

    def set_data(self, image):
        self.data = image

    def load(self, image_path, variant=-1):
        self.data = cv2.imread(image_path, variant)

    def save(self, image_path):
        cv2.imwrite(image_path, self.data)

    def display(self, window_name="default", destroyable=True):
        cv2.imshow(window_name, self.data)
        if destroyable is True:
            cv2.waitKey(0)
            cv2.destroyWindow(window_name)

    def display_histogram(self):
        # create zero array for the histogram
        bins = np.zeros(256, int)

        # for loop, which iterates through the image
        for element in np.nditer(self.data):
            # has to be implemented from the student
            # start ...
            # print("Need to be implemented")
            bins[element] += 1
            # ... end

        # plot the resulting histogram normalized
        bins = bins / np.linalg.norm(bins)
        plt.plot(bins, 'b')
        plt.xlim([0, 256])
        plt.show()

    def add_noise(self, noise_typ):
        if noise_typ == "gauss":
            mean = 2.5
            var = 15
            sigma = var ** 0.5

            if self.data.ndim > 2:
                row, col, ch = self.data.shape
                gauss = np.random.normal(mean, sigma, (row, col, ch))
                gauss = gauss.reshape(row, col, ch)
            else:
                row, col = self.data.shape
                gauss = np.random.normal(mean, sigma, (row, col))
                gauss = gauss.reshape(row, col)

            noisy = self.data + gauss.astype(np.uint8)
            self.data = noisy
        elif noise_typ == "s&p":
            s_vs_p = 0.5
            amount = 0.004
            out = np.copy(self.data)
            # Salt mode
            num_salt = np.ceil(amount * self.data.size * s_vs_p)
            coords = [np.random.randint(0, i - 1, int(num_salt)) for i in self.data.shape]
            out[tuple(coords)] = 1
            # Pepper mode
            num_pepper = np.ceil(amount * self.data.size * (1. - s_vs_p))
            coords = [np.random.randint(0, i - 1, int(num_pepper)) for i in self.data.shape]
            out[tuple(coords)] = 255
            self.data = out
        elif noise_typ == "poisson":
            values = len(np.unique(self.data))
            values = 2 ** np.ceil(np.log2(values))
            noisy = np.random.poisson(self.data * values) / float(values)
            self.data = noisy.astype(np.uint8)
        elif noise_typ == "speckle":
            if self.data.ndim > 2:
                row, col, ch = self.data.shape
                gauss = np.random.rand(row, col, ch) * 0.2
                gauss = gauss.reshape(row, col, ch)
            else:
                row, col = self.data.shape
                gauss = np.random.rand(row, col) * 0.2
                gauss = gauss.reshape(row, col)

            noisy = self.data + self.data * gauss
            self.data = noisy.astype(np.uint8)

    def resize(self, height, width, interpolation=cv2.INTER_CUBIC):
        self.data = cv2.resize(self.data, (int(height), int(width)), interpolation)

    def rotate(self, angle):
        rows = self.data.shape[0]
        cols = self.data.shape[1]
        m = cv2.getRotationMatrix2D((cols / 2, rows / 2), angle, 1)
        self.data = cv2.warpAffine(self.data, m, (cols, rows))

    def get_array(self):
        if len(self.data.shape) > 2:
            image_data = np.array(cv2.cvtColor(self.data, cv2.COLOR_BGR2GRAY))
        else:
            image_data = np.array(self.data)
        flattened = image_data.flatten()
        return np.array(flattened)

    def undistort(self, K, coeffs):
        # start ...
        h,  w = self.data.shape[:2]
        newcameramtx, roi = cv2.getOptimalNewCameraMatrix(K, coeffs, (w,h), 1, (w,h))
        self.data = cv2.undistort(self.data, newcameramtx, coeffs)
        #x, y, w, h = roi
        #self.data = self.data[y:y+h, x:x+w]
        #cv2.imwrite('calibresult.png', dst)
        # ... end
