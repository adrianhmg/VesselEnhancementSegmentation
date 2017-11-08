# -*- coding: utf-8 -*-

"""
Date                :  15/08/2017
Author              :  Adrián Homero Moreno García
Objective of Script :  This script has function that generate the area opening or know also as bwareopen,
                       where it can be extract the area of interest.
"""


import cv2
import numpy as np

class AreaOfInterest:

    def generates_area_opening(self, image):
        """
        This function takes the image, then it calculates the connected component for take their areas,
        and then compare then into a minimum area for delete all the tiny components
        that are not relevant.
        :param image: Image that it will be extracted the area of interest.
        :return: It return the image with the area of interest.
        """
        # find all your connected components (white blobs in your image)
        nb_components, output, stats, centroids = cv2.connectedComponentsWithStats(image, connectivity=8)
        # connectedComponentswithStats yields every seperated component with information on each of them,
        #  such as size
        # the following part is just taking out the background which is also considered a component,
        # but most of the time we don't want that.
        sizes = stats[1:, -1]
        nb_components = nb_components - 1

        # minimum size of particles we want to keep (number of pixels)
        # here, it's a fixed value, but you can set it as you want, eg the mean of the sizes or whatever
        # in this case it takes the maximum area/2, in other words it takes the media
        min_size = 0
        if(sizes != []):
            min_size = max(sizes)/2

        # your answer image
        area_of_interest = np.zeros((output.shape), dtype=np.uint8)
        # for every component in the image, you keep it only if it's above min_size
        for i in range(0, nb_components):
            if sizes[i] >= min_size:
                area_of_interest[output == i + 1] = 255

        return area_of_interest