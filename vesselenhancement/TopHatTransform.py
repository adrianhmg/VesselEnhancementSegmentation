# -*- coding: utf-8 -*-

"""
Date                :  12/08/2017
Author              :  Adrián Homero Moreno García
Objective of Script :  This script has the main function that will call the classes
                       for make the process of the TopHatTransformation
"""
from auxiliarymodules.BasicOperations import BasicOperations
from auxiliarymodules.MorphologicalOperations import MorphologicalOperations
from auxiliarymodules.StructuringElements import StructuringElements


class TopHatTransform:
    # Global variables
    img_inverted = [] # List of values of the inverted image: list
    img_opening = [] # List of values of the opening gray image: list
    img_substract = []

    def generates_top_hat_transform(self, img_original, se_name, se_params):
        """
        Function that returns an image with a TopHat applied transform.
        :param img_original: Image to transform
        :param se_name: Name of the structuring element that will be used.
        :param se_params: Size of the structuring element that will be used.
        :return: Return the image resultant
        """
        global img_opening, img_inverted

         # -- STEPS OF TOP HAT TRANSFORM
        img_inverted = BasicOperations().invert_image(img_original)
        structuring_element = StructuringElements().create_structuring_element(se_name, se_params)
        img_opening = MorphologicalOperations().gray_opening_image(img_inverted, structuring_element)
        img_substract = BasicOperations().substract_imges(img_inverted, img_opening)

        return img_substract
