import tkinter, time
from tkinter import *
from tkinter.ttk import *

user = Tk()
user.title('Bank app for user v0.1')
user.geometry('500x500')
lbl = Label(user, text = 'Input login and password or register', font = ('Arial Bold', 20))
lbl.grid(column = 0, row = 0)
user.mainloop()