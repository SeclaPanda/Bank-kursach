from tkinter import *
from tkinter.ttk import *

def exit():
    global window
    window.destroy()

def clicked():
    '''
    search = login.get() + ':' + passw.get()
    index = 0
    if search != ' ':
        with open('C:\pyton\курсач\data.txt', 'r') as data:
            for index, line in enumerate(data):
                if search in line:
                    if index == 0:
                    #exit()
                        import user
    '''
    global window
    window.destroy()
    
    import user

#create window
window = Tk()
window.title('Bank app v0.1')
window.geometry('500x500')

log = StringVar()
pas = StringVar()

lbl = Label(window, text = 'Input login and password', font = ('Arial Bold', 30))
lbl.grid(column = 0, row = 0) #position

login = Entry(window, width=10, textvariable=log)
login.grid(column = 0, row = 1)
login.focus()
passw = Entry(window, width=10, textvariable=pas)
passw.grid(column = 0, row = 2)

login_btn = Button(window, text = 'login', command = clicked())
login_btn.grid(column = 0, row = 3)

exit_btn = Button(window, text = 'exit', command = exit)
exit_btn.grid(column = 1, row = 3)

#loop for show window
window.mainloop()