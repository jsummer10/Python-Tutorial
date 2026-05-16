
import cv2
import matplotlib.pyplot as plt
import os
import sys
from pathlib import Path

script_dir = Path(__file__).parent
os.chdir(script_dir)


def display_pixel_info(img: cv2.typing.MatLike, pix_x: int, pix_y: int):
    """ Display the pixel information for the specified pixel

    :param img: RGB image to use
    :type img: cv2.typing.MatLike
    :param pix_x: pixel on x-axis
    :type pix_x: int
    :param pix_y: pixel on y-axis
    :type pix_y: int
    """

    print(f'Sample Pixel: x={pix_x}, y={pix_y}')

    print(f'\nRGB Pixel: {img[pix_y, pix_x]}')
    print(f'  Shape : {img.shape}')
    print(f'  Red   : {img[pix_y, pix_x, 0]}')
    print(f'  Green : {img[pix_y, pix_x, 1]}')
    print(f'  Blue  : {img[pix_y, pix_x, 2]}')

    new_img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    print(f'\nBRG Pixel: {new_img[pix_y, pix_x]}')
    print(f'  Shape : {new_img.shape}')
    print(f'  Red   : {new_img[pix_y, pix_x, 2]}')
    print(f'  Green : {new_img[pix_y, pix_x, 1]}')
    print(f'  Blue  : {new_img[pix_y, pix_x, 0]}')

    new_img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    print(f'\nGrayscale Pixel: {new_img[pix_y, pix_x]}')
    print(f'  Shape : {new_img.shape}')

    new_img = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
    print(f'\nHSV Pixel: {new_img[pix_y, pix_x]}')
    print(f'  Shape      : {new_img.shape}')
    print(f'  Hue        : {new_img[pix_y, pix_x, 0]}')
    print(f'  Saturation : {new_img[pix_y, pix_x, 1]}')
    print(f'  Value      : {new_img[pix_y, pix_x, 2]}')

    new_img = cv2.cvtColor(img, cv2.COLOR_RGB2LAB)
    print(f'\nLAB Pixel: {new_img[pix_y, pix_x]}')
    print(f'  Shape     : {new_img.shape}')
    print(f'  Luminance : {new_img[pix_y, pix_x, 0]}')
    print(f'  A Value   : {new_img[pix_y, pix_x, 1]}')
    print(f'  B Value   : {new_img[pix_y, pix_x, 2]}')

    new_img = cv2.cvtColor(img, cv2.COLOR_RGB2YCrCb)
    print(f'\nYCrCb Pixel: {new_img[pix_y, pix_x]}')
    print(f'  Shape       : {new_img.shape}')
    print(f'  Intensity   : {new_img[pix_y, pix_x, 0]}')
    print(f'  Red Chroma  : {new_img[pix_y, pix_x, 1]}')
    print(f'  Blue Chroma : {new_img[pix_y, pix_x, 2]}')


def main():
    """ Main function for the image processing ntoes """

    img_file = script_dir/'sample.jpg'
    if not img_file.exists():
        print(f'Unable to find image: {img_file}')
        sys.exit(1)

    #--------------
    #  Load Image
    #--------------

    # read in image as BRG
    img = cv2.imread(img_file)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    print(f'\nImage Size: {img.shape[1]}x{img.shape[0]} '
          f'({img.size:,} pixels)')

    print('\n' + '-'*80 + '\n')
    display_pixel_info(img, 100, 100)
    print('\n' + '-'*80 + '\n')

    # split into RGB channels and merge back together
    r, g, b = cv2.split(img)
    img = cv2.merge((r, g, b))

    #------------------
    #  Display Images
    #------------------

    fig = plt.figure(figsize=(15, 9))
    gs = fig.add_gridspec(nrows=1, ncols=2)

    cell = fig.add_subplot(gs[0, 0])
    cell.imshow(img)
    cell.set_title('RGB')
    cell.axis('off')

    gray_img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    cell = fig.add_subplot(gs[0, 1])
    cell.imshow(gray_img, cmap='gray')
    cell.set_title('Grayscale')
    cell.axis('off')

    plt.show()


if __name__ == '__main__':
    main()