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

    def load_bitmap(self, bgr_bitmap):
        self.image = numpy.array(bgr_bitmap)
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
