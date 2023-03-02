from filters_opencv.filters.local_filters.utils.constants import (
    INCREASE_SHARPNESS_KERNEL_1,
    INCREASE_SHARPNESS_KERNEL_2,
)
from filters_opencv.filters.local_filters.utils.methods.image_changes import apply_kernels

from filters_opencv.image import Image


def increase_sharpness_1(image: Image):
    apply_kernels(image, [INCREASE_SHARPNESS_KERNEL_1])


def increase_sharpness_2(image: Image):
    apply_kernels(image, [INCREASE_SHARPNESS_KERNEL_2])

