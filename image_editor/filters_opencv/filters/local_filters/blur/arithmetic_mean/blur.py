from filters_opencv.image import Image
from numpy import array
from copy import copy


def blur(image: Image, radius_h, radius_w):
    old_rgb = _pixel(image, 0, 0, radius_h, radius_w)
    static_image = copy(image)

    for i in range(image.height):
        if i % 2 == 0:
            for j in range(image.width):
                image[i, j] = _update_pixel(static_image, i, j, radius_h, radius_w, old_rgb)
        else:
            for j in range(image.width - 1, -1, -1):
                image[i, j] = _update_pixel(static_image, i, j, radius_h, radius_w, old_rgb)


def _update_pixel(image: Image, h, w, radius_h, radius_w, old_rgb):
    hs = max(h - radius_h, 0)
    hf = min(h + radius_h + 1, image.height)
    ws = max(w - radius_w, 0)
    wf = min(w + radius_w + 1, image.width)
    if old_rgb[1] != h:
        old_rgb[0] += _delta_hight(image, h, old_rgb[1], ws, wf, radius_h, radius_w)
    elif old_rgb[2] != w:
        old_rgb[0] += _delta_width(image, w, old_rgb[2], hs, hf, radius_h, radius_w)

    old_rgb[1] = h
    old_rgb[2] = w
    return old_rgb[0] // ((hf - hs) * (wf - ws))


def _pixel(image: Image, h, w, radius_h, radius_w):
    rgb = array([0, 0, 0])

    for i in range(max(h - radius_h, 0), min(h + radius_h + 1, image.height)):
        for j in range(max(w - radius_w, 0), min(w + radius_w + 1, image.width)):
            rgb += image[i, j]

    return [rgb, h, w]


def _delta_hight(image: Image, h, old_h, ws, wf, radius_h, radius_w):
    rgb = array([0, 0, 0])

    if h + radius_h < image.height:
        for i in range(ws, wf):
            rgb += image[h + radius_h, i]

    if old_h - radius_h >= 0:
        for i in range(ws, wf):
            rgb -= image[old_h - radius_h, i]

    return rgb


def _delta_width(image: Image, w, old_w, hs, hf, radius_h, radius_w):
    rgb = array([0, 0, 0])

    if w - old_w > 0:  # go right
        if w + radius_w < image.width:
            for i in range(hs, hf):
                rgb += image[i, w + radius_w]
        if old_w - radius_w >= 0:
            for i in range(hs, hf):
                rgb -= image[i, old_w - radius_w]
    else:  # go left
        if w - radius_w >= 0:
            for i in range(hs, hf):
                rgb += image[i, w - radius_w]
        if old_w + radius_w < image.width:
            for i in range(hs, hf):
                rgb -= image[i, old_w + radius_w]

    return rgb
