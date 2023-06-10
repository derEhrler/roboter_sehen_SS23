import numpy as np
import cv2

from RHMIcv import utils
from RHMIcv.image import Image

from RHMIcv.filter.sobel_filter import SobelFilter
from RHMIcv.filter.canny_filter import CannyFilter
from RHMIcv.trackbars.trackbar_canny import CannyTrackbar

from RHMIcv.feature.hough_lines import HoughLinesDetector
from RHMIcv.feature.hough_circles import HoughCirclesDetector
from RHMIcv.trackbars.trackbar_hough_circles import HoughTrackbar

from RHMIcv.feature.harris_feature import HarrisFeature
from RHMIcv.feature.orb_feature import ORBFeature

SOBEL = False
CANNY = False
HOUGH_CV = False
HOUGH_SELF = True
HOUGH_CIRCLE_DEMO = True
HARRIS = True
ORB = True
APPLICATION_EXAMPLE = False

def main():
    # load and show the image
    img_1 = Image("data/IMG_6960.JPG", cv2.IMREAD_GRAYSCALE)
    img_sobel = Image("data/sobel_test.png", cv2.IMREAD_GRAYSCALE)
    img_muenzen = Image("data/muenzen.png")
    img_mika = Image("data/mika.png", cv2.IMREAD_GRAYSCALE)
    img_1.display("original image")

    # first exercise: the sobel filter
    if SOBEL is True:
        # implement sobel filter for different directions
        sobel_filter = SobelFilter(3)  # initialize the filter

        sobel_filter.set_directions(1, 0)  # x, y
        sobel_x_img = sobel_filter.filter(img_1)

        sobel_filter.set_directions(0, 1)
        sobel_y_img = sobel_filter.filter(img_1)

        utils.display_images(sobel_x_img.data, sobel_y_img.data, "x / y")
        sobel_both_img = sobel_filter.filter_both_sides(img_sobel)
        sobel_both_img.display("sobel both")

    # second exercise: canny filter with trackbar
    if CANNY is True:
        canny_filter = CannyFilter()  # initialize the filter
        canny_img = canny_filter.filter(img_1)
        canny_img.display("canny")
        canny_img = canny_filter.filter(img_sobel)
        canny_img.display("canny")

        trackbar = CannyTrackbar(canny_filter)  # initialize the filter
        trackbar.set_image(img_1)  # change image to test canny filter
        trackbar.trackbar_setup("kernel", trackbar.on_trackbar_kernel)
        trackbar.trackbar_setup("lower", trackbar.on_trackbar_min)
        trackbar.trackbar_setup("upper", trackbar.on_trackbar_max)
        cv2.waitKey(0)

    # third exercise a): Hough Lines Detector with OpenCV
    if HOUGH_CV is True:
        canny_filter = CannyFilter()
        canny_filter.set_parameter(400, 600, 3)
        filtered_image = canny_filter.filter(img_1)
        filtered_image.display("Kanten vom Canny-Filter")

        # compute the lines and display them
        hough_lines = HoughLinesDetector()
        hough_lines.set_image(filtered_image)
        lines_image = hough_lines.hough_lines_opencv(150)
        lines_image.display("Hough Lines")

    # third exercise b): Hough Lines Detector by yourself
    if HOUGH_SELF is True:
        canny_filter = CannyFilter()
        canny_filter.set_parameter(400, 600, 3)
        filtered_image = canny_filter.filter(img_1)
        filtered_image.display("Kanten vom Canny-Filter")

        # compute the lines and display them
        hough_lines = HoughLinesDetector()
        hough_lines.set_image(filtered_image)
        lines_image = hough_lines.hough_lines_self()
        lines_image.display("Hough Lines Self")

    # fourth exercise: hough circle detection with trackbar
    if HOUGH_CIRCLE_DEMO is True:
        hough_circles = HoughCirclesDetector()
        trackbar = HoughTrackbar(hough_circles)

        trackbar.set_image(img_muenzen)
        trackbar.trackbar_setup("threshold_1", trackbar.on_trackbar_threshold_1)
        trackbar.trackbar_setup("threshold_2", trackbar.on_trackbar_threshold_2)
        trackbar.trackbar_setup("min_rad", trackbar.on_trackbar_min_radius)
        trackbar.trackbar_setup("max_rad", trackbar.on_trackbar_max_radius)
        cv2.waitKey(0)

    if HARRIS is True:
        harris_detector = HarrisFeature()
        harris_detector.set_image(img_1)
        harris_corners = harris_detector.calc_keypoints()
        harris_corners.display("Harris keypoints")
        harris_corners = harris_detector.refined_keypoints()
        harris_corners.display("Harris keypoints refined")

    if ORB is True:
        orb_detector = ORBFeature()
        orb_detector.set_image(img_1)
        orb_detector.set_features(30)
        orb_detector.calc_keypoints()
        image_with_orb_points = orb_detector.draw_points(draw_orientation=True)

        rot_image = img_1
        rot_image.rotate(45)
        rows, cols = rot_image.data.shape
        rot_image.resize(cols * 1.2, rows)
        orb_detector.set_image(rot_image)
        orb_detector.calc_keypoints()
        image_with_orb_points_2 = orb_detector.draw_points(draw_orientation=True)
        utils.display_images(image_with_orb_points.data, image_with_orb_points_2.data, "orb")

    if APPLICATION_EXAMPLE is True:
        # start ...
        print("Need to be implemented")

        # ...end

if __name__ == '__main__':
    main()
