# -*- coding: utf-8 -*-

"""
Date                :  19/08/2017
Author              :  Adrián Homero Moreno García
Objective of Script :  This script has the objective to give a report of the metrics in
                        different methods, also it will be exported as .png
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

class ReportMetrics:

    def create_report(self, metrics, name_image, se_name, se_params):
        """
        This function create the report and showing it.
        :param metrics: Array with the metrics of the segmented image.
        :param name_image: Name of the image that is reporting metrics.
        :return: No return
        """
        file_name = name_image[7:]

        # Array of methods and titles, yes it is hard coded
        methods = ['R&C - 1/2 Gaussian', 'R&C Noisy', "Otsu's Gaussian"]
        titles = ['Sensitivity', 'Specificity', 'Accuracy', 'PPV', 'NPV', 'Average']

        fig = plt.figure(num=None, figsize=(11, 7), dpi=80, facecolor='w', edgecolor='k')
        fig.canvas.set_window_title('Report Metrics')

        dc = pd.DataFrame({'A': metrics[0], 'B': metrics[1], 'C': metrics[2]})

        # Plot for graphic
        plt.plot(dc)
        plt.legend(methods)
        dcsummary = dc

        # Creating table
        plt.table(cellText=dcsummary.values, colWidths=[0.25] * len(dc.columns),
                  rowLabels=titles,
                  colLabels=methods,
                  cellLoc='center', rowLoc='center',
                  loc='top')

        # Order of titles in X axe
        x = np.array([0, 1, 2, 3, 4 ,5])
        my_xticks = titles
        plt.xticks(x, my_xticks)

        # Subplot default settings of position
        plt.subplots_adjust(left=0.10, right=0.95, top=0.77)

        plt.annotate('Structuring Element: '+se_name+', '+str(se_params), xy=(1, 1), xytext=(-15, 95), fontsize=11,
                     xycoords='axes fraction', textcoords='offset points',
                     bbox=dict(facecolor='red', alpha=0.8),
                     horizontalalignment='right', verticalalignment='top')

        fig = plt.gcf()


        # Saving the plot of metrics
        extent = fig.get_window_extent().transformed(fig.dpi_scale_trans.inverted())
        file_name = file_name.replace('inputs/', '')
        fig.savefig('images/outputs/report-metrics'+file_name , bbox_inches=extent)

        # Showing the plot of report metrics
        plt.show()