import os
from scipy import ndimage
import random
import cv2
import skimage
import matplotlib.pyplot as plt
import re
from skimage import io

import numpy as np
################cv2 method for salt and pepper ###########################

def add_noise(img):

    # Getting the dimensions of the image
    # image shape : 768 x 474
    row, col = img.shape
    # Randomly pick some pixels in the
    # image for coloring them white
    # Pick a random number between 300 and 10000
    # (total count of pixels in a frame is 364,032
    number_of_pixels = random.randint(300, 10000)
    for i in range(number_of_pixels):
        # Pick a random y coordinate
        y_coord = random.randint(0, row - 1)

        # Pick a random x coordinate
        x_coord = random.randint(0, col - 1)

        # Color that pixel to white
        img[y_coord][x_coord] = 255

    # Randomly pick some pixels in
    # the image for coloring them black

    number_of_pixels = random.randint(300, 10000)
    for i in range(number_of_pixels):
        # Pick a random y coordinate
        y_coord = random.randint(0, row - 1)

        # Pick a random x coordinate
        x_coord = random.randint(0, col - 1)

        # Color that pixel to black
        img[y_coord][x_coord] = 0

    return img

####################################################
# main_path = os.getcwd()
# filename = 'frames'
# path = os.path.join(main_path, filename)
# #####################sorting the frame numbers ##########################
# images = [img for img in os.listdir(path)]
def natural_sort_key(s, _nsre=re.compile('([0-9]+)')):
    return [
        int(text)
        if text.isdigit() else text.lower()
        for text in _nsre.split(s)]

# sorted_images = sorted(images, key=natural_sort_key)
#
#
#
# ##############################################
# i=0
# #for image_path in os.listdir(path):
# for image_path in sorted_images:
#     # create the full input path and read the file
#     input_path = os.path.join(path, image_path)
#     #image_to_add_noise = ndimage.imread(input_path)
#     raw_image = cv2.imread(input_path, cv2.IMREAD_GRAYSCALE)
#     noisy_folder='s&p_noisy'
#     noisy_path = os.path.join(main_path, noisy_folder)
# #    cv2.imwrite(noisy_path + '/' + "frame%d.jpg" % i,  add_noise(raw_image))
#     #print(input_path)
#     #print(i)
#     cv2.imwrite(noisy_path + '/' + "%d.jpg" % i,  add_noise(raw_image))
#     #print("saved",i)
#     i+=1
##########################testing#######################################
# test_img = path+'\\'+'frame0.jpg'
# # print(test_img)
# raw_image = cv2.imread(test_img, cv2.IMREAD_GRAYSCALE)
# #cv2.imshow('Image', raw_image)
# #cv2.waitKey(0)
# shape=raw_image.shape
# # total number of image pixels : 364,032
#
# #print(shape)
# noisy=add_noise(raw_image)
# #print(noisy.shape)
# #cv2.imshow('Image', noisy)
# #cv2.waitKey(0)
######################skimage method for different types of noise #############################


def selectnoise(path, mode, out_folder):
    images = [img for img in os.listdir(path)]
    sorted_images = sorted(images, key=natural_sort_key)
    noisy_path = os.path.join(main_path, out_folder)
    if not os.path.isdir(noisy_path):
        os.mkdir(noisy_path)

    if mode is not None:
        i = 0
        for image_path in sorted_images:
            input_path = os.path.join(path, image_path)
            # print(path)
            # break
            img = skimage.io.imread(input_path) / 255.0
            nimg = skimage.util.random_noise(img, mode=mode)
            noise_img = np.array(255 * nimg, dtype='uint8')
            # print(noise_img)
            cv2.imwrite(noisy_path + '/' + "%d.jpg" % i, noise_img)
            i+=1


#############################################################

main_path = os.getcwd()
# print(main_path)
img_folder='frames'

path = os.path.join(main_path, img_folder)
# print(path)

# selectnoise(path, "gaussian","gaussian")
# selectnoise(path, "localvar","localvar")
# selectnoise(path, "poisson","poisson")
# selectnoise(path, "salt","salt")
# selectnoise(path, "pepper","pepper")
# selectnoise(path, "s&p","s&p")
# selectnoise(path, "speckle","speckle")
# selectnoise(path, None)
