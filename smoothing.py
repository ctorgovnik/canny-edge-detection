import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np


class Smoothing:
    kernel_3 = np.array([[1.0, 2.0, 1.0], [2.0, 4.0, 2.0], [1.0, 2.0, 1.0]]) / 16

    def gaussian_blur(im, kernel):
        step = kernel.shape[0]

        # adding padding around the border
        padded_im = np.pad(im, (int(step / 2), int(step / 2)))

        blur_im = []
        for i in range(im.shape[0]):  # for row
            for j in range(im.shape[1]):  # for pixel in row
                current_blur = np.sum(padded_im[i : step + i, j : step + j] * kernel)
                blur_im.append(current_blur)

        blur_im = np.array(blur_im).reshape((im.shape[0], im.shape[1]))
        return blur_im
