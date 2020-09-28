import tkinter, time
from tkinter import *
from tkinter.ttk import *

def clicked():
    #lbl.configure(text = 'Loading, please wait')
    #inp = login.get() + '\n' + passw.get() + '\n\n'
    #with open('users.txt', 'a+') as f:
    #    f.write(inp)
    #lbl.configure(text = 'Input login and password')
    global window
    window.destroy()
    import user
def exit():
    global window
    window.destroy()

#create window
window = Tk()
window.title('Bank app v0.1')
window.geometry('500x500')

lbl = Label(window, text = 'Input login and password', font = ('Arial Bold', 30))
lbl.grid(column = 0, row = 0) #position

login = Entry(window, width=10)
login.grid(column = 0, row = 1)
login.focus()
passw = Entry(window, width=10)
passw.grid(column = 0, row = 2)

btn = Button(window, text = 'login', command = clicked)
btn.grid(column = 0, row = 3)

exit = Button(window, text = 'exit', command = exit)
exit.grid(column = 1, row = 3)

#loop for show window
window.mainloop()