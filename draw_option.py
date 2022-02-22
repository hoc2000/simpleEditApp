from tkinter import *

import imutils
import cv2.cv2 as cv2

class Draw(Toplevel):

    def __init__(self, master=None):
        Toplevel.__init__(self,width=300,height=800, master=master, bg='white')
        self.title("edit filter")
        self.ratio = 0
        self.draw_ids = list()
        self.black = PhotoImage(file='icon/black.png')
        self.white = PhotoImage(file='icon/white.png')
        self.cyan = PhotoImage(file='icon/blue.png')
        self.red = PhotoImage(file='icon/red.png')
        self.yellow = PhotoImage(file='icon/yellow.png')
        self.green = PhotoImage(file='icon/green.png')
        self.orange = PhotoImage(file='icon/orange.png')
        self.apply = PhotoImage(file='icon/accept.png')
        self.close =PhotoImage(file='icon/close.png')




        def button(x,y,text,image,event):
            mybutton=Button(self,bg="white",image=image,text=text,borderwidth=0)
            mybutton.bind("<ButtonRelease>", event)
            mybutton.grid(column=x, row=y, sticky='ew')

        button(0, 0, "black",self.black,self.black_button)
        button(1, 0, "white",self.white,self.white_button)
        button(2,0,"cyan",self.cyan,self.cyan_button)
        button(3,0,"red",self.red,self.red_button)
        button(4, 0, "yellow",self.yellow,self.yellow_button)
        button(5, 0, "green",self.green,self.green_button)
        button(6, 0, "orange",self.orange,self.orange_button)
        button(1,1,"ok",self.apply,self.apply_button)
        button(2,1,"thoats",self.close,self.close_button)

    def black_button(self,event):
        self.color="black"

    def white_button(self,event):
        self.color="white"
    def cyan_button(self,event):
        self.color="blue"

    def red_button(self,event):
        self.color="red"
    def yellow_button(self,event):
        self.color="yellow"
    def green_button(self,event):
        self.color="green"
    def orange_button(self,event):
        self.color="orange"

    def apply_button(self,event):
        self.master.image_viewer.maincolor =self.color
        self.master.image_viewer.activate_draw()
        self.close_button()


    def close_button(self):
        self.destroy()