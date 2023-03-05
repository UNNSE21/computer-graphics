from filters_opencv.image import Image


def linear_stretch(image: Image):
    min_brightness_pixel, max_brightness_pixel = _search_min_max_pixels_brightness(image)
    for i in range(image.height):
        for j in range(image.width):
            pixel_difference = _subtract_pixels(image[i, j], min_brightness_pixel)
            max_min_difference = _subtract_pixels(max_brightness_pixel, min_brightness_pixel)
            image[i, j] = [x / y * 255 for x, y in zip(pixel_difference, max_min_difference)]


def _subtract_pixels(reduced, deductible):
    return [x - y for x, y in zip(reduced, deductible)]


def _search_min_max_pixels_brightness(image: Image):
    min_brightness_pixel = image[0, 0]
    max_brightness_pixel = image[0, 0]

    for i in range(image.height):
        for j in range(image.width):
            min_brightness_pixel = min(min_brightness_pixel, image[i, j], key=lambda x: sum(x))
            max_brightness_pixel = max(max_brightness_pixel, image[i, j], key=lambda x: sum(x))
    return min_brightness_pixel, max_brightness_pixel
