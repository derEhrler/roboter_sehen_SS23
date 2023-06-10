import abc
import numpy as np
from RHMIcv.filter.filter import FilterBase
from RHMIcv.image import Image

class MeanFilter(FilterBase):
    def filter(self, image):
        image_data = image.data.copy()
        new_image = image_data
        image_data  = np.pad(image_data, 1, 'edge')

        for rows in range(0,new_image.shape[0]):
            # new_image[rows,cols] = np.mean(image_data[rows:rows+2*padding_size,  cols:cols+2*padding_size])
            for cols in range(0,new_image.shape[1]):
                new_image[rows,cols] = np.mean(image_data[rows:rows+2, cols:cols+2])
            


        return Image(new_image)
