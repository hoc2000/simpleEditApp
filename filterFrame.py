# from tkinter import Toplevel, Button, RIGHT
from tkinter import *
from PIL import Image, ImageTk
import numpy as np
import cv2.cv2 as cv2
from scipy.interpolate import UnivariateSpline


class FilterFrame(Toplevel):

    def __init__(self, master=None):
        Toplevel.__init__(self,width=300,height=800, master=master, bg='#141414')

        self.original_image = self.master.processed_image
        self.filtered_image = None
        self.title("edit filter")

        def ani(x, y, text, bcolor, fcolor, event):
            def on_enter(e):
                mybutton['background'] = bcolor
                mybutton['foreground'] = fcolor

            def on_leave(e):
                mybutton['background'] = fcolor
                mybutton['foreground'] = bcolor

            mybutton = Button(self, width=42, height=2, text=text,
                              fg=bcolor,
                              bg=fcolor,
                              border=0,
                              activeforeground=fcolor,
                              activebackground=bcolor,
                              command=0, )

            mybutton.bind("<Enter>", on_enter)
            mybutton.bind("<Leave>", on_leave)
            mybutton.bind("<ButtonRelease>", event)
            mybutton.grid(column=x, row=y, sticky='ew')



        ani(0, 0, "NEGATIVE", '#ffcc66', '#141414', self.negative_button_released)
        ani(1, 0, "BLACK & WHITE", '#ffcc66', '#141414', self.black_white_released)
        ani(0, 1, "SEPIA", '#ffcc66', '#141414', self.sepia_button_released)
        ani(1, 1, "EMBOSS", '#ffcc66', '#141414', self.emboss_button_released)
        ani(0, 2, "GAUSSIAN BLUR", '#ffcc66', '#141414', self.gaussian_blur_button_released)
        ani(1, 2, "MEDIAN BLUR", '#ffcc66', '#141414', self.median_blur_button_released)
        ani(0, 3, "HOẠT HÌNH HÓA", '#ffcc66', '#141414', self.cartoonify_button_released)
        ani(1, 3, "SAUNA", '#ffcc66', '#141414', self.bright_button_released)
        ani(0, 4, "DARK", '#ffcc66', '#141414', self.darken_button_released)
        ani(1, 4, "SKETCH XÁM", '#ffcc66', '#141414', self.pencil_gray_button_released)
        ani(0, 5, "SKETCH MÀU", '#ffcc66', '#141414', self.pencil_colour_button_released)
        ani(1, 5, "HDR", '#ffcc66', '#141414', self.HDR_button_released)
        ani(0, 6, "SUMMER", '#ffcc66', '#141414', self.Summer_button_released)
        ani(1, 6, "WINTER", '#ffcc66', '#141414', self.Winter_button_released)
        ani(0, 7, "OLD TIME", '#ffcc66', '#141414', self.oldtime_button_released)
        ani(1, 7, "POSTER", '#ffcc66', '#141414', self.poster_button_released)
        ani(0, 8, "GLITCH", '#ffcc66', '#141414', self.glitch_button_realeased)
        ani(1, 8, "INSTANT", '#ffcc66', '#141414', self.instant_button_realeased)
        ani(0, 9, "PROCESS", '#ffcc66', '#141414', self.process_button_realeased)
        ani(1, 9, "ABSTRACT", '#ffcc66', '#141414', self.abstract_button_realeased)
        ani(0, 10, "apply", '#25dae9', '#141414', self.apply_button_released)
        ani(1,10, "cancel", '#25dae9', '#141414', self.cancel_button_released)


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

    def poster_button_released(self, event):
        self.poster()
        self.show_image()

    def glitch_button_realeased(self, event):
        self.glitch_add()
        self.show_image()

    def instant_button_realeased(self, event):
        self.Instant()
        self.show_image()

    def process_button_realeased(self, event):
        self.Process()
        self.show_image()

    def abstract_button_realeased(self, event):
        self.Abstract_Art()
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
        kernel = np.array([[0, -1, -1],
                           [1, 0, -1],
                           [1, 1, 0]])

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

        self.filtered_image = blend

    def Instant(self):
        red_img = np.full((682, 512, 3), (0, 0, 255), np.uint8)
        blue_img = np.full((682, 512, 3), (255, 0, 0), np.uint8)
        imgheight = self.original_image.shape[0]
        imgwidth = self.original_image.shape[1]

        # Cropping an image
        cropped_image = self.original_image[80:imgheight - 80, 80:imgwidth - 80]

        # Display cropped image
        dim = (imgwidth, imgheight)
        crop_resize = cv2.resize(cropped_image, dim)
        red = cv2.resize(red_img, dim)
        blue = cv2.resize(blue_img, dim)
        fused_red = cv2.addWeighted(crop_resize, 0.2, red, 0.8, 0.0)
        fused_img = cv2.addWeighted(self.original_image, 0.8, fused_red, 0.1, 0.0)
        final_img = cv2.addWeighted(fused_img, 0.8, blue, 0.2, 0.0)
        self.filtered_image = final_img

    def Process(self):
        red_img = np.full((682, 512, 3), (0, 0, 123), np.uint8)
        blue_img = np.full((682, 512, 3), (155, 0, 0), np.uint8)
        imgheight = self.original_image.shape[0]
        imgwidth = self.original_image.shape[1]

        # Cropping an image
        cropped_image = self.original_image[80:imgheight - 80, 80:imgwidth - 80]
        cropped_image2 = self.original_image[90:imgheight - 90, 90:imgwidth - 90]
        # Display cropped image
        dim = (imgwidth, imgheight)
        crop_resize = cv2.resize(cropped_image, dim)
        red = cv2.resize(red_img, dim)
        blue = cv2.resize(blue_img, dim)
        fused_red = cv2.addWeighted(crop_resize, 0.2, red, 0.8, 0.0)
        fused_img = cv2.addWeighted(self.original_image, 0.8, fused_red, 0.1, 0.0)
        final_img = cv2.addWeighted(fused_img, 0.8, blue, 0.3, 0.0)
        self.img_bright = cv2.convertScaleAbs(final_img, beta=60)
        self.filtered_image = self.img_bright
    def Abstract_Art(self):
         self.poster()
         processed_img=self.filtered_image
         self.grey_image = cv2.cvtColor(processed_img, cv2.COLOR_BGR2GRAY)
         self.blur_image = cv2.medianBlur(self.grey_image, 7)
         self.edges = cv2.adaptiveThreshold(self.blur_image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 2)
         # cv2.imshow('edges', edges)
         # cv2.waitKey()
         # cartoonize
         self.color = cv2.bilateralFilter(processed_img, 9, 250, 250)
         self.filtered_image = cv2.bitwise_and(self.color, self.color, mask=self.edges)

         img_warm=self.filtered_image

         increaseLookupTable = self.LookupTable([0, 64, 128, 256], [0, 80, 160, 256])
         decreaseLookupTable = self.LookupTable([0, 64, 128, 256], [0, 50, 100, 256])
         blue_channel, green_channel, red_channel = cv2.split(img_warm)
         red_channel = cv2.LUT(red_channel, increaseLookupTable).astype(np.uint8)
         blue_channel = cv2.LUT(blue_channel, decreaseLookupTable).astype(np.uint8)
         self.filtered_image = cv2.merge((blue_channel, green_channel, red_channel))




    ####################################################################

    def close(self):
        self.destroy()
