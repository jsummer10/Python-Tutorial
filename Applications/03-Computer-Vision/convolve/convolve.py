"""
.. module:: convolve
    :platform: Unix, Windows
    :synopsis: Entry point for project 2 functionality

.. moduleauthor:: Jacob Summerville <jacob39@illinois.edu>
"""

import cv2
import matplotlib.pyplot as plt
import numpy as np


def high_pass_filters(image_rgb) -> np.array:
    fig = plt.figure(figsize=(15, 9))
    gs = fig.add_gridspec(nrows=2, ncols=3)

    cell = fig.add_subplot(gs[0, 0])
    cell.imshow(image_rgb)
    cell.set_title('Original')
    cell.axis('off')

    convolved = cv2.filter2D(image_rgb, -1,
                             np.array([[-1, -1, -1],
                                       [-1,  8, -1],
                                       [-1, -1, -1]]))
    cell = fig.add_subplot(gs[0, 1])
    cell.imshow(convolved)
    cell.axis('off')

    convolved = cv2.filter2D(image_rgb, -1,
                             np.array([[0, 0,  0],
                                       [1, 0, -1],
                                       [0, 0,  0]]))
    cell = fig.add_subplot(gs[0, 2])
    cell.imshow(convolved)
    cell.axis('off')

    convolved = cv2.filter2D(image_rgb, -1,
                             np.array([[ 0, 0, 0],
                                       [-1, 0, 1],
                                       [ 0, 0, 0]]))
    cell = fig.add_subplot(gs[1, 0])
    cell.imshow(convolved)
    cell.axis('off')

    plt.show()


def shift_right_filters(image_rgb) -> np.array:
    fig = plt.figure(figsize=(16, 9))
    gs = fig.add_gridspec(nrows=1, ncols=4)

    cell = fig.add_subplot(gs[0, 0])
    cell.imshow(image_rgb)
    cell.set_title('Original')
    cell.axis('off')

    convolved = image_rgb.copy()
    for _ in range(10):
        convolved = cv2.filter2D(convolved, -1,
                             np.array([[0, 0, 0],
                                       [1, 0, 0],
                                       [0, 0, 0]]))
    cell = fig.add_subplot(gs[0, 1])
    cell.imshow(convolved)
    cell.axis('off')

    plt.show()


def main():
    # read image as RGB
    image = cv2.imread('city.jpg')
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    high_pass_filters(image_rgb)


if __name__ == '__main__':
    main()
