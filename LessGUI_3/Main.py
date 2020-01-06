from tkinter import *


def Send():
    user = "mioutente"
    psw = "miapassword"
    if username.get() == user and PASSWORD.get() == psw:
        print("Effettuato")
    else:
        print("Errato!")


root = Tk()
root.title("LogIn")
root.configure(bg="white")

username = StringVar(value="")
PASSWORD = StringVar(value="")

luser = Label(root, text="Inserisci username: ", bg="white", padx=10, pady=10)
lpassword = Label(root, text="Inserisci la password: ", bg="white")

euser = Entry(root, textvariable=username)
epassword = Entry(root, textvariable=PASSWORD, show="*")

send = Button(root, text="Login", command=Send)

"""
Per orinare le componenti usiamo un sistema a griglia
"""
luser.grid(row=0, column=0, padx=10, pady=10)
lpassword.grid(row=1, column=0, padx=10, pady=10)
euser.grid(row=0, column=1, padx=10, pady=10)
epassword.grid(row=1, column=1, padx=10, pady=10)
send.grid(row=2, column=0, columnspan=2, padx=10, pady=10)


def cambia():
    if variabile.get() == 0:
        lCheck.config(text="Off")
    if variabile.get() == 1:
        lCheck.config(text="On")



root.title("Checkbutton")
lCheck = Label(root, text="")
"""
Il checkbutton restituira' i seguenti valori:
0, nel caso in cui il checkbutton non sia spuntato
1, nel caso in cui il checkbutton sia spuntato
"""
variabile = IntVar()
cb1 = Checkbutton(root,
                  text="Checkbutton",
                  variable=variabile,
                  command=cambia)

lCheck.grid(row=4, column=0, padx=10, pady=10)
cb1.grid(row=5, column=0, padx=10, pady=10)
root.mainloop()
