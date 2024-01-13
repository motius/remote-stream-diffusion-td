from random import randint

import cv2 as cv
import numpy as np

from touchdesigner_plugin.constants import IMG_HEIGHT, IMG_WIDTH, RGB_CHANNELS


def get_random_rgb():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return r, g, b


def get_random_image(nb_circles: int = 0, noise_background: bool = False):

    if noise_background:
        image = (
            np.random.standard_normal([IMG_HEIGHT, IMG_WIDTH, RGB_CHANNELS]) * 255
        ).astype(np.uint8)
    else:
        red = np.full((IMG_HEIGHT, IMG_WIDTH), randint(0, 255))
        green = np.full((IMG_HEIGHT, IMG_WIDTH), randint(0, 255))
        blue = np.full((IMG_HEIGHT, IMG_WIDTH), randint(0, 255))
        image = cv.merge((red, green, blue))

    for i in range(nb_circles):
        position = randint(0, IMG_HEIGHT - 1), randint(0, IMG_WIDTH - 1)
        r, g, b = get_random_rgb()
        size = randint(400, 1000)
        cv.circle(image, (position[0], position[1]), size, (r, g, b), -1)
    return image
