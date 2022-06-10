from tkinter import *
from datetime import datetime
from tkinter.ttk import *
from time import strftime
root = Tk()
root.title('clock')
label = Label(root, font=('ds-digital', 80),
              background='black', foreground='lightblue')
label.pack(anchor='center')


def fetchtime():
    now = datetime.now()
    t=now.strftime('%I:%M:%S %p %m/%d/%Y')
    label.config(text=t)
    label.after(1000, fetchtime)

fetchtime()
root.mainloop()
