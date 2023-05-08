import numpy as np

from RHMIcv import utils
from RHMIcv.image import Image
from RHMIcv.filter.bilateral_filter import BilateralFilter
from RHMIcv.filter.gauss_filter import GaussFilter
from RHMIcv.filter.histogram_equalization import HistogramEqualization
from RHMIcv.filter.mean_filter import MeanFilter
from RHMIcv.filter.median_filter import MedianFilter

HISTOGRAM = False
HISTOGRAM_EQUALIZATION = False
MEAN_FILTER = True
MEDIAN_FILTER = False

def main():
    # First we will load the images, here some different examples
    img_1 = Image("data/IMG_6960.JPG", 0)
    img_2 = Image("data/Panda_Arm.jpg", 0)
    img_3 = Image("data/mika.png", 0)

    # then we add noise to evaluate the filters and display the result
    img_1.add_noise("gauss")  # or "poison", "s&p"
    img_2.add_noise("poison")  # or "gauss", "s&p"
    img_3.add_noise("s&p")  # or "gauss", "poison"
    img_1.display("original_image")

    if HISTOGRAM is True:
        # first exercise: generate histogram from image (complete function in the file image.py)
        print("Berechnung und Anzeige des Histogramms")
        img_1.display_histogram()

    if HISTOGRAM_EQUALIZATION is True:
        # second exercise: write the histogram equalization (complete function in the file histogram_equalization.py)
        print("Berechnung und Anzeige des Histogrammausgleichs")
        histogram_equalization = HistogramEqualization()
        equal_img = histogram_equalization.filter(img_1)
        equal_img.display_histogram()

    if MEAN_FILTER is True:
        # third exercise: write the mean or box filter (complete function in the file mean_filter.py)
        print("Berechnung und Anzeige des Mittelwertfilters")
        kernel_size = 3
        mean_filter = MeanFilter(kernel_size)
        mean_img = mean_filter.filter(img_1)
        mean_img.display("mean filter")

        # In addition to compare Gauss and Bilateral filter, functions are already implemented.
        print("Berechnung und Anzeige des Gauss- und Bilateralfilters")
        gauss_filter = GaussFilter(kernel_size)
        bilateral_filter = BilateralFilter(kernel_size)
        gauss_img = gauss_filter.filter(img_1)
        bil_img = bilateral_filter.filter(img_1)
        utils.display_images(gauss_img.data, bil_img.data, "gaussian / bilateral filter")

    if MEDIAN_FILTER is True:
        # fourth exercise: write the median filter (complete function in the file median_filter.py)
        print("Berechnung und Anzeige des Medianfilters")
        kernel_size = 3
        median_filter = MedianFilter(kernel_size)
        median_img = median_filter.filter(img_1)
        median_img.display("median filter")

    if HISTOGRAM and HISTOGRAM_EQUALIZATION and MEAN_FILTER and MEDIAN_FILTER:
        # Display all filtered images together to compare and discuss them.
        print("Vergleich der verschiedenen Filter")
        rows, cols = img_1.data.shape
        scale = 0.8
        img_1.resize(cols * scale, rows * scale)
        mean_img.resize(cols * scale, rows * scale)
        median_img.resize(cols * scale, rows * scale)
        gauss_img.resize(cols * scale, rows * scale)
        bil_img.resize(cols * scale, rows * scale)
        numpy_horizontal_concat = np.concatenate((img_1.data, mean_img.data, median_img.data, gauss_img.data,
                                                  bil_img.data), axis=1)
        strung_filters = Image(numpy_horizontal_concat)
        strung_filters.display("images with the filters: raw, mean, median, gauss, bilateral")

if __name__ == '__main__':
    main()
