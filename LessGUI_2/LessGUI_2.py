from tkinter import *
from tkinter.ttk import *

root = Tk()
root.title("Img")

immagine = PhotoImage(file="611131.gif")
limg = Label(root, image=immagine).pack()

icona = PhotoImage(file="611131.gif")
root.tk.call("wm", "iconphoto", root._w, icona)

root.mainloop()
