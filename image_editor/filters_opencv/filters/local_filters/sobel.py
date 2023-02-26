from filters_opencv.filters.local_filters.utils.constants import SOBEL_KERNEL_X, SOBEL_KERNEL_Y
from filters_opencv.filters.local_filters.utils.methods.image_changes import apply_kernel
from filters_opencv.image import Image


def sobel(image: Image):
    apply_kernel(image, [SOBEL_KERNEL_X, SOBEL_KERNEL_Y])
