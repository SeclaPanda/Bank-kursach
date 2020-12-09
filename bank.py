import os
import tkinter as tk
from tkinter import messagebox
from tkinter import *

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        log = StringVar()
        pas = StringVar()

        self.lbl = Label(self, text = 'Input login and password', font = ('Arial Bold', 30))
        self.lbl.grid(column = 0, row = 0) #position

        self.login = Entry(self, width=10, textvariable=log)
        self.login.grid(column = 0, row = 1)
        self.login.focus()
        self.passw = Entry(self, width=10, textvariable=pas)
        self.passw.grid(column = 0, row = 2)

        self.login_btn = Button(self, text = 'login', command = self.new_window)
        self.login_btn.grid(column = 0, row = 3)

        self.exit_btn = Button(self, text = 'exit', command = exit)
        self.exit_btn.grid(column = 1, row = 3)

    def new_window(self):
        log = str(self.login.get())
        pas = str(self.passw.get())
        search = (f'{log}:{pas}')
        index = self.find(search)
        #index = 0
        if index == 0:
            self.destroy() 
            os.system("python C:/pyton/курсач/user.py")
        elif index == 1:
            messagebox.showinfo("GUI Python", 'Hello, world')
        else:
            messagebox.showinfo("WARNING", 'Incorrect login or password')

    def find(self, search):
        with open('C:\pyton\курсач\data.txt', 'r') as data:
            for index, line in enumerate(data):
                if search in line:
                    return (index)

if __name__ == "__main__":
    app = App()
    app.title('Bank app v0.1')
    app.geometry('500x500')
    app.mainloop()