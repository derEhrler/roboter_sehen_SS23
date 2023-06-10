import numpy as np
from RHMIcv.filter.filter import FilterBase
from RHMIcv.image import Image

class HistogramEqualization(FilterBase):

    def filter(self, image):
        image_data = image.data.copy()

        # create zero array for the histogram
        bins = np.zeros(256, int)
        # return cv2.equalizeHist(img)  # test function from OpenCV
        # for loop, which iterates through the image
        for element in np.nditer(image_data):
            # has to be implemented from the student
            # start ...
            print("Need to be implemented")

            # ... end

        # compute the cumulative histogram
        # has to be implemented from the student
        # start ...
        print("Need to be implemented")

        # ... end

        # equalize the image
        rows, cols = image_data.shape
        for element in np.nditer(image_data, op_flags=['readwrite']):
            # has to be implemented from the student
            # start ...
            print("Need to be implemented")

            # ... end

        return Image(image_data)
