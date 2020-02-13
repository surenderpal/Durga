# import ctypes  # An included library with Python install.
# def Mbox(title, text, style):
#     return ctypes.windll.user32.MessageBoxW(0, text, title, style)
# Mbox('Your title', 'Your text', 1)
from Tkinter import *
from tkMessageBox import *

def answer():
    showerror("Answer", "Sorry, no answer available")

def callback():
    if askyesno('Verify', 'Have you dring Water?'):
        showwarning('Yes', 'close')
    else:
        showinfo('No', 'Please drink Water')

Button(text='Water', command=callback).pack(fill=X)
Button(text='Answer/Lunch', command=answer).pack(fill=X)
mainloop()
