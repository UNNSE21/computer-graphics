from filters_opencv.filters.local_filters.border_selection.utils.constants import SHARRA_KERNEL_X, SHARRA_KERNEL_Y
from filters_opencv.filters.local_filters.utils.kernel_application import apply_kernels
from filters_opencv.image import Image


def sharra(image: Image):
    apply_kernels(image, [SHARRA_KERNEL_X, SHARRA_KERNEL_Y])
