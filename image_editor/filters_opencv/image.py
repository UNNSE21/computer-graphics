import numpy
import cv2


class Image:

    def __init__(self, path: str):
        self.path = path
        self.image = cv2.imread(path)

        if not isinstance(self.image, numpy.ndarray):
            raise Exception('Сant open image: check file path.')
        self.height = self.image.shape[0]
        self.width = self.image.shape[1]
        self.size = self.height * self.width

    def __getitem__(self, vals):
        return tuple(reversed(self.image[vals]))

    def __setitem__(self, vals, rgb_color):
        rgb_color = [min(max(x, 0), 255) for x in rgb_color]
        self.image[vals] = tuple(reversed(rgb_color))

    def get_bitmap(self):
        bitmap = []
        for i in range(self.height):
            line = []
            for j in range(self.width):
                line.append(tuple(reversed(self.image[i, j])))
            bitmap.append(line)
        return bitmap

    def load_bitmap(self, bitmap):
        self.image = numpy.full((len(bitmap), len(bitmap[0]), 3), 0, dtype=numpy.uint8)
        for i, row in enumerate(bitmap):
            for j, elem in enumerate(row):
                rgb_color = [int(min(max(x, 0), 255)) for x in tuple(reversed(elem))]
                self.image[i, j] = rgb_color

        self.height = self.image.shape[0]
        self.width = self.image.shape[1]

    def show(self):
        cv2.imshow("Image", self.image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def save(self, path: str):
        is_written = cv2.imwrite(path, self.image)
        if not is_written:
            raise Exception('Failed to save image')
