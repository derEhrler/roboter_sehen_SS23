import numpy as np
from RHMIcv.filter.filter import FilterBase
from RHMIcv.image import Image
from matplotlib import pyplot as plt

class HistogramEqualization(FilterBase):

    def filter(self, image):
        image_data = image.data.copy()

        # create zero array for the histogram
        bins = np.zeros(256, int)
        # return cv2.equalizeHist(img)  # test function from OpenCV
        # for loop, which iterates through the image
        # compute the cumulative histogram
        for element in np.nditer(image_data):
            bins[element:256] +=1

        # equalize the image
        rows, cols = image_data.shape
        for element in np.nditer(image_data, op_flags=['readwrite']):
            # has to be implemented from the student
            element[...] = bins[element] / (rows*cols) * 255


        return Image(image_data)
