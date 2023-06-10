import abc
import numpy as np
from RHMIcv.filter.filter import FilterBase
from RHMIcv.image import Image

class MeanFilter(FilterBase):

    def filter(self, image):
        image_data = image.data.copy()
        new_image = image_data

        # has to be implemented from the student
        # start ...
        print("Need to be implemented")

        # ... end

        return Image(new_image)
