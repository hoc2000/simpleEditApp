from tkinter import *
import numpy as np
import cv2.cv2 as cv2
import dlib
from math import hypot


class SnapChatFrame(Toplevel):

    def __init__(self, master=None):
        Toplevel.__init__(self, master=master)

        self.original_image = self.master.processed_image
        self.edit_image = None
        self.title("snap chat")
        # Here is the snap chat
        self.nose_image = cv2.imread("snapchat/snapchat_dog.png")
        self.dalmatian = cv2.imread("snapchat/Dalmatian.png")
        self.hat = cv2.imread("snapchat/santa hat.png")
        self.beared = cv2.imread("snapchat/santa_beared.png")

        self.image_gray = cv2.cvtColor(self.original_image, cv2.COLOR_BGR2GRAY)

        self.detector = dlib.get_frontal_face_detector()
        self.predictor = dlib.shape_predictor("facedetection/shape_predictor_68_face_landmarks.dat")

        # Button
        self.dog_button = Button(self, text="Dog")
        self.dalmatian_button = Button(self, text="Dalmatian")
        self.santa_button = Button(self, text="Santa")
        # BIND BUTTON
        self.dog_button.bind("<ButtonRelease>", self.dog_snapchat_button_released)
        self.dalmatian_button.bind("<ButtonRelease>", self.dalmatian_snapchat_button_released)
        self.santa_button.bind("<ButtonRelease>", self.santa_snapchat_button_released)
        # GRID
        self.dog_button.grid(column=0, row=0)
        self.dalmatian_button.grid(column=1, row=0)
        self.santa_button.grid(column=2, row=0)

    def dog_snapchat_button_released(self, event):
        self.dog_snap()
        self.show_image()

    def dalmatian_snapchat_button_released(self, event):
        self.Dalmatian_snap()
        self.show_image()

    def santa_snapchat_button_released(self, event):
        self.santa_snap()
        self.show_image()

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

    def Dalmatian_snap(self):
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
                              left[1] - right[1]) * 7)
            # tính hệ số cho height bằng cách lấy độ dài ảnh chia cho width
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
