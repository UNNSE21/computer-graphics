from typing import Final

SOBEL_KERNEL_X: Final = [[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]
SOBEL_KERNEL_Y: Final = [[-1, -2, -1], [0, 0, 0], [1, 2, 1]]
INCREASE_SHARPNESS_KERNEL_1: Final = [[0, -1, 0], [-1, 5, -1], [0, -1, 0]]
INCREASE_SHARPNESS_KERNEL_2: Final = [[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]]
SHARRA_KERNEL_X: Final = [[3, 10, 3], [0, 0, 0], [-3, -10, -3]]
SHARRA_KERNEL_Y: Final = [[3, 0, -3], [10, 0, -10], [3, 0, -3]]
PRUITT_KERNEL_X: Final = [[1, 1, 1], [0, 0, 0], [-1, -1, -1]]
PRUITT_KERNEL_Y: Final = [[1, 0, -1], [1, 0, -1], [1, 0, -1]]
