from sys import version_info

from tkinter import *
from tkinter.ttk import *

"""
Tra ro = TK() e ro.mainloop() vanno definite le componenti della gui
"""
ro = Tk()
ro.title("Titolo")  # Titolo
ro.geometry("300x300+200+200")  # finestra grande 300 che si genrea a 200 px
ro.resizable(FALSE, FALSE)  # bloccare entrami o i lati di una gui

bt1 = Button(ro, text="destroy", command=ro.destroy).pack()
bt2 = Button(ro, text="small", command=ro.iconify).pack()

"""
nel definire un label che cambia non possiamo passare al comand del button una funzione con parametri quidni solo seza 
le parentesi e dunque bisogna escogitare qualcosa per passare diversamente i valori
"""
from random import randrange

def rand():
    lista = ["ciao", "hello", "hola"]
    x = randrange(0, 3)
    l1.config(text=lista[x])


l1 = Label(ro, text="Sono label")
l1.pack()
btLabel = Button(ro, text="Cambia", command=rand)
btLabel.pack()

ro.mainloop()
