import os
import time
import tkinter as tk
from tkinter.ttk import *
from tkinter import messagebox
from tkinter import *

class add_user (tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.geometry('500x500')

        self.label = Label(self, text = 'Please, wait!', font = ('Arial Bold', 20))
        self.label.grid(column = 0, row = 0)

        self.label_text = Label(self, text = 'We are updating data of all users', font = ('Arial Bold', 20))
        self.label_text.grid(column = 0, row = 1)

        v = 0
        self.progres = Progressbar(self, orient="horizontal", mode="determinate", maximum=100, value=v)
        self.progres.grid(column = 0, row = 2)
        while self.progres['value'] < 100: 
            self.progres['value'] += 10
            self.master.update() 
            time.sleep(0.5)
        
        self.label.destroy()
        self.label_text.destroy()
        self.label_up = Label(self, text = 'All users is up to date!', font = ('Arial Bold', 20))
        self.label_up.grid(column = 0, row = 0)

        self.exit = tk.Button(self, text="exit", command=self.destroy)
        self.exit.grid(column = 1, row = 3)

class del_user (tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.label = Label(self, text = 'Here u can delete user from system')
        self.label.grid(column = 0, row = 0)

        '''Надо прикрутить статус бар для обновлдения базы '''


class app(tk.Tk):
    def __init__(self):
        super().__init__()
        self.lbl = Label(self, text = 'Welcome administrator', font = ('Arial Bold', 20))
        self.lbl.grid(column = 0, row = 0)
        
        self.lbl_text = Label(self, text = 'What would u like too do?', font = ('Arial Bold', 15))
        self.lbl_text.grid(column = 0, row = 1)
        
        self.ch_1 = Button(self, text = 'Add all new users', command = self.add_user)
        self.ch_1.grid(column= 0, row = 2)

        self.ch_2 = Button(self, text = 'Delete all users', command = self.del_user)
        self.ch_2.grid(column = 1, row = 2)

        self.exit_btn = Button(self, text = 'Exit', command = self.exit_btn)
        self.exit_btn.grid(column = 0, row = 3)

    def add_user(self):
        add = add_user(self)
        add.grab_set()

    def del_user(self):
        del_us = del_user(self)
        del_us.grab_set()
        
    def exit_btn(self):
        self.destroy()
        os.system("python C:/pyton/курсач/bank.py")


if __name__ == "__main__":
    app = app()
    app.title('Bank app for admin v0.1')
    app.geometry('500x500')
    app.mainloop()