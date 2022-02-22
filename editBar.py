# from tkinter import Frame, Button, LEFT
from tkinter import *
from tkinter import filedialog

from filterFrame import FilterFrame
from adjustFrame import AdjustFrame
from snapChatFrame import SnapChatFrame
import cv2.cv2 as cv2


class EditBar(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master=master, bg="gray24", width=100, height=800)
        self.openb = PhotoImage(file='icon/OPEN.png')
        self.saveb = PhotoImage(file='icon/SAVE.png')
        self.saveasb = PhotoImage(file='icon/SAVEAS.png')
        self.drawb = PhotoImage(file='icon/DRAW.png')
        self.cropb = PhotoImage(file='icon/CROP.png')
        self.flipb = PhotoImage(file='icon/FLIP.png')
        self.ninentyb = PhotoImage(file='icon/ROTATE90.png')
        self.minnusninetyb = PhotoImage(file='icon/ROTATE-90.png')
        self.filterb = PhotoImage(file='icon/FILTER.png')
        self.magicb =PhotoImage(file='icon/MAGIC.png')
        self.adjustb = PhotoImage(file='icon/ADJUST.png')
        self.clearb = PhotoImage(file='icon/CLEAR.png')
        self.snapb = PhotoImage(file='icon/SNAPCHHAT.png')
        self.quitb = PhotoImage(file='icon/QUIT.png')



        self.new_button = Button(self, bg="white", image=self.openb, width=70, borderwidth=0)
        self.label = Label(self, bg="white", text="open").grid(column=0, row=1, sticky='ew')

        self.save_as_button = Button(self, bg="white", image=self.saveasb, width=70, borderwidth=0)
        self.label = Label(self, bg="white", text="save").grid(column=1, row=1, sticky='ew')

        self.draw_button = Button(self, bg="white", image=self.drawb, width=70, borderwidth=0)
        self.label = Label(self, bg="white", text="draw").grid(column=2, row=1, sticky='ew')

        self.crop_button = Button(self, bg="white", image=self.cropb, width=70, borderwidth=0)
        self.label = Label(self, bg="white", text="crop").grid(column=3, row=1, sticky='ew')

        self.flip_button = Button(self, bg="white", image=self.flipb, width=70, borderwidth=0)
        self.label = Label(self, bg="white", text="flip").grid(column=4, row=1, sticky='ew')

        self.ninety_rotate_button = Button(self, bg="white", image=self.ninentyb, width=70, borderwidth=0)
        self.label = Label(self, bg="white", text="rotate 90").grid(column=5, row=1, sticky='ew')

        self.minus_ninety_rotate_button = Button(self, bg="white", image=self.minnusninetyb, width=70, borderwidth=0)
        self.label = Label(self, bg="white", text="rotate -90").grid(column=6, row=1, sticky='ew')

        self.filter_button = Button(self, bg="white", image=self.magicb, width=70, borderwidth=0)
        self.label = Label(self, bg="white", text="magic").grid(column=7, row=1, sticky='ew')

        self.adjust_button = Button(self, bg="white", image=self.adjustb, width=70, borderwidth=0)
        self.label = Label(self, bg="white", text="adjust").grid(column=8, row=1, sticky='ew')

        self.clear_button = Button(master=self, bg="white", image=self.clearb, width=70, borderwidth=0)
        self.label = Label(self, bg="white", text="snapchat").grid(column=9, row=1, sticky='ew')

        self.snapchat_button = Button(master=self, bg="white", image=self.snapb, width=70, borderwidth=0)
        self.label = Label(self, bg="white", text="clear").grid(column=10, row=1, sticky='ew')

        self.button_quit = Button(master=self, bg="white", image=self.quitb, borderwidth=0, command=self.quit)
        self.label = Label(self, bg="white", text="quit").grid(column=11, row=1, sticky='ew')
        # sử dựng bind() như cách khác để sử dụng button mà sử dụng class,

        self.new_button.bind("<ButtonRelease>", self.new_button_released)

        self.save_as_button.bind("<ButtonRelease>", self.save_as_button_released)
        self.draw_button.bind("<ButtonRelease>", self.draw_button_released)
        self.crop_button.bind("<ButtonRelease>", self.crop_button_released)
        self.flip_button.bind("<ButtonRelease>", self.flip_button_released)
        self.ninety_rotate_button.bind("<ButtonRelease>", self.ninety_rotate_button_released)
        self.minus_ninety_rotate_button.bind("<ButtonRelease>", self.minus_ninety_rotate_button_released)
        self.filter_button.bind("<ButtonRelease>", self.filter_button_released)
        self.adjust_button.bind("<ButtonRelease>", self.adjust_button_released)
        self.snapchat_button.bind("<ButtonRelease>", self.snapchat_button_released)
        self.clear_button.bind("<ButtonRelease>", self.clear_button_released)

        self.new_button.grid(column=0, row=0, sticky='ew')
        # self.save_button.pack(side=LEFT)
        self.save_as_button.grid(column=1, row=0, sticky='ew')
        self.draw_button.grid(column=2, row=0, sticky='ew')
        self.crop_button.grid(column=3, row=0, sticky='ew')
        self.flip_button.grid(column=4, row=0, sticky='ew')
        self.ninety_rotate_button.grid(column=5, row=0, sticky='ew')
        self.minus_ninety_rotate_button.grid(column=6, row=0, sticky='ew')
        self.filter_button.grid(column=7, row=0, sticky='ew')
        self.adjust_button.grid(column=8, row=0, sticky='ew')
        self.snapchat_button.grid(column=9, row=0, sticky='ew')
        self.clear_button.grid(column=10, row=0, sticky='ew')

        self.button_quit.grid(column=11, row=0, sticky='ew')

    # ===============================================================================================================================================
    def new_button_released(self, event):
        if self.winfo_containing(event.x_root, event.y_root) == self.new_button:
            if self.master.is_draw_state:
                self.master.image_viewer.deactivate_draw()
            if self.master.is_crop_state:
                self.master.image_viewer.deactivate_crop()
            # đọc file từ ô máy tính(file ảnh vì là edit ảnh sử dụng filedialong và askopenfilename())
            filename = filedialog.askopenfilename()
            image = cv2.imread(filename)

            if image is not None:
                self.master.filename = filename
                self.master.original_image = image.copy()
                self.master.processed_image = image.copy()
                self.master.image_viewer.show_image()
                self.master.is_image_selected = True
    #
    # def save_button_released(self, event):
    #     if self.winfo_containing(event.x_root, event.y_root) == self.save_button:
    #         if self.master.is_image_selected:
    #             if self.master.is_crop_state:
    #                 self.master.image_viewer.deactivate_crop()
    #             if self.master.is_draw_state:
    #                 self.master.image_viewer.deactivate_draw()
    #
    #             save_image = self.master.processed_image
    #             image_filename = self.master.filename
    #             cv2.imwrite(image_filename, save_image)

    def save_as_button_released(self, event):
        if self.winfo_containing(event.x_root, event.y_root) == self.save_as_button:
            if self.master.is_image_selected:
                if self.master.is_draw_state:
                    self.master.image_viewer.deactivate_draw()
                if self.master.is_crop_state:
                    self.master.image_viewer.deactivate_crop()

                original_file_type = self.master.filename.split('.')[-1]
                filename = filedialog.asksaveasfilename()
                filename = filename + "." + original_file_type

                save_image = self.master.processed_image
                cv2.imwrite(filename, save_image)

                self.master.filename = filename

    def draw_button_released(self, event):
        if self.winfo_containing(event.x_root, event.y_root) == self.draw_button:
            if self.master.is_image_selected:
                if self.master.is_crop_state:
                    self.master.image_viewer.deactivate_crop()
                if self.master.is_draw_state:
                    self.master.image_viewer.deactivate_draw()
                else:
                    self.master.image_viewer.activate_draw()

    def crop_button_released(self, event):
        if self.winfo_containing(event.x_root, event.y_root) == self.crop_button:
            if self.master.is_image_selected:
                if self.master.is_draw_state:
                    self.master.image_viewer.deactivate_draw()
                if self.master.is_crop_state:
                    self.master.image_viewer.deactivate_crop()
                else:
                    self.master.image_viewer.activate_crop()

    def flip_button_released(self, event):
        if self.winfo_containing(event.x_root, event.y_root) == self.flip_button:
            if self.master.is_image_selected:
                if self.master.is_draw_state:
                    self.master.image_viewer.deactivate_draw()
                if self.master.is_crop_state:
                    self.master.image_viewer.deactivate_crop()
                else:
                    self.master.image_viewer.activate_flip()
                    self.master.image_viewer.show_image()

    def minus_ninety_rotate_button_released(self, event):
        if self.winfo_containing(event.x_root, event.y_root) == self.minus_ninety_rotate_button:
            if self.master.is_image_selected:
                if self.master.is_draw_state:
                    self.master.image_viewer.deactivate_draw()
                if self.master.is_crop_state:
                    self.master.image_viewer.deactivate_crop()
                else:
                    self.master.image_viewer.activate_rotate_minus_90()
                    self.master.image_viewer.show_image()

    def ninety_rotate_button_released(self, event):
        if self.winfo_containing(event.x_root, event.y_root) == self.ninety_rotate_button:
            if self.master.is_image_selected:
                if self.master.is_draw_state:
                    self.master.image_viewer.deactivate_draw()
                if self.master.is_crop_state:
                    self.master.image_viewer.deactivate_crop()
                else:
                    self.master.image_viewer.activate_rotate_90()
                    self.master.image_viewer.show_image()

    def filter_button_released(self, event):
        if self.winfo_containing(event.x_root, event.y_root) == self.filter_button:
            if self.master.is_image_selected:
                if self.master.is_draw_state:
                    self.master.image_viewer.deactivate_draw()
                if self.master.is_crop_state:
                    self.master.image_viewer.deactivate_crop()

                self.master.filter_frame = FilterFrame(master=self.master)
                self.master.filter_frame.grab_set()

    def adjust_button_released(self, event):
        if self.winfo_containing(event.x_root, event.y_root) == self.adjust_button:
            if self.master.is_image_selected:
                if self.master.is_draw_state:
                    self.master.image_viewer.deactivate_draw()
                if self.master.is_crop_state:
                    self.master.image_viewer.deactivate_crop()

                self.master.adjust_frame = AdjustFrame(master=self.master)
                self.master.adjust_frame.grab_set()

    def snapchat_button_released(self, event):
        if self.winfo_containing(event.x_root, event.y_root) == self.snapchat_button:
            if self.master.is_image_selected:
                if self.master.is_draw_state:
                    self.master.image_viewer.deactivate_draw()
                if self.master.is_crop_state:
                    self.master.image_viewer.deactivate_crop()

                self.master.snapchat_frame = SnapChatFrame(master=self.master)
                self.master.snapchat_frame.grab_set()

    def clear_button_released(self, event):
        if self.winfo_containing(event.x_root, event.y_root) == self.clear_button:
            if self.master.is_image_selected:
                if self.master.is_draw_state:
                    self.master.image_viewer.deactivate_draw()
                if self.master.is_crop_state:
                    self.master.image_viewer.deactivate_crop()

                self.master.processed_image = self.master.original_image.copy()
                self.master.image_viewer.show_image()
