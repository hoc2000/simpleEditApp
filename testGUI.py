from tkinter import *

w = Tk()
w.geometry('300x500')
w.configure(bg='#141414')


def ani(x, y, text, bcolor, fcolor,cmd):
    def on_enter(e):
        mybutton['background'] = bcolor
        mybutton['foreground'] = fcolor

    def on_leave(e):
        mybutton['background'] = fcolor
        mybutton['foreground'] = bcolor

    mybutton = Button(w, width=42, height=2, text=text,
                      fg=bcolor,
                      bg=fcolor,
                      border=0,
                      activeforeground=fcolor,
                      activebackground=bcolor,
                      command=cmd,)

    mybutton.bind("<Enter>", on_enter)
    mybutton.bind("<Leave>", on_leave)

    mybutton.place(x=x, y=y)

def cmd():
        print("lol")
ani(0, 0, "H E L L", '#ffcc66', '#141414',cmd)
w.mainloop()
