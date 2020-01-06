from tkinter import *

from PIL import ImageTk, Image

root = Tk()

# set width and height


canvas = Canvas(root, width=1280, height=720)

# give this image path. image should be in png format.


# Example: "C:\\Users\\ASUS\\OneDrive\\Pictures\\image.png"


image = ImageTk.PhotoImage(Image.open("611131.gif"))

canvas.create_image(0, 0, anchor=NW, image=image)

canvas.grid(row=0, column=1)

l1 = Label(root, text="ciao", background = 'black' , foreground = "white")

l1.grid(row=0, column=1)

root.mainloop()
