# -*- coding: utf-8 -*-

"""
Date                :  12/08/2017
Author              :  Adrián Homero Moreno García
Objective of Script :  This scrpt has the main function that will call the classes
                       for make the complete process for segmented image.
"""

from auxiliarymodules.ManipulationImage import ManipulationImage
from auxiliarymodules.AreaOfInterest import AreaOfInterest

from segmentation.ThresholdingImage import ThresholdingImage
from vesselenhancement.TopHatTransform import TopHatTransform

from evaluationmetrics.ReportMetrics import ReportMetrics
from evaluationmetrics.EvaluationMetrics import EvaluationMetrics


class VesselEnhancementSegmentation:

    def main():
        #------------------------------------------------------------------------------------------------------------------#
        """
        USER INPUT:
        Here are the variables that the user can put on this program.
        *************************************************************
        se_name options are: diamond, cross, elliptical
        se_params options are: if it is diamond = dict(radius=n), and cross, elliptical= dict(width=n, height=n)
        """

        img_path = 'images/inputs/14.png'
        img_gt = 'images/inputs/14_gt.png'
        se_name = 'elliptical'
        se_params = dict(width=11, height=14)

        #------------------------------------------------------------------------------------------------------------------#
        # 1.- It reads the original image
        img_original = ManipulationImage().read_image(img_path, 'L')
        # 2.- It applies to it the TopHat Transform
        vessel_enhancement_image = TopHatTransform().generates_top_hat_transform(img_original, se_name, se_params)
        # 3.- It applies the Thresholding Images and gaussian filtering, it returns 3 images with different methods
        images, titles = ThresholdingImage().gaussian_otsu_thresholding(vessel_enhancement_image)
        # 4.- It generates the area of interest
        for i in range(3):
            images[i * 4 + 3] = AreaOfInterest().generates_area_opening(images[i * 4 + 3])
        # 5.- It print the 3 images results segmented images with different method of Thresholding
        ManipulationImage().print_images(images, titles, se_name, se_params)
        # 6.- It reads the Ground Truth image
        img_grand_truth = ManipulationImage().read_image(img_gt,'L')
        # 7.- It caluclates the respective metrics
        metrics = []
        for i in range(3):
            evaluation = EvaluationMetrics()
            evaluation.calculate_classifiers(images[i * 4 + 3], img_grand_truth)
            metrics.append(evaluation.calculate_metrics())
        # 8.- It creates the report of metrics
        ReportMetrics().create_report(metrics, img_path, se_name, se_params)
        # 9.- It select the best segmented image with better metrics and it save it.
        better_image = 0
        j = 0
        for i in range(3):
            if(better_image < metrics[i][5]):
                better_image = metrics[i][5]
                j = i

        index = (((j+1)*3)+j)
        ManipulationImage().save_image(images[index],img_path)

VesselEnhancementSegmentation.main()
