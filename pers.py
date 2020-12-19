import tkinter as tk
from tkinter import messagebox
from tkinter import *

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.lbl = Label(self, text = 'Input login and password or register', font = ('Arial Bold', 20))
        self.lbl.grid(column = 0, row = 0)

    def say_hello(self):
        messagebox.showinfo("GUI Python", 'Hello, world')


if __name__ == "__main__":
    app = App()
    app.title('Bank app for user v0.1')
    app.geometry('500x500')
    app.mainloop()