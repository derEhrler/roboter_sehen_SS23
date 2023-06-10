from RHMIcv.image import Image
import cv2
import numpy as np

# return object and image points
def detect_chessboard(images, num_x, num_y, square_size, show_images=True):
    # termination criteria
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

    # Arrays to store object points and image points from all the images.
    obj_points = []  # 3d point in real world space
    img_points = []  # 2d points in image plane.

    # prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
    obj_p = np.zeros((num_y * num_x, 3), np.float32)
    obj_p[:, :2] = np.mgrid[0:num_x, 0:num_y].T.reshape(-1, 2)
    obj_p *= square_size  # add the square size of the chessboard

    for img in images:
        image_data = img.data

        # start ...
        print("Need to be implemented")

        # Find the chess board corners and append them to the point lists

        # ... end

    # return object and image points
    return obj_points, img_points

def calibrate_intrinsic(obj_points, img_points, img):
    # start ...
    print("Need to be implemented")
    # start the calibration

    # ... end

    # return camera matrix K and the distortion parameters
    return K, dist_coeffs

def calibrate_extrinsic(obj_points, img_points, K, dist_coeffs):
    # start ...
    print("Need to be implemented")
    # start the calibration

    # ... end

    # return rotation matrix R and the translation vector t
    return R[0], tvecs
