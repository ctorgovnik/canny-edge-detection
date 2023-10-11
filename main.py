from image_io import ImageIO
import smoothing
from gradient import SobelOperator
from suppression import NonMaximumSupression


def main():
    color_im = ImageIO.read_image("goat.jpeg")
    gray_im = ImageIO.convert_grayscale(color_im)
    blur_im = smoothing.gaussian_blur(gray_im, smoothing.kernel_3)
    
    sobel_operator = SobelOperator()
    magnitude = sobel_operator.gradient_magnitude(blur_im)
    dir = sobel_operator.gradient_direction()

    suppressed_im = NonMaximumSupression.suppress(dir, magnitude)

    ImageIO.display_image(color_im, None)
    ImageIO.display_image(gray_im, "gray")
    ImageIO.display_image(blur_im, "gray")
    ImageIO.display_image(suppressed_im, "gray")


if __name__ == "__main__":
    main()
