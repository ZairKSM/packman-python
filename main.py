from time import sleep
import os
import pathlib
from tkinter import *
from PIL import Image, ImageTk
from random import randint

mywindow = Tk()

#Boucle principale
def main(mywindow,canvas):
    while True:
        mywindow.update()


#Truc de base
mywindow.resizable(False,False)
mywindow.wm_title("PacMan")
mywindow.geometry("600x600")
mywindow.configure(bg="black")
canvas = Canvas(mywindow,width=600, height=600, background='white')

#On lance la première fonction
main(mywindow,canvas)

mywindow.mainloop()

