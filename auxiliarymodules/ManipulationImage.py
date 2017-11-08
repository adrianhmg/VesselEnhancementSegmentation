# -*- coding: utf-8 -*-

"""
Date                :  10/08/2017
Author              :  Adrián Homero Moreno García
Objective of Script :  This script has the functions that will be used for manipulate the image like reading,
                        copying, printing etc.
"""

import PIL.Image as img
import matplotlib.pyplot as plt
import scipy.misc as misc


class ManipulationImage:

    # Global variables
    WIDTH = 0 # Width of image:Int
    HEIGHT = 0  # Height of image: Int
    img_file = ''

    def read_image(self, img_name, img_mode):
        """
        Function for read image, scanning values of the original 
        image and store on global img_original = []
        :param img_name: string name of the ready image to be process.
        :param img_mode: type mode of reading image, in this case 8-bit grayscale 'L'
        :return: Returns the original image data
        """

        global WIDTH, HEIGHT, img_file
        img_file = img_name
        img_data = img.open(img_name).convert(img_mode)  # convert image to 8-bit grayscale

        WIDTH, HEIGHT = img_data.size

        img_original = list(img_data.getdata())  # convert image data to a list of integers


        # convert that to 2D list (list of lists of integers)
        img_original = [img_original[offset:offset + WIDTH]
                for offset in range(0, WIDTH * HEIGHT, WIDTH)]

        return img_original

    def print_images(self, images, titles, se_name, se_params):
        """
        This function creates a subplot, showing differences between 3 comparing methods, structuring elements,
        and gaussian pre-applied masks.
        :param images: Array with the images and hitograms to show on plot.
        :param titles: Array with the titles to show on plot.
        :param se_name: Structural element that was used in TopHat transform
        :param se_params: Size of the Structural element that was used in TopHat transform
        :return: No return
        """
        file_name = img_file[7:]

        # Title of subplot
        title_subplot = 'segmentation-results-'+file_name

        # Configuration of plt figure.
        fig = plt.figure(num=None, figsize=(12, 8), dpi=80, facecolor='w', edgecolor='k')
        fig.canvas.set_window_title(title_subplot)

        # This range the arrays and it organizes the subplot with the images and titles
        for i in range(3):
            plt.subplot(3, 4, i * 4 + 1), plt.imshow(images[i * 4], 'gray') # 1,4,7
            plt.title(titles[i * 4]), plt.xticks([]), plt.yticks([])

            plt.subplot(3, 4, i * 4 + 2), plt.hist(images[i * 4].ravel(), 256) # 2,5,8
            plt.title(titles[i * 4 + 1]), \
            plt.xlabel('Pixels Val: '+str(int(plt.hist(images[i * 4].ravel(), 256)[1].min())) +' to '+str(int(plt.hist(images[i * 4].ravel(), 256)[1].max()))),\
            plt.ylabel('Freq. Val: '+str(int(plt.hist(images[i * 4].ravel(), 256)[0].min())) +' to '+str(int(plt.hist(images[i * 4].ravel(), 256)[0].max()))),
            plt.xticks([]), plt.yticks([])

            plt.subplot(3, 4, i * 4 + 3), plt.imshow(images[i * 4 + 2], 'gray') # 3,6,9
            plt.title(titles[i * 4 + 2]), plt.xticks([]), plt.yticks([])

            plt.subplot(3, 4, i * 4 + 4), plt.imshow(images[i * 4 + 3], 'gray') # 3,6,9
            plt.title(titles[i * 4 + 3]), plt.xticks([]), plt.yticks([])


        plt.annotate('Structuring Element: '+se_name+', '+str(se_params), xy=(1, 1), xytext=(-8, 355), fontsize=11,
                    xycoords='axes fraction', textcoords='offset points',
                    bbox=dict(facecolor='red', alpha=0.8),
                    horizontalalignment='right', verticalalignment='top')

        title_subplot = title_subplot.replace('inputs/','')
        # It saves the plot in an image
        plt.savefig('images/outputs/' + title_subplot)
        # It shows the plot
        plt.show()

    def save_image(self, data, img_name):
        """
        This function save an image, giving an array of values.
        :param data: Is the list of values of the image.
        :param img_name: Name of the image to store.
        :return:
        """

        # Image name of file
        file_name = img_name[7:]

        # Title of the subplot
        file_name = file_name.replace('inputs/', '')
        title_subplot = 'segmentation-' + file_name

        # Path and name of the image to save, with data.
        misc.imsave('images/outputs/' + title_subplot, data)

# ---------------------------------------------------------------------------------------------------------------------- #
        """
        data_formating = []

        for y in range(HEIGHT):
            row = (data[y][x] for x in range(WIDTH))
            print(' '.join('{:3.2f}'.format(value) for value in row)) # format of values to print

        # formating to 4 decimals
        for row in data:
            for value in row:
                data_formating.append(float("{:1.4f}".format(value)))

        numpy_values = np.array(data_formating)

        numpy = np.reshape(numpy_values, (-1, 300))

        print(numpy)

        plt.imshow(numpy, cmap=plt.get_cmap(img_scale), vmin=min_grayscale, vmax=max_grayscale) # shows png image
        plt.show()
        """