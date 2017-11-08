# -*- coding: utf-8 -*-

"""
Date                :  02/08/2017
Author              :  Adrián Homero Moreno García
Objective of Script :  This script has function that manipulates the image using a structuring element,
                       some examples are: opening, closing, erosion & dilation, it is supported by the package
                       of scipy and uses ndimage for get the methods
"""

import numpy as np
import scipy.ndimage as ndimage

class MorphologicalOperations:

    def gray_opening_image(self, data, structuring_element):
        """
        This function makes the gray opening of the image, that consists on the dilation and erosion of an image
        :param data: This contains a list of the values of the image to transform
        :param structuring_element: This parameter has the the array of the structuring element that will be used
        :return: It returns the opening image data
        """
        image = np.array(data)

        img_gray_opening = ndimage.grey_opening(image, structure=structuring_element).astype(image.dtype)

        return img_gray_opening