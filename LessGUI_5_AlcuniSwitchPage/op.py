from tkinter import *

root = Tk()
root.geometry("500x500")


def new():
    ss.grid(row=0, column=0)


ss = Frame(root, height=200, width=200, bg="red")
ss.grid(row=0, column=0)

clean = Button(root, text="Delete", command=ss.grid_forget)
clean.grid(row=1, column=0)

add = Button(root, text="Add", command=new)
add.grid(row=2, column=0)

root.mainloop()