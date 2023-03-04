from filters_opencv.filters.local_filters.border_selection.utils.constants import SOBEL_KERNEL_X, SOBEL_KERNEL_Y
from filters_opencv.filters.local_filters.border_selection.utils.kernel_application import apply_split_kernels

from filters_opencv.image import Image


def sobel(image: Image):
    apply_split_kernels(image, [SOBEL_KERNEL_X, SOBEL_KERNEL_Y])

