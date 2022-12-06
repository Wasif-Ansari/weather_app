from tkinter import *
from tkinter import ttk #combobox
import requests #to use apis


win = Tk()
win.title("Weather")
win.config(bg="blue")
win.geometry("500x600")

city_name = StringVar()

name = Label(win,text="MY WEATHER APP",font=("Time New Roman",30,"bold"))
name.place(x=25, y=50,height=50,width=450)


win.mainloop()