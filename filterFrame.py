# from tkinter import Toplevel, Button, RIGHT
from tkinter import *
from PIL import Image, ImageTk
import numpy as np
import cv2.cv2 as cv2
from scipy.interpolate import UnivariateSpline


class FilterFrame(Toplevel):

    def __init__(self, master=None):
        Toplevel.__init__(self, master=master, bg='#141414')

        self.original_image = self.master.processed_image
        self.filtered_image = None
        self.title("edit filter")

        self.negative_button = Button(self, text="Negative")
        self.black_white_button = Button(self, text="Black White")
        self.sepia_button = Button(self, text="Sepia")
        self.emboss_button = Button(self, text="Emboss")
        self.gaussian_blur_button = Button(self, text="Gaussian Blur")
        self.median_blur_button = Button(self, text="Median Blur")
        self.cartoonify_button = Button(self, text="Hoạt hình hóa")
        self.bright_button = Button(self, text="Sauna")
        self.darken_button = Button(self, text="Trauma")
        self.sharpen_button = Button(self, text="Sắc nét")
        self.pencil1_button = Button(self, text="Sketch xám")
        self.pencil2_button = Button(self, text="Sketch màu")
        self.HDR_button = Button(self, text="HDR")
        self.Summer_button = Button(self, text="Ấm áp")
        self.Winter_button = Button(self, text="Lạnh giá")
        self.oldtime_button = Button(self, text="Cổ điển")
        self.poster_button =Button(self,text="Poster style")
        self.glitch_button =Button(self,text="Glitch")
        self.apply_button = Button(self, text="Apply")
        self.cancel_button = Button(self, text="Cancel")
        # BIND BUTTON
        self.negative_button.bind("<ButtonRelease>", self.negative_button_released)
        self.black_white_button.bind("<ButtonRelease>", self.black_white_released)
        self.sepia_button.bind("<ButtonRelease>", self.sepia_button_released)
        self.emboss_button.bind("<ButtonRelease>", self.emboss_button_released)
        self.gaussian_blur_button.bind("<ButtonRelease>", self.gaussian_blur_button_released)
        self.median_blur_button.bind("<ButtonRelease>", self.median_blur_button_released)
        self.cartoonify_button.bind("<ButtonRelease>", self.cartoonify_button_released)
        self.bright_button.bind("<ButtonRelease>", self.bright_button_released)
        self.darken_button.bind("<ButtonRelease>", self.darken_button_released)
        self.sharpen_button.bind("<ButtonRelease>", self.sharpen_button_released)
        self.oldtime_button.bind("<ButtonRelease>", self.oldtime_button_released)
        self.pencil1_button.bind("<ButtonRelease>", self.pencil_gray_button_released)
        self.pencil2_button.bind("<ButtonRelease>", self.pencil_colour_button_released)
        self.HDR_button.bind("<ButtonRelease>", self.HDR_button_released)
        self.Summer_button.bind("<ButtonRelease>", self.Summer_button_released)
        self.Winter_button.bind("<ButtonRelease>", self.Winter_button_released)
        self.poster_button.bind("<ButtonRelease>", self.poster_button_released)
        self.glitch_button.bind("<ButtonRelease>", self.glitch_button_realeased)
        self.apply_button.bind("<ButtonRelease>", self.apply_button_released)
        self.cancel_button.bind("<ButtonRelease>", self.cancel_button_released)
        # GUI VIEW

        self.negative_button.grid(column=0, row=0, sticky='ew')
        self.black_white_button.grid(column=1, row=0, sticky='ew')
        self.sepia_button.grid(column=2, row=0, sticky='ew')
        self.emboss_button.grid(column=0, row=1, sticky='ew')
        self.gaussian_blur_button.grid(column=1, row=1, sticky='ew')
        self.median_blur_button.grid(column=2, row=1, sticky='ew')
        self.cartoonify_button.grid(column=0, row=2, sticky='ew')
        self.bright_button.grid(column=1, row=2, sticky='ew')
        self.darken_button.grid(column=2, row=2, sticky='ew')
        self.sharpen_button.grid(column=0, row=3, sticky='ew')
        self.pencil1_button.grid(column=1, row=3, sticky='ew')
        self.pencil2_button.grid(column=2, row=3, sticky='ew')
        self.HDR_button.grid(column=0, row=4, sticky='ew')
        self.Summer_button.grid(column=1, row=4, sticky='ew')
        self.Winter_button.grid(column=2, row=4, sticky='ew')
        self.poster_button.grid(column=0,row=5,sticky ='ew')
        self.oldtime_button.grid(column=1, row=5, sticky='ew')
        self.glitch_button.grid(column=2,row=5,sticky='ew')
        self.apply_button.grid(column=0, row=6, sticky='ew')
        self.cancel_button.grid(column=2, row=6, sticky='ew')

    def LookupTable(self, x, y):
        spline = UnivariateSpline(x, y)
        return spline(range(256))

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

    def cartoonify_button_released(self, event):
        self.cartoonify()
        self.show_image()

    def bright_button_released(self, event):
        self.bright()
        self.show_image()

    def darken_button_released(self, event):
        self.darken()
        self.show_image()

    def sharpen_button_released(self, event):
        self.sharpen()
        self.show_image()

    def oldtime_button_released(self, event):
        self.oldtime()
        self.show_image()

    def pencil_gray_button_released(self, event):
        self.pencil_sketch_grey()
        self.show_image()

    def pencil_colour_button_released(self, event):
        self.pencil_sketch_col()
        self.show_image()

    def HDR_button_released(self, event):
        self.HDR()
        self.show_image()

    def Summer_button_released(self, event):
        self.Summer()
        self.show_image()

    def Winter_button_released(self, event):
        self.Winter()
        self.show_image()

    def poster_button_released(self,event):
        self.poster()
        self.show_image()

    def glitch_button_realeased(self,event):
        self.glitch_add()
        self.show_image()

    # lưu
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

        kernel = np.array([[0,-1,-1],
                            [1,0,-1],
                            [1,1,0]])


        self.filtered_image = cv2.filter2D(self.original_image, -1, kernel)

    def cartoonify(self):
        self.grey_image = cv2.cvtColor(self.original_image, cv2.COLOR_BGR2GRAY)
        self.blur_image = cv2.medianBlur(self.grey_image, 7)
        self.edges = cv2.adaptiveThreshold(self.blur_image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 2)
        # cv2.imshow('edges', edges)
        # cv2.waitKey()
        # cartoonize
        self.color = cv2.bilateralFilter(self.original_image, 9, 250, 250)
        self.filtered_image = cv2.bitwise_and(self.color, self.color, mask=self.edges)

    def gaussian_blur(self):
        self.filtered_image = cv2.GaussianBlur(self.original_image, (11, 11), 0)

    def median_blur(self):
        self.filtered_image = cv2.medianBlur(self.original_image, 7)

    ###################################################
    def bright(self):
        self.img_bright = cv2.convertScaleAbs(self.original_image, beta=60)
        self.filtered_image = self.img_bright

    def darken(self):
        self.img_bright = cv2.convertScaleAbs(self.original_image, beta=-60)
        self.filtered_image = self.img_bright

    def sharpen(self):
        kernel = np.array([[-1, -1, -1],
                           [-1, 9.5, -1],
                           [-1, -1, -1]])
        self.filtered_image = cv2.filter2D(self.original_image, -1, kernel)

    def oldtime(self):
        img_sepia = np.array(self.original_image, dtype=np.float64)  # converting to float to prevent loss
        img_sepia = cv2.transform(img_sepia, np.matrix([[0.272, 0.534, 0.131],
                                                        [0.349, 0.686, 0.168],
                                                        [0.393, 0.769,
                                                         0.189]]))  # multipying image with special sepia matrix
        img_sepia[np.where(img_sepia > 255)] = 255  # normalizing values greater than 255 to 255
        img_sepia = np.array(img_sepia, dtype=np.uint8)
        self.filtered_image = img_sepia

    def pencil_sketch_grey(self):
        grey_img = cv2.cvtColor(self.original_image, cv2.COLOR_RGB2GRAY)
        image_invert = cv2.bitwise_not(grey_img)
        img_smooth = cv2.GaussianBlur(image_invert, (21, 21), 0)
        invert_smooth = cv2.bitwise_not(img_smooth)

        sketch_image = cv2.divide(grey_img, invert_smooth, scale=256.0)
        self.filtered_image = sketch_image

    def pencil_sketch_col(self):
        sk_color = cv2.stylization(self.original_image, sigma_s=60, sigma_r=0.07, )
        self.filtered_image = sk_color

    def HDR(self):
        self.filtered_image = cv2.detailEnhance(self.original_image, sigma_s=12, sigma_r=0.15)

    def Summer(self):
        increaseLookupTable = self.LookupTable([0, 64, 128, 256], [0, 80, 160, 256])
        decreaseLookupTable = self.LookupTable([0, 64, 128, 256], [0, 50, 100, 256])
        blue_channel, green_channel, red_channel = cv2.split(self.original_image)
        red_channel = cv2.LUT(red_channel, increaseLookupTable).astype(np.uint8)
        blue_channel = cv2.LUT(blue_channel, decreaseLookupTable).astype(np.uint8)
        self.filtered_image = cv2.merge((blue_channel, green_channel, red_channel))

    def Winter(self):
        increaseLookupTable = self.LookupTable([0, 64, 128, 256], [0, 80, 160, 256])
        decreaseLookupTable = self.LookupTable([0, 64, 128, 256], [0, 50, 100, 256])
        blue_channel, green_channel, red_channel = cv2.split(self.original_image)
        red_channel = cv2.LUT(red_channel, decreaseLookupTable).astype(np.uint8)
        blue_channel = cv2.LUT(blue_channel, increaseLookupTable).astype(np.uint8)
        self.filtered_image = cv2.merge((blue_channel, green_channel, red_channel))

    def poster(self):
        image = self.original_image

        def ColourQuantization(img, K=9):
            Z = img.reshape((-1, 3))
            Z = np.float32(Z)
            criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.001)
            compactness, label, center = cv2.kmeans(Z, K, None, criteria, 1, cv2.KMEANS_RANDOM_CENTERS)
            center = np.uint8(center)
            res = center[label.flatten()]
            res2 = res.reshape((img.shape))
            return res2

        def Countours(img):
            contoured_image = img
            gray = cv2.cvtColor(contoured_image, cv2.COLOR_BGR2GRAY)
            edged = cv2.Canny(gray, 200, 200)
            contours, hierarchy = cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)[-2:]
            cv2.drawContours(contoured_image, contours, contourIdx=-1, color=6, thickness=1)
            return contoured_image

        coloured = ColourQuantization(image)
        contoured = Countours(coloured)
        self.filtered_image = contoured

    def glitch_add(self):

        foreg = cv2.imread("sample/glitch.jpg")
        width = int(self.original_image.shape[1])
        height = int(self.original_image.shape[0])
        dim = (width, height)
        fg = cv2.resize(foreg, dim)
        blend = cv2.addWeighted(self.original_image, 0.8, fg, 0.6, 0.0)

        self.filtered_image=blend
    ####################################################################

    def close(self):
        self.destroy()
