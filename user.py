import os
import tkinter as tk
from tkinter import messagebox
from tkinter import *

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.lbl = Label(self, text = 'Input login and password or register', font = ('Arial Bold', 20))
        self.lbl.grid(column = 0, row = 0)

        self.exit = tk.Button(self, text="exit", command=self.exit_btn)
        self.exit.grid(column = 1, row = 3)

    def exit_btn(self):
        self.destroy()
        os.system("python C:/pyton/курсач/bank.py")


if __name__ == "__main__":
    app = App()
    app.title('Bank app for user v0.1')
    app.geometry('500x500')
    app.mainloop()