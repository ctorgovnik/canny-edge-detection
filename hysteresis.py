import numpy as np


class Hysteresis:
    def apply_hysteresis(im):
        weak = 75
        strong = 255

        M, N = im.shape

        new_im = np.copy(im)

        for y in range(1, M - 1):
            for x in range(1, N - 1):
                if im[y, x] == weak:
                    if np.any(new_im[y - 1 : y + 2, x - 1 : x + 2] == strong):
                        new_im[y, x] = strong
                    else:
                        new_im[y, x] = 0
        return new_im
