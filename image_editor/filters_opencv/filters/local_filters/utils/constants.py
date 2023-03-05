from typing import Final

INCREASE_SHARPNESS_KERNEL_1: Final = [[0, -1, 0], [-1, 5, -1], [0, -1, 0]]
INCREASE_SHARPNESS_KERNEL_2: Final = [[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]]
EMBOSSING_KERNEL: Final = [[0, 1, 0], [1, 0, -1], [0, -1, 0]]
