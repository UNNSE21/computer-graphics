from filters_opencv.filters.local_filters.border_selection.sobel import sobel
from filters_opencv.filters.local_filters.maximum import maximum
from filters_opencv.filters.local_filters.median import median
from filters_opencv.image import Image


def glowing_edges(image: Image, radius_filter: int):
    median(image, radius_filter)
    sobel(image)
    maximum(image, radius_filter)
