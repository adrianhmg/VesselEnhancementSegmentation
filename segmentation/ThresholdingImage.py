# -*- coding: utf-8 -*-

"""
Date                :  19/08/2017
Author              :  Adrián Homero Moreno García
Objective of Script : The objective of this script is to Thresholding an Image with diferent methods and
                      applying gaussian blur.
"""

import mahotas as mh
import cv2
import numpy as np


class ThresholdingImage:

    def gaussian_otsu_thresholding(self, data):
        """ This function store the resulting image that has been in an thresholding process
        in diferent methods.
        :param data: The data of the image to process.
        :return: It return the images thresholded and the titles of the methods
        """
        # Otsu's thresholding after Gaussian filtering
        image_255 = np.array(data * 255, dtype=np.uint8)
        blur = cv2.GaussianBlur(image_255, (3, 5), 0)
        median_blur = cv2.medianBlur(image_255,7)

        # Ridler & Calvard thresholding with median blur
        ret1 = mh.rc(median_blur)
        th1 = ( median_blur > ret1)
        th1 = th1.astype(int)
        th1 = th1*255
        th1 = np.uint8(th1)

        # Rilder & Calvard thresholding without blur
        ret2 = mh.rc(image_255)
        th2 = ( image_255 > ret2)
        th2 = th2.astype(int)
        th2 = th2*255
        th2 = np.uint8(th2)

        # Otsu's thresholding after Gaussian filtering
        ret3, th3 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

        # plot all the images and their histograms
        images = [image_255, 0, th1,th1,
                  image_255, 0, th2,th2,
                  blur, 0, th3, th3]

        # plot al the titles
        titles = ['Median Gaussian filtered TopHat Image', 'Histogram Freq.', 'Ridler & Calvard Thresholding (v={0})'.format(int(ret1)),'Area Of Interest (AOI)',
                  'Original Noisy TopHat Image', 'Histogram Freq.', "Ridler & Calvard Thresholding (v={0})".format(int(ret2)),'Area Of Interest (AOI)',
                  'Gaussian filtered TopHat Image', 'Histogram Freq.', "Otsu's Thresholding (v={0})".format(int(ret3)), 'Area Of Interest (AOI)']

        # it return all the images, histogram and titles.
        return images, titles


