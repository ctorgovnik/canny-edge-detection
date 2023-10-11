import numpy as np

class SobelOperator:

    def __init__(self):
        Kx = np.array([[1.0, 0.0, -1.0], [2.0, 0.0, -2.0], [1.0, 0.0, -1.0]])
        Ky = Kx.T
        Ix = []
        Iy = []

    def gradient_magnitude(self, im):
        self.Ix = self.convolve_2d(im, self.Kx)
        self.Iy = self.convolve_2d(im, self.Ky)
        magnitude = np.sqrt(np.square(self.Ix) + np.square(self.Iy))
        return magnitude

    def gradient_direction(self):
        theta = np.arctan2(self.Ix, self.Iy)
        return theta


    def convolve_2d(im, k):
        Im, In = im.shape
        Km, Kn = im.shape

        # add padding
        pad = (Kn - 1) // 2
        padded_img = np.pad(im, ((pad, pad), (pad, pad)), mode = 'constant')

        output = np.zeros((Im, In))

        for y in range (Km):
            for x in range (Kn):
                # extract sub array the size of kernel
                region = padded_img[y:y+Km, x:x+Kn]

                output[y, x] = np.sum(region * k)

            return output
        
