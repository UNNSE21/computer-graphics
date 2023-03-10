from filters_opencv.filters.local_filters.increase_sharpness import increase_sharpness_1, increase_sharpness_2
from filters_opencv.filters.local_filters.border_selection import sobel, pruitt, sharra
from filters_opencv.filters.local_filters.median import median
from filters_opencv.filters.local_filters.glowing_edges import glowing_edges
from filters_opencv.filters.local_filters.embossing import emboss
from filters_opencv.filters.local_filters.maximum import maximum
from filters_opencv.filters.local_filters.blur import (
    blur,
    blur_by_andrey,
    not_optimized_blur,
    blur_gaussian,
    motion_blur,
)
from filters_opencv.filters.local_filters.mathematical_morphology import (
    erosion,
    dilation,
    opening,
    closing,
    top_hat,
    black_hat,
    grad,
)
