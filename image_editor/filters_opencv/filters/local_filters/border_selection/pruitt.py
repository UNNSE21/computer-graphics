from filters_opencv.filters.local_filters.border_selection.utils.constants import PRUITT_KERNEL_X, PRUITT_KERNEL_Y
from filters_opencv.filters.local_filters.border_selection.utils.kernel_application import apply_split_kernels
from filters_opencv.image import Image


def pruitt(image: Image):
    apply_split_kernels(image, [PRUITT_KERNEL_X, PRUITT_KERNEL_Y])
