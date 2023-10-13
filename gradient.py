import numpy as np


class SobelOperator:
    def __init__(self):
        self.Kx = np.array([[1.0, 0.0, -1.0], [2.0, 0.0, -2.0], [1.0, 0.0, -1.0]])
        self.Ky = self.Kx.T
        self.Ix = []
        self.Iy = []

    def gradient_magnitude(self, im):
        self.Ix = self.convolve_2d(im, self.Kx)
        self.Iy = self.convolve_2d(im, self.Ky)
        magnitude = np.sqrt(np.square(self.Ix) + np.square(self.Iy))
        magnitude = magnitude / magnitude.max() * 255
        return magnitude

    def gradient_direction(self):
        theta = np.arctan2(self.Iy, self.Ix)
        return theta

    def convolve_2d(self, im, k):
        Im, In = im.shape
        Km, Kn = k.shape

        # add padding
        pad = (Kn - 1) // 2
        padded_img = np.pad(im, ((pad, pad), (pad, pad)), mode="constant")

        output = np.zeros((Im, In))

        for y in range(Im):
            for x in range(In):
                # extract sub array the size of kernel
                region = padded_img[y : y + Km, x : x + Kn]

                output[y, x] = np.sum(region * k)

        return output
