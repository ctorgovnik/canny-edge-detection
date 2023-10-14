
import numpy as np

class Hysteresis:

    def apply_hysteresis(im):
        weak = 75
        strong = 255

        M,N = im.shape

        for y in range(1, M-1):
            for x in range(1, N-1):
                if(im[y,x] == weak):
                    ## create 3x3 matrix around weak pixel
                    if np.any(im[y-1:y+2, x-1:x+2] == strong):
                        im[y, x] = strong
                else:
                    im[y, x] = 0
        
        return im

        