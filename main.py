from image_io import ImageIO


def main():
    color_im = ImageIO.read_image("goat.jpeg")
    gray_im = ImageIO.convert_grayscale(color_im)

    ImageIO.display_image(color_im, None)
    ImageIO.display_image(gray_im, "gray")


if __name__ == "__main__":
    pass

main()
