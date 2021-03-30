import os
import pathlib
from tkinter import *
from PIL import Image, ImageTk
from random import randint
from time import sleep

mywindow = Tk()


#Fonction principale 
def main(mywindow,canvas):
    canvas.pack()
    mywindow.update()


#Truc de base
mywindow.resizable(False,False)
mywindow.wm_title("PacMan")
mywindow.geometry("600x600")
mywindow.configure(bg="white")
canvas = Canvas(mywindow,width=600, height=600, background='white')

#On lance la première fonction
main(mywindow,canvas)

mywindow.mainloop()

