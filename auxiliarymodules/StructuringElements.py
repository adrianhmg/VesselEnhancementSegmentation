# -*- coding: utf-8 -*-

"""
Date                :  01/08/2017
Author              :  Adrián Homero Moreno García
Objective of Script :  Create functions for produce different type of structuring elements, 
                       using numping arrays of pacakage numpy, for a better manipulation for operations
"""

import numpy as np
import cv2

class StructuringElements:

    def create_structuring_element(self, structuring_name, params):
        """
        This function is used to selected a type of structuring element and return it.
        :param structuring_name: Structuring elmenent name selected.
        :param params: Size of Structuring element selected.
        :return: It returns the structural element selected.
        """
        if(structuring_name == 'diamond'):
            return StructuringElements().create_diamond_mask(**params)
        elif(structuring_name == 'cross'):
            return StructuringElements().create_cross_shaped_mask(**params)
        elif(structuring_name == 'elliptical'):
            return StructuringElements().create_elipsed_mask(**params)


    def create_diamond_mask(self, radius):
        """
        This method will create a Diamond Structure element, the will be used 
        for the morphological operations of the image
        :param radius: Specifies the distance from the structuring element origin to the point of the diamond 
        :return: It returns the data of the  mask to be used
        """
        _radius_mask_ = radius + 1

        mask_values = []
        array_values = []

        for x in list(range(_radius_mask_)) + list(reversed(range(_radius_mask_ - 1))) + list(reversed(range(0))):
            mask_values.append('{:0<{w1}}{:1>{w2}}{:0<{w3}}'
                               .format('', '', '', w1=_radius_mask_ - x - 1, w2=x * 2 + 1, w3=_radius_mask_ - x - 1))

        for x in mask_values:
            for value in x:
                array_values.append(int(value))

        numpy_values = np.array(array_values)

        numpy_diamond = np.reshape(numpy_values, (-1, (radius*2)+1))

        return numpy_diamond

    def create_cross_shaped_mask(self, width, height):
        """
        Function for create a cross shaped structuring element.
        :param width: Width of the cross shaped structuring element.
        :param height: Height of the cross shaped structuring element.
        :return: It returns the cross shaped mask.
        """
        cross_mask = cv2.getStructuringElement(cv2.MORPH_CROSS, (width, height))

        return cross_mask

    def create_elipsed_mask(self, width, height):
        """
        Function for create a elipsed structuring element.
        :param width: Width of the elipsed structuring element.
        :param height: Height of the elipsed structuring element.
        :return: It returns the elipsed mask.
        """
        cross_mask = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (width, height))

        return cross_mask