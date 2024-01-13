from random import randint

import cv2 as cv
import numpy as np

from touchdesigner_plugin.constants import IMG_HEIGHT, IMG_WIDTH, RGB_CHANNELS


def get_random_image(nb_circles: int = 3):
    image = (
        np.random.standard_normal([IMG_HEIGHT, IMG_WIDTH, RGB_CHANNELS]) * 255
    ).astype(np.uint8)
    for i in range(nb_circles):
        position = randint(0, IMG_HEIGHT - 1), randint(0, IMG_WIDTH - 1)
        red = randint(0, 255)
        green = randint(0, 255)
        blue = randint(0, 255)
        size = randint(400, 1000)
        cv.circle(image, (position[0], position[1]), size, (red, green, blue), -1)
    return image
