from math import exp


def calculate_kernel_gaussian_blur(size: int, denominator: float):
    kernel = [0.0] * (size + 1)
    for i in range(1, size + 1):
        kernel[i] = exp(-1 * i * i / denominator)
        kernel[-i] = kernel[i]
    return kernel


def calculate_kernel_motion_blur(size: int):
    if size % 2 == 0:
        size += 1
    return [1/size] * size
