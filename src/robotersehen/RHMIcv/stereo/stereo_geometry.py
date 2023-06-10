import cv2
import numpy as np

from RHMIcv.image import Image
from RHMIcv.stereo import stereo
from matplotlib import pyplot as plt

class StereoGeometry:
    def find_keypoints(self, img1, img2, draw_matches = False):

        # Initiate ORB detector
        orb = cv2.ORB_create()

        # find the keypoints and descriptors with SIFT
        kp1, des1 = orb.detectAndCompute(img1.data, None)
        kp2, des2 = orb.detectAndCompute(img2.data, None)

        good = []
        pts1 = []
        pts2 = []

        # create BFMatcher object
        bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
        # Match descriptors.
        matches = bf.match(des1, des2)
        # Sort them in the order of their distance.
        matches = sorted(matches, key=lambda x: x.distance)

        if draw_matches:
            img3 = cv2.drawMatches(img1.data, kp1, img2.data, kp2, matches[:50], None,
                                   flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
            plt.imshow(img3), plt.show()

        for i in range(0, 50, 1):
            mat = matches[i]
            img1_idx = mat.queryIdx
            img2_idx = mat.trainIdx
            pts1.append(kp1[img1_idx].pt)
            pts2.append(kp2[img2_idx].pt)

        return pts1, pts2

    def draw_lines(self, image_left, image_right, lines, pts1, pts2):
        r, c = image_left.data.shape
        img1 = cv2.cvtColor(image_left.data, cv2.COLOR_GRAY2BGR)
        img2 = cv2.cvtColor(image_right.data, cv2.COLOR_GRAY2BGR)

        for r, pt1, pt2 in zip(lines, pts1, pts2):
            color = tuple(np.random.randint(0,255,3).tolist())
            x0, y0 = map(int, [0, -r[2]/r[1]])
            x1, y1 = map(int, [c, -(r[2]+r[0]*c)/r[1]])
            img1 = cv2.line(img1, (x0, y0), (x1, y1), color, 10)
            img1 = cv2.circle(img1, tuple(pt1), 5, color, -1)
            img2 = cv2.circle(img2, tuple(pt2), 5, color, -1)
            return img1, img2

    def compute_correspond_epilines(self, img1, img2, points_left, points_right, F):
        pts1 = np.int32(points_left)
        pts2 = np.int32(points_right)

        # Find epilines corresponding to points in right image (second image) and
        # drawing its lines on left image
        linestor = cv2.computeCorrespondEpilines(pts2.reshape(-1, 1, 2), 2, F)
        linestor = linestor.reshape(-1, 3)
        limgtor, rimgtor = self.draw_lines(img1, img2, linestor, pts1, pts2)

        # Find epilines corresponding to points in left image (first image) and
        # drawing its lines on right image
        linestol = cv2.computeCorrespondEpilines(pts1.reshape(-1, 1, 2), 1, F)
        linestol = linestol.reshape(-1, 3)
        limgtol, rimgtol = self.draw_lines(img2, img1, linestol, pts2, pts1)

        limgtor = cv2.resize(limgtor, (int(640), int(480)), interpolation=cv2.INTER_CUBIC)
        limgtol = cv2.resize(limgtol, (int(640), int(480)), interpolation=cv2.INTER_CUBIC)

        numpy_horizontal_concat = np.concatenate((limgtor, limgtol), axis=1)
        image = Image(numpy_horizontal_concat)
        image.display("epipol lines")
