from image_io import ImageIO
from smoothing import Smoothing
from gradient import SobelOperator
from suppression import NonMaximumSupression
from thresholding import DoubleThreshold
from hysteresis import Hysteresis

import numpy as np


def main():
    file_name = input("Enter the image file name (with extension)\n")

    try:
        color_im = ImageIO.read_image(file_name)
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found in the current directory.")
        return
    
    gray_im = ImageIO.convert_grayscale(color_im)
    blur_im = Smoothing.gaussian_blur(gray_im, Smoothing.kernel_3)

    sobel_operator = SobelOperator()
    magnitude = sobel_operator.gradient_magnitude(blur_im)
    dir = sobel_operator.gradient_direction()

    suppressed_im = NonMaximumSupression.suppress(dir, magnitude)

    thresh_im = DoubleThreshold.apply_threshold(suppressed_im, 0.1, 0.25)

    final_im = Hysteresis.apply_hysteresis(thresh_im)

    ImageIO.display_image(color_im, None, "Original Image")
    # ImageIO.display_image(gray_im, "gray", "Gray Scale Image")
    # ImageIO.display_image(blur_im, "gray", "Blurred Image")
    # ImageIO.display_image(suppressed_im, "gray", "Supressed Image")
    # ImageIO.display_image(thresh_im, "gray", "Thresholded Image")
    ImageIO.display_image(final_im, "gray", "Final Image")


if __name__ == "__main__":
    main()
