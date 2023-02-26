from filters_opencv.filters.local_filters.utils.constants import PRUITT_KERNEL_X, PRUITT_KERNEL_Y
from filters_opencv.filters.local_filters.utils.methods.image_changes import apply_kernel
from filters_opencv.image import Image


def pruitt(image: Image):
    apply_kernel(image, [PRUITT_KERNEL_X, PRUITT_KERNEL_Y])
