from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry ("1920x1080")
def hello():
	messagebox.showinfo("say hello", "hello world")

A = Button(root, text = "say hello", command = hello)
A.place (x = 50 , y = 500)
root.mainloop()