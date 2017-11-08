# -*- coding: utf-8 -*-

"""
Date                :  18/08/2017
Author              :  Adrián Homero Moreno García
Objective of Script :  This script calculates the metrics and classifiers, given an segmented image
                        and a Grand Truth Image
"""
import numpy as np


class EvaluationMetrics:

    TP, FP, TN, FN, RN = 0, 0, 0, 0, 0


    def calculate_classifiers(self, segmented_image, grand_truth_image):
        """
        This function calculate the classifiers of 2 images.
        :param segmented_image: Values of the Segmented Image.
        :param grand_truth_image: Values of the Truth Image.
        :return: No return
        """
        grand_truth_image = np.array(grand_truth_image)

        rows = grand_truth_image.shape[0]
        cols = grand_truth_image.shape[1]

        global TP, FP, TN, FN, RN

        TP, FP, TN, FN, RN = 0, 0, 0, 0, 0

        # It calculates the classifers
        for x in range(0, rows):
            for y in range(0, cols):

                if grand_truth_image[x][y] == 255 and segmented_image[x][y] == 255:
                    TP += 1
                elif grand_truth_image[x][y] == 0 and segmented_image[x][y] == 255:
                    FP += 1
                elif grand_truth_image[x][y] == 0 and segmented_image[x][y] == 0:
                    TN += 1
                elif grand_truth_image[x][y] == 255 and segmented_image[x][y] == 0:
                    FN += 1
                else:
                    RN += 1


    def calculate_metrics(self):
        """
        Before this method, it is needed to execute the "calculate_classifiers" for get
        the classifiers and calculate the metrics, this order can be established in the principal class.
        :return: It return an array of metrics in order with every method
        """
        sensitivity = TP + FN
        sensitivity = TP / sensitivity

        specificity = TN + FP
        specificity = TN / specificity

        accuracy = TP + FP + TN + FN
        divisor = TP + TN
        accuracy = divisor / accuracy

        positive_predictive = TP + FP
        positive_predictive = TP / positive_predictive

        negative_predictive = TN + FN
        negative_predictive = TN / negative_predictive

        # This is for format decimal in metrics
        sensitivity = float("{0:.4f}".format(sensitivity))
        specificity = float("{0:.4f}".format(specificity))
        accuracy = float("{0:.4f}".format(accuracy))
        positive_predictive = float("{0:.4f}".format(positive_predictive))
        negative_predictive = float("{0:.4f}".format(negative_predictive))

        average = (sensitivity + specificity + accuracy + positive_predictive + negative_predictive) / 5

        average = float("{0:.4f}".format(average))

        metrics = [sensitivity, specificity, accuracy,positive_predictive,negative_predictive, average]

        return metrics
