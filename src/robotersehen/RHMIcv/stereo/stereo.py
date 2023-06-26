from RHMIcv.image import Image
import cv2
import numpy as np
import csv

def estimate_fundamental_matrix(points_left, points_right):
    # estimate the fundamental matrix from point correspondents
    F = np.zeros((1, 1), int)
    pts1 = np.int32(points_left)
    pts2 = np.int32(points_right)

    # start ...
    print("Need to be implemented")

    # ... end

    return F

def calc_fundamental_matrix(K_left, K_right, R, t, print_matrices=False):
    # calculate the fundamental matrix from the equation
    F = np.zeros((1, 1), int)

    if print_matrices:
        print("R: ", R)
        print("t: ", t)
        print("K_left: ", K_left)
        print("K_right: ", K_right)

    # start ...
    print("Need to be implemented")

    # ... end
    return F

def triangulate(baseline, K_left, K_right, points_left, points_right):
    P_left = np.zeros((3, 4), int)
    P_right = np.zeros((3, 4), int)
    X = 0  # variable for output 3D points

    # start ...
    print("Need to be implemented")

    # define R and t from the passed parameter

    # calculate the projection matrices

    # calculate the triangulation

    # ... end

    print("Pl: ", P_left)
    print("Pr: ", P_right)

    return Xs

def compute_disparity_map(img_left, img_right, num_disparities, block_size):
    # start ...
    print("Need to be implemented")

    # ... end
    return disparity

def compute_depth_map(disparity_map, f, baseline):
    depth = disparity_map.copy()
    # calculate depth value from disparity
    with np.nditer(depth, op_flags=['readwrite']) as it:
        for x in it:
            # start ...

            x[...] = baseline * f / x
            # ... end

    return depth

def read_calib(calib_file_path):
    with open(calib_file_path, 'r') as calib_file:
        calib = {}
        csv_reader = csv.reader(calib_file, delimiter='=')
        for attr, value in csv_reader:
            calib.setdefault(attr, value)

    calib['cam0'] = calib['cam0'].replace('[', '')
    calib['cam0'] = calib['cam0'].replace(']', '')
    calib['cam1'] = calib['cam1'].replace('[', '')
    calib['cam1'] = calib['cam1'].replace(']', '')
    calib['cam0'] = calib['cam0'].replace(';', '')
    calib['cam1'] = calib['cam1'].replace(';', '')

    calib['cam0'] = np.fromstring(calib['cam0'], dtype=float, sep=' ').reshape((3, 3))
    calib['cam1'] = np.fromstring(calib['cam1'], dtype=float, sep=' ').reshape((3, 3))

    np.fromstring(calib['cam0'], dtype=float, sep=' ')

    return calib
