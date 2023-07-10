from RHMIcv.image import Image
import cv2 as cv
import numpy as np
import csv
import numpy.linalg as lg
from matplotlib import pyplot as plt

def estimate_fundamental_matrix(points_left, points_right):
    # estimate the fundamental matrix from point correspondents
    F = np.zeros((1, 1), int)
    pts1 = np.int32(points_left)
    pts2 = np.int32(points_right)

    F, mask = cv.findFundamentalMat(pts1,pts2, cv.FM_LMEDS)

    pts1 = pts1[mask.ravel()==1]
    pts2 = pts2[mask.ravel()==1]

    return F

def calc_fundamental_matrix(K_left, K_right, R, t, print_matrices=False):
    # calculate the fundamental matrix from the equation
    F = np.zeros((1, 1), int)

    if print_matrices:
        print("R: ", R)
        print("t: ", t)
        print("K_left: ", K_left)
        print("K_right: ", K_right)

    E = np.matmul(t,R)
    K_right = np.transpose(lg.inv(K_right))
    F = np.matmul(np.matmul(K_right,E),lg.inv(K_left))


    return F

def triangulate(baseline, K_left, K_right, points_left, points_right):
    P_left = np.zeros((3, 4), int)
    P_right = np.zeros((3, 4), int)
    X = []  # variable for output 3D points

    t = np.array([baseline,0,0])

    R = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])

    # start ...
    print("Need to be implemented")

    # define R and t from the passed parameter

    P_left = np.matmul(K_left,np.insert(R,[3],t))
    P_right = np.matmul(K_right,np.insert([3],t))

    # calculate the projection matrices

    X.append(np.matmul([points_left,1],lg.inv(P_left)))
    X.append(np.matmul([points_right,1],lg.inv(P_right))) 

    # calculate the triangulation

    # ... end

    print("Pl: ", P_left)
    print("Pr: ", P_right)

    return X

def compute_disparity_map(img_left, img_right, num_disparities, block_size):

    stereo = cv.StereoBM_create(numDisparities=16, blockSize=block_size)
    disparitiy = stereo.compute(img_left,img_right)
    plt.imshov(disparitiy,'gray')
    plt.show()

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
