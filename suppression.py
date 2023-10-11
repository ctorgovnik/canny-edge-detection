import numpy as np

class NonMaximumSupression:

    @staticmethod
    def suppress(direction, magnitude):
        
        M,N = magnitude.shape
        suppressed_im = np.zeros((M, N))
        neighbor1 = 0
        neighbor2 = 0
        for y in range(1, M-1):
            for x in range(1, N-1):
                dir = NonMaximumSupression.get_current_dir(direction[y, x])

                if (dir == "horizontal"):
                    neighbor1 = magnitude[y, x+1]
                    neighbor2 = magnitude[y, x-1]

                elif (dir == "vertical"):
                    neighbor1 = magnitude[y+1, x]
                    neighbor2 = magnitude[y-1, x]
                
                elif (dir == "positive_diagonal"):
                    neighbor1 = magnitude[y-1, x+1]
                    neighbor2 = magnitude[y+1, x-1]

                elif (dir == "negative_diagonal"):
                    neighbor1 = magnitude[y-1, x-1]
                    neighbor2 = magnitude[y+1, x+1]


                if (magnitude[y,x] >= neighbor1 and magnitude[y,x] >= neighbor2):

                    suppressed_im[y,x] = magnitude[y, x]
  
                else:
                    suppressed_im[y,x] = 0
       
        
        return suppressed_im



    @staticmethod
    def get_current_dir(dir):
        
        angle = (dir * 180 / np.pi) % 360

        if (angle >= 0 and angle < 22.5) or (angle >= 157.5 and angle < 202.5) or (angle >= 337.5 and angle <= 360):
            return "horizontal"
        elif (angle >= 22.5 and angle < 67.5) or (angle >= 202.5 and angle < 247.5):
            return "positive_diagonal"
        elif (angle >= 67.5 and angle < 112.5) or (angle >= 247.5 and angle < 292.5):
            return "vertical"
        elif (angle >= 112.5 and angle < 157.5) or (angle >= 292.5 and angle < 337.5):
            return "negative_diagonal"
        
        return angle