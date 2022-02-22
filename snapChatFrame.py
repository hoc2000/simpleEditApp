from tkinter import *
import numpy as np
from PIL import Image, ImageTk
import cv2.cv2 as cv2
import dlib
from math import hypot


class SnapChatFrame(Toplevel):

    def __init__(self, master=None):
        Toplevel.__init__(self, master=master)

        self.original_image = self.master.processed_image
        self.edit_image = None
        self.title("snap chat")
        # Here is the snap chat photo
        self.dog=ImageTk.PhotoImage(Image.open("icon/icon_dog.jpg"))
        self.dal=ImageTk.PhotoImage(Image.open("icon/dalmatian icon.jpg"))
        self.santa =ImageTk.PhotoImage(Image.open("icon/Santa icon.jpg"))
        self.anime = ImageTk.PhotoImage(Image.open("icon/anime eye.jpg"))



        self.nose_image = cv2.imread("snapchat/snapchat_dog.png")# chó
        self.dalmatian = cv2.imread("snapchat/Dalmatian.png")#chó đốm
        self.hat = cv2.imread("snapchat/santa hat.png")#Ông già noel
        self.beared = cv2.imread("snapchat/santa_beared.png")
        self.right_eye=cv2.imread("snapchat/right eye.png")
        self.left_eye=cv2.imread("snapchat/left eye.png")

        #predictor face
        self.image_gray = cv2.cvtColor(self.original_image, cv2.COLOR_BGR2GRAY)
        self.detector = dlib.get_frontal_face_detector()
        self.predictor = dlib.shape_predictor("facedetection/shape_predictor_68_face_landmarks.dat")

        # Button

        self.dog_button = Button(self, bg="white", image=self.dog, borderwidth=0)
        self.label = Label(self, bg="white", text="puppy").grid(column=0, row=1, sticky='ew')
        self.dalmatian_button = Button(self, bg="white", image=self.dal, borderwidth=0)
        self.label = Label(self, bg="white", text="chó đốm").grid(column=1, row=1, sticky='ew')
        self.santa_button = Button(self, bg="white", image=self.santa, borderwidth=0)
        self.label = Label(self, bg="white", text="santa").grid(column=2, row=1, sticky='ew')
        self.anime_button= Button(self, bg="white", image=self.anime, borderwidth=0)
        self.label = Label(self, bg="white", text="anime eye").grid(column=3, row=1, sticky='ew')

        self.apply_button=Button(self,text="apply",bg="white")
        self.cancel_button=Button(self,text="cancel",bg="white")

        # BIND BUTTON
        self.dog_button.bind("<ButtonRelease>", self.dog_snapchat_button_released)
        self.dalmatian_button.bind("<ButtonRelease>", self.dalmatian_snapchat_button_released)
        self.santa_button.bind("<ButtonRelease>", self.santa_snapchat_button_released)
        self.anime_button.bind("<ButtonRelease>", self.anime_snapchat_button_released)
        self.apply_button.bind("<ButtonRelease>", self.apply_button_released)
        self.cancel_button.bind("<ButtonRelease>", self.cancel_button_released)

        # GRID
        self.dog_button.grid(column=0, row=0)
        self.dalmatian_button.grid(column=1, row=0)
        self.santa_button.grid(column=2, row=0)
        self.anime_button.grid(column=3,row=0)
        self.apply_button.grid(column=1,row=2)
        self.cancel_button.grid(column=2,row=2)


    def dog_snapchat_button_released(self, event):
        self.dog_snap()
        self.show_image()

    def dalmatian_snapchat_button_released(self, event):
        self.Dalmatian_snap()
        self.show_image()

    def santa_snapchat_button_released(self, event):
        self.santa_snap()
        self.show_image()
    def anime_snapchat_button_released(self,event):
        self.anime_snap()
        self.show_image()

    def apply_button_released(self, event):
        self.master.processed_image = self.edit_image
        self.show_image()
        self.close()

    def cancel_button_released(self, event):
        self.master.image_viewer.show_image()
        self.close()

    def show_image(self):
        self.master.image_viewer.show_image(img=self.edit_image)

    # Function
    def dog_snap(self):
        self.original_image = self.master.processed_image.copy()

        faces = self.detector(self.image_gray)
        for face in faces:
            landmarks = self.predictor(self.image_gray, face)
            # top_nose = (landmarks.part(27).x, landmarks.part(29).y)
            center = (landmarks.part(29).x, landmarks.part(29).y)
            left = (landmarks.part(31).x, landmarks.part(31).y)
            right = (landmarks.part(35).x, landmarks.part(35).y)

            # tính độ dài
            width = int(hypot(left[0] - right[0],
                              left[1] - right[1]) * 8)
            # tính hệ số cho height bằng cách lấy độ dài ảnh chia cho width
            height = int(width * 1.12)

            top_left = (int(center[0] - width / 2),
                        int(center[1] - height / 2))

            dog = cv2.resize(self.nose_image, (width, height))
            dog_gray = cv2.cvtColor(dog, cv2.COLOR_BGR2GRAY)
            _, mask = cv2.threshold(dog_gray, 25, 255, cv2.THRESH_BINARY_INV)

            area = self.original_image[top_left[1]:top_left[1] + height, top_left[0]:top_left[0] + width]
            nose_are_no_nose = cv2.bitwise_and(area, area, mask=mask)
            final = cv2.add(nose_are_no_nose, dog)

            self.edit_image = self.original_image
            self.edit_image[top_left[1]:top_left[1] + height, top_left[0]:top_left[0] + width] = final

    def anime_snap(self):
        self.original_image = self.master.processed_image.copy()

        faces = self.detector(self.image_gray)
        for face in faces:
            landmarks = self.predictor(self.image_gray, face)
            # top_nose = (landmarks.part(27).x, landmarks.part(29).y)
            center_eye1 = (landmarks.part(37).x, landmarks.part(37).y)
            left_eye1 = (landmarks.part(36).x, landmarks.part(36).y)
            right_eye1 = (landmarks.part(39).x, landmarks.part(39).y)

            # tính độ dài
            eye1_width = int(hypot(left_eye1[0] - right_eye1[0],
                                   left_eye1[1] - right_eye1[1]) * 2.4)
            # tính hệ số cho height bằng cách lấy độ dài ảnh chia cho width
            eye1_height = int(eye1_width * 0.5)

            top_left_eye1 = (int(center_eye1[0] - eye1_width / 2),
                             int(center_eye1[1] - eye1_height / 2))
            bottom_right_eye1 = (int(center_eye1[0] + eye1_width / 2),
                                 int(center_eye1[1] + eye1_height / 2))

            eye1 = cv2.resize(self.left_eye, (eye1_width, eye1_height))
            eye1_gray = cv2.cvtColor(eye1, cv2.COLOR_BGR2GRAY)
            _, nose_mask = cv2.threshold(eye1_gray, 25, 255, cv2.THRESH_BINARY_INV)

            eye1_area = self.original_image[top_left_eye1[1]:top_left_eye1[1] + eye1_height,
                        top_left_eye1[0]:top_left_eye1[0] + eye1_width]
            nose_are_no_nose = cv2.bitwise_and(eye1_area, eye1_area, mask=nose_mask)
            final_eye1 = cv2.add(nose_are_no_nose, eye1)

            # mắt phải
            center_eye2 = (landmarks.part(44).x, landmarks.part(44).y)
            left_eye2 = (landmarks.part(42).x, landmarks.part(42).y)
            right_eye2 = (landmarks.part(45).x, landmarks.part(45).y)

            # tính độ dài
            eye2_width = int(hypot(left_eye2[0] - right_eye2[0],
                                   left_eye2[1] - right_eye2[1]) * 2.4)
            # tính hệ số cho height bằng cách lấy độ dài ảnh chia cho width
            eye2_height = int(eye2_width * 0.5)

            top_left_eye2 = (int(center_eye2[0] - eye2_width / 2),
                             int(center_eye2[1] - eye2_height / 2))
            bottom_right = (int(center_eye2[0] + eye2_width / 2),
                            int(center_eye2[1] + eye2_height / 2))

            eye2 = cv2.resize(self.right_eye, (eye2_width, eye2_height))
            eye2_gray = cv2.cvtColor(eye2, cv2.COLOR_BGR2GRAY)
            _, nose_mask = cv2.threshold(eye2_gray, 25, 255, cv2.THRESH_BINARY_INV)

            eye2_area = self.original_image[top_left_eye2[1]:top_left_eye2[1] + eye2_height,
                        top_left_eye2[0]:top_left_eye2[0] + eye2_width]
            nose_are_no_nose = cv2.bitwise_and(eye2_area, eye2_area, mask=nose_mask)
            final_eye2 = cv2.add(nose_are_no_nose, eye2)
            self.edit_image = self.original_image

            self.edit_image[top_left_eye1[1]:top_left_eye1[1] + eye1_height,
            top_left_eye1[0]:top_left_eye1[0] + eye1_width] = final_eye1

            self.edit_image[top_left_eye2[1]:top_left_eye2[1] + eye2_height,
            top_left_eye2[0]:top_left_eye2[0] + eye2_width] = final_eye2

    def Dalmatian_snap(self):
        self.original_image = self.master.processed_image.copy()

        faces = self.detector(self.image_gray)
        for face in faces:
            landmarks = self.predictor(self.image_gray, face)
            # top_nose = (landmarks.part(27).x, landmarks.part(29).y)
            center = (landmarks.part(29).x, landmarks.part(29).y)
            left = (landmarks.part(31).x, landmarks.part(31).y)
            right = (landmarks.part(35).x, landmarks.part(35).y)


            width = int(hypot(left[0] - right[0],
                              left[1] - right[1]) * 7)

            height = int(width * 1.4)

            top_left = (int(center[0] - width / 2),
                        int(center[1] - height / 2))

            dalmatian = cv2.resize(self.dalmatian, (width, height))
            dalmatian_gray = cv2.cvtColor(dalmatian, cv2.COLOR_BGR2GRAY)
            _, mask = cv2.threshold(dalmatian_gray, 25, 255, cv2.THRESH_BINARY_INV)

            area = self.original_image[top_left[1]:top_left[1] + height, top_left[0]:top_left[0] + width]
            nose_are_no_nose = cv2.bitwise_and(area, area, mask=mask)
            final = cv2.add(nose_are_no_nose, dalmatian)

            self.edit_image = self.original_image

            self.edit_image[top_left[1]:top_left[1] + height, top_left[0]:top_left[0] + width] = final

    def santa_snap(self):
        self.original_image = self.master.processed_image.copy()
        faces = self.detector(self.image_gray)
        for face in faces:
            landmarks = self.predictor(self.image_gray, face)
            # top_nose = (landmarks.part(27).x, landmarks.part(29).y)
            center_hat = (landmarks.part(27).x, landmarks.part(27).y)
            left_hat = (landmarks.part(0).x, landmarks.part(0).y)
            right_hat = (landmarks.part(16).x, landmarks.part(16).y)

            width_hat = int(hypot(left_hat[0] - right_hat[0],
                                  left_hat[1] - right_hat[1]) * 1.3)

            height_hat = int(width_hat * 1.6)

            top_left_hat = (int(center_hat[0] - width_hat / 2),
                            int(center_hat[1] - height_hat / 2))

            hat = cv2.resize(self.hat, (width_hat, height_hat))
            hat_gray = cv2.cvtColor(hat, cv2.COLOR_BGR2GRAY)
            _, mask = cv2.threshold(hat_gray, 25, 255, cv2.THRESH_BINARY_INV)

            area = self.original_image[top_left_hat[1]:top_left_hat[1] + height_hat,
                   top_left_hat[0]:top_left_hat[0] + width_hat]
            nose_are_no_nose = cv2.bitwise_and(area, area, mask=mask)
            final_hat = cv2.add(nose_are_no_nose, hat)

            center_beared = (landmarks.part(57).x, landmarks.part(57).y)
            left_beared = (landmarks.part(4).x, landmarks.part(4).y)
            right_beared = (landmarks.part(12).x, landmarks.part(12).y)

            width_beared = int(hypot(left_beared[0] - right_beared[0],
                                     left_beared[1] - right_beared[1]) * 1.3)

            height_beared = int(width_beared * 1.2)

            top_left_beared = (int(center_beared[0] - width_beared / 2),
                               int(center_beared[1] - height_beared / 2))

            beared = cv2.resize(self.beared, (width_beared, height_beared))
            beared_gray = cv2.cvtColor(beared, cv2.COLOR_BGR2GRAY)
            _, mask = cv2.threshold(beared_gray, 25, 255, cv2.THRESH_BINARY_INV)

            area = self.original_image[top_left_beared[1]:top_left_beared[1] + height_beared,
                   top_left_beared[0]:top_left_beared[0] + width_beared]
            nose_are_no_nose = cv2.bitwise_and(area, area, mask=mask)
            final_beared = cv2.add(nose_are_no_nose, beared)

            self.edit_image = self.original_image
            self.edit_image[top_left_hat[1]:top_left_hat[1] + height_hat,
            top_left_hat[0]:top_left_hat[0] + width_hat] = final_hat
            self.edit_image[top_left_beared[1]:top_left_beared[1] + height_beared,
            top_left_beared[0]:top_left_beared[0] + width_beared] = final_beared

    def close(self):
        self.destroy()