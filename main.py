import os
import pathlib
from tkinter import *
from PIL import Image, ImageTk
from random import randint
from time import sleep

mywindow = Tk()

def main(mywindow,canvas):
    canvas.pack()
    mywindow.update()



mywindow.resizable(False,False)
mywindow.wm_title("PacMan")
mywindow.geometry("900x900")
mywindow.configure(bg="white")
canvas = Canvas(mywindow,width=1200, height=800, background='white')

main(mywindow,canvas)

mywindow.mainloop()

