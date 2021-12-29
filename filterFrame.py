# from tkinter import Toplevel, Button, RIGHT
from tkinter import *
import numpy as np
import cv2.cv2 as cv2


class FilterFrame(Toplevel):

    def __init__(self, master=None):

        Toplevel.__init__(self, master=master)

        self.original_image = self.master.processed_image
        self.filtered_image = None
        self.title("edit filter")

        self.negative_button = Button(self, text="Negative")
        self.black_white_button = Button(self, text="Black White")
        self.sepia_button = Button(self, text="Sepia")
        self.emboss_button = Button(self, text="Emboss")
        self.gaussian_blur_button = Button(self, text="Gaussian Blur")
        self.median_blur_button = Button(self, text="Median Blur")
        self.cartoonify_button = Button(self,text="hoạt hình hóa")
        self.cancel_button = Button(self, text="Cancel")
        self.apply_button = Button(self, text="Apply")

        self.negative_button.bind("<ButtonRelease>", self.negative_button_released)
        self.black_white_button.bind("<ButtonRelease>", self.black_white_released)
        self.sepia_button.bind("<ButtonRelease>", self.sepia_button_released)
        self.emboss_button.bind("<ButtonRelease>", self.emboss_button_released)
        self.gaussian_blur_button.bind("<ButtonRelease>", self.gaussian_blur_button_released)
        self.median_blur_button.bind("<ButtonRelease>", self.median_blur_button_released)
        self.cartoonify_button.bind("<ButtonRelease>",self.cartoonify_button_released)
        self.apply_button.bind("<ButtonRelease>", self.apply_button_released)
        self.cancel_button.bind("<ButtonRelease>", self.cancel_button_released)

        self.negative_button.pack(side= LEFT)
        self.black_white_button.pack(side= LEFT)
        self.sepia_button.pack(side= LEFT)
        self.emboss_button.pack(side= LEFT)
        self.gaussian_blur_button.pack(side= LEFT)
        self.median_blur_button.pack(side= LEFT)
        self.cartoonify_button.pack(side= LEFT)
        self.cancel_button.pack(side= BOTTOM)
        self.apply_button.pack(side=BOTTOM)

    def negative_button_released(self, event):
        self.negative()
        self.show_image()

    def black_white_released(self, event):
        self.black_white()
        self.show_image()

    def sepia_button_released(self, event):
        self.sepia()
        self.show_image()

    def emboss_button_released(self, event):
        self.emboss()
        self.show_image()

    def gaussian_blur_button_released(self, event):
        self.gaussian_blur()
        self.show_image()

    def median_blur_button_released(self, event):
        self.gaussian_blur()
        self.show_image()

    def cartoonify_button_released(self,event):
        self.cartoonify()
        self.show_image()

    def apply_button_released(self, event):
        self.master.processed_image = self.filtered_image
        self.show_image()
        self.close()

    def cancel_button_released(self, event):
        self.master.image_viewer.show_image()
        self.close()

    def show_image(self):
        self.master.image_viewer.show_image(img=self.filtered_image)

    def negative(self):
        self.filtered_image = cv2.bitwise_not(self.original_image)

    def black_white(self):
        self.filtered_image = cv2.cvtColor(self.original_image, cv2.COLOR_BGR2GRAY)
        self.filtered_image = cv2.cvtColor(self.filtered_image, cv2.COLOR_GRAY2BGR)

    def sepia(self):
        kernel = np.array([[0.272, 0.534, 0.131],
                           [0.349, 0.686, 0.168],
                           [0.393, 0.769, 0.189]])

        self.filtered_image = cv2.filter2D(self.original_image, -1, kernel)

    def emboss(self):
        kernel = np.array([[0, -1, -1],
                           [1, 0, -1],
                           [1, 1, 0]])

        self.filtered_image = cv2.filter2D(self.original_image, -1, kernel)

    def cartoonify(self):
        self.grey_image = cv2.cvtColor(self.original_image, cv2.COLOR_BGR2GRAY)
        self.grey_image = cv2.medianBlur(self.grey_image, 5)
        self.edges = cv2.adaptiveThreshold(self.grey_image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)
        # cv2.imshow('edges', edges)
        # cv2.waitKey()
        # cartoonize
        self.color = cv2.bilateralFilter(self.original_image, 9, 250, 250)
        self.filtered_image = cv2.bitwise_and(self.color, self.color, mask=self.edges)

    def gaussian_blur(self):
        self.filtered_image = cv2.GaussianBlur(self.original_image, (21, 21), 0)

    def median_blur(self):
        self.filtered_image = cv2.medianBlur(self.original_image, 31)

    def close(self):
        self.destroy()
