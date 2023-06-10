import numpy as np
import cv2

from RHMIcv import utils
from RHMIcv.image import Image
from RHMIcv.calib import calib

IMAGE_CAPTURE = False
CALIBRATION = False
DISTORTION_CORRECTION = False
EXTRINSIC_CALIBRATION = True

def main():
    # define chessboard properties
    num_x = 10  # number of corners in x direction (vertical)
    num_y = 7  # number of corners in y direction (horizontal)
    square_size = 20  # size in mm of a square from the calibration target

    if IMAGE_CAPTURE is True:
        image = Image()
        cap = cv2.VideoCapture(0)  # Define general video driver

        count = 0
        while True:
            ret, frame = cap.read()  # Capture frame-by-frame

            image.data = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            image.display("live stream", False)
            key = cv2.waitKey(1)
            if key == ord('q'):
                break
            elif key == ord('s'):
                image_file = "image" + str(count) + ".png"
                print("Write image: " + image_file)
                image.save("data/capture/" + image_file)
                count += 1

        # When everything done, release the capture
        cap.release()
        cv2.destroyAllWindows()

    if CALIBRATION is True:
        calib_images = utils.read_captured_images()  # read all images inside the folder "data/capture"

        # detect all chessboards and get the object and image points
        obj_pts, img_pts = calib.detect_chessboard(calib_images, num_x, num_y, square_size, show_images=True)

        # calibrate and get the camera matrix and the distortion parameters
        K, dist_coeffs = calib.calibrate_intrinsic(obj_pts, img_pts, calib_images[0])
        # save and print the calibration
        cv_file = cv2.FileStorage("calib.xml", cv2.FILE_STORAGE_WRITE)
        cv_file.write("K", K)
        cv_file.write("dist_coeffs", dist_coeffs)
        cv_file.release()
        print("K: ", K)
        print("distortion coefficients: ", dist_coeffs)

    if DISTORTION_CORRECTION is True:
        calib_images = utils.read_captured_images()  # read all images inside the folder "data/capture"
        # read the calibration
        cv_file = cv2.FileStorage("calib.xml", cv2.FILE_STORAGE_READ)
        K = cv_file.getNode("K").mat()
        dist_coeffs = cv_file.getNode("dist_coeffs").mat()

        # test the calibration with the input images, discuss the changes
        for img in calib_images:
            img.undistort(K, dist_coeffs)
            img.display("undistorted")
            cv2.waitKey(0)

    if EXTRINSIC_CALIBRATION is True:
        # read the calibration
        cv_file = cv2.FileStorage("calib.xml", cv2.FILE_STORAGE_READ)
        K = cv_file.getNode("K").mat()
        dist_coeffs = cv_file.getNode("dist_coeffs").mat()
        # read and undistort the images
        images = utils.read_captured_images()  # read all images inside the folder "data/capture"
        for img in images:
            img.undistort(K, dist_coeffs)
        image = [images[0]]  # take the first image for the extrinsic calibration

        # perform the extrinsic calibration and get the pose of the board to the camera
        # detect all chessboards and get the object and image points
        obj_pts, img_pts = calib.detect_chessboard(image, num_x, num_y, square_size)
        R, t = calib.calibrate_extrinsic(obj_pts, img_pts, K, dist_coeffs)
        print("R: ", R)
        print("t: ", t)

if __name__ == '__main__':
    main()
