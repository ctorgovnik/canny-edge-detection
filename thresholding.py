import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np


class DoubleThreshold:
    def apply_threshold(im, low_ratio, high_ratio):
        high_thresh = im.max() * high_ratio
        low_thresh = high_thresh * low_ratio

        x, y = im.shape
        thresh_im = np.zeros((x, y))

        strong_x, strong_y = np.where(im >= high_thresh)
        weak_x, weak_y = np.where((im <= high_thresh) & (im >= low_thresh))

        thresh_im[strong_x, strong_y] = 255
        thresh_im[weak_x, weak_y] = 75

        return thresh_im
