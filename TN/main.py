from tkinter import *


root = Tk()

# Library Menu

def library():
    xor = Tk()

    libmen = Menu(root, bg="blue")
    root.config(menu=libmen)

    d = Label(xor, text="-LIBRARY-\nGucci Forema\nDisco Girl\nEye of yo mama", bg="red")
    d.pack(fill=X)

    fr = Frame(xor, width=700, height=300, bg="blue")
    fr.pack()

    xor.mainloop()


# Menu

menu = Menu(root)
root.config(menu=menu)




s = Label(root, text="MENU", bg="red")
s.pack(fill=X)

# VersTone Label

status = Label(root, text="VerseTone", bd=1, relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM, fill=X)


# Buttons

toolbar = Frame(root, bg="blue")

insertButt = Button(toolbar, bg="green", text="Search a song")
insertButt.pack(padx=2, pady=2)

toolbar.pack(fill=X)

toolbar = Frame(root, bg="blue")

insertButt2 = Button(toolbar, bg="green", text="Library", command=library)
insertButt2.pack(padx=2, pady=20)

toolbar.pack(fill=X)

toolbar = Frame(root, bg="blue")

insertButt3 = Button(toolbar, bg="green", text="Charts", command=3)
insertButt3.pack(padx=2, pady=2)

toolbar.pack(fill=X)

toolbar = Frame(root, bg="blue")

insertButt4 = Button(toolbar, bg="green", text="Account", command=3)
insertButt4.pack(padx=2, pady=20)

toolbar.pack(fill=X)

toolbar = Frame(root, bg="blue")

insertButt5 = Button(toolbar, bg="green", text="Add Song", command=3)
insertButt5.pack(padx=2, pady=2)

toolbar.pack(fill=X)

toolbar = Frame(root, bg="blue")

insertButt12 = Button(toolbar, bg="green", text="Exit", command=quit)
insertButt12.pack(padx=2, pady=2)

toolbar.pack(side=BOTTOM, fill=X)

toolbar = Frame(root, bg="blue")

insertButt6 = Button(toolbar, bg="green", text="Rate Us", command=3)
insertButt6.pack(padx=2, pady=10)

toolbar.pack(side=BOTTOM, fill=X)

toolbar = Frame(root, bg="blue")

insertButt7 = Button(toolbar, bg="green", text="About Us", command=3)
insertButt7.pack(padx=2, pady=10)

toolbar.pack(side=BOTTOM, fill=X)

toolbar = Frame(root, bg="blue")

insertButt8 = Button(toolbar, bg="green", text="FAQ", command=3)
insertButt8.pack(padx=2, pady=10)

toolbar.pack(side=BOTTOM, fill=X)

# Frame

fr = Frame(root, width=700, height=300, bg="blue")
fr.pack()

root.mainloop()