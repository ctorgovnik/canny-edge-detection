from image_io import ImageIO
from smoothing import Smoothing
from gradient import SobelOperator
from suppression import NonMaximumSupression
from thresholding import DoubleThreshold

import cv2


def main():
    color_im = ImageIO.read_image("taylor_swift.webp")
    gray_im = ImageIO.convert_grayscale(color_im)
    blur_im = Smoothing.gaussian_blur(gray_im, Smoothing.kernel_3)

    sobel_operator = SobelOperator()
    magnitude = sobel_operator.gradient_magnitude(blur_im)
    dir = sobel_operator.gradient_direction()

    suppressed_im = NonMaximumSupression.suppress(dir, magnitude)

    thresh_im = DoubleThreshold.apply_threshold(suppressed_im, 0.05, 0.2)

    ImageIO.display_image(color_im, None)
    ImageIO.display_image(gray_im, "gray")
    ImageIO.display_image(blur_im, "gray")
    ImageIO.display_image(suppressed_im, "gray")
    ImageIO.display_image(thresh_im, "gray")


if __name__ == "__main__":
    main()
