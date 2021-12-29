from tkinter import ttk
import tkinter as tk

from editBar import EditBar
from imageViewer import ImageViewer


class Main(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)
#định các tham số còn rỗng
        self.filename = ""
        self.original_image = None
        self.processed_image = None
        self.is_image_selected = False
        self.is_draw_state = False
        self.is_crop_state = False

        self.iconbitmap('sample/seven.ico')
        self.title("Hoc_editor")



        self.filter_frame = None
        self.adjust_frame = None


        self.editbar = EditBar(master=self)
        # separator1 = ttk.Separator(master=self, orient=tk.HORIZONTAL)
        self.image_viewer = ImageViewer(master=self)

        self.editbar.grid(column=0,row=0)
        # separator1.pack(fill=tk.X, padx=20, pady=5)
        self.image_viewer.grid(column=1,row=0)

root =Main()
root.mainloop()