import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np


class ImageIO:
    def read_image(path):
        # Read the image
        image = plt.imread(path)
        return image

    def convert_grayscale(im):
        return np.dot(im[..., :3], [0.299, 0.587, 0.114])

    def display_image(image, color, title):
        # Display the image
        plt.imshow(image, cmap=color)
        plt.title(title)
        plt.show()
