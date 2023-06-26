import numpy as np
import cv2

from RHMIcv import utils
from RHMIcv.image import Image
from RHMIcv.stereo.stereo_geometry import StereoGeometry
from RHMIcv.stereo import stereo

FUNDAMENTAL_MATRIX = True
TRIANGULATION = True
DISPARITY = True
np.set_printoptions(precision=2)

def main():
    stereo_geo = StereoGeometry()

    image_left = Image("data/stereo/umbrellaLeft.png", 0)
    image_right = Image("data/stereo/umbrellaRight.png", 0)
    calib = stereo.read_calib("data/stereo/umbrellaCalib.txt")
    # image_left = Image("data/stereo/bicycleLeft.png", 0)
    # image_right = Image("data/stereo/bicycleRight.png", 0)
    # calib = stereo.read_calib("data/stereo/bicycleCalib.txt")
    # image_left = Image("data/stereo/pianoLeft.png", 0)
    # image_right = Image("data/stereo/pianoRight.png", 0)
    # calib = stereo.read_calib("data/stereo/pianoCalib.txt")

    K_left = calib['cam0']
    K_right = calib['cam1']
    baseline = float(calib['baseline'])

    # find point correspondents
    points_left, points_right = stereo_geo.find_keypoints(image_left, image_right, True)

    if FUNDAMENTAL_MATRIX:  # Task 1
        print("K left: ", K_left)
        print("K right: ", K_right)

        # --- estimate as first with the OpenCV Lib ---
        F_estimated = stereo.estimate_fundamental_matrix(points_left, points_right)

        # --- calculate F as second from the equation in the letters ---
        # define rotation and translation matrix
        # start ...
        R = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
        t = np.array([baseline, 0, 0])
        # ... end
        F_calculated = stereo.calc_fundamental_matrix(K_left, K_right, R, t)

        # print the resulting matrices and display the corresponding epipolar lines
        print("F estimated: ", F_estimated)
        print("F calculated: ", F_calculated)
        stereo_geo.compute_correspond_epilines(image_left, image_right, points_left, points_right, F_calculated)

    if TRIANGULATION:  # Task 2
        # call the point triangulation function of the stereo.py file
        stereo.triangulate(baseline, K_left, K_right, points_left, points_right)

    if DISPARITY:  # Task 3
        # resize images
        rows, cols = image_left.data.shape
        scale = 0.5
        image_left.resize(cols * scale, rows * scale)
        image_right.resize(cols * scale, rows * scale)
        cv2.imshow("image", image_left.data)

        # calculate disparities
        # test different disparity and block sizes
        # num_disparity must be dividable by 16, block size  has to be a kernel: 9, 16, 25, 36
        disparity = stereo.compute_disparity_map(image_left, image_right, 112, 25)
        utils.display_map(disparity, 'disparity map')

        # calculate depth map
        print('calculate depth map')
        f = K_left[0, 0]
        # calculate depth map from disparity
        depth = stereo.compute_depth_map(disparity, f, baseline)

        print('display depth map')
        utils.display_map(depth, 'depth map')
        cv2.waitKey(0)

if __name__ == '__main__':
    main()
