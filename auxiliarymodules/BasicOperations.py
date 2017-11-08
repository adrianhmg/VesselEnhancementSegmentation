# -*- coding: utf-8 -*-

"""
Date                :  15/08/2017
Author              :  Adrián Homero Moreno García
Objective of Script :  This script has functions of the basic operations that can be do in the image
"""

import numpy as np

class BasicOperations:

    def invert_image(self, data):
        """
        Function for invert image, scanning values of the original 
        image and substract 255 and stored on global img_inverted = []
        :param data: It contians in a list of list the values of the image to invert.
        :return: The data of the image inverted
        """

        img_inverted = []

        LENGTH = len(data)

        # process where it makes the invert operation
        for row in data:
            for value in row:
                img_inverted.append(1.0 - (value / 255))

        # convert that to 2D list (list of lists of integers)
        img_inverted = [img_inverted[offset:offset + LENGTH]
                        for offset in range(0, LENGTH * LENGTH, LENGTH)]

        return img_inverted

    def substract_imges(self, data_image, data_substract):
        """
        Function that subsract 2 images, like difference = data_image - data_substract
        :param data_image: Image to substract
        :param data_substract: Image for substract
        :return: Return difference between them
        """

        # First, it convert the data images into a numy array
        numpy_image = np.array(data_image)
        substract_image = np.array(data_substract)

        # Numpy Arrays difference
        difference = numpy_image - substract_image

        return difference