import csv
import numpy as np

class GroupingBase:
    def __init__(self):
        self.data = []
        self.gts = []
        self.all_points = []

    def clear_data(self):
        self.gts = []
        self.all_points = []

    def load_2d_data(self, file_name, delimit=','):
        self.clear_data()
        with open(file_name, 'r') as f:
            data = list(csv.reader(f, delimiter=delimit))

        points_x = []
        points_y = []
        for i in data:
            points_x.append(float(i[0]))
            points_y.append(float(i[1]))
            self.gts.append(float(i[2]))

        # tuple to np array
        self.all_points = list(zip(points_x, points_y))
        self.all_points = np.array(self.all_points)

    def load_image_data(self, image_array):
        self.clear_data()
        self.all_points = image_array

