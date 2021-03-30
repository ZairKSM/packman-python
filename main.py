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



mywindow.resizable(False,False)
mywindow.wm_title("PacMan")
mywindow.geometry("900x900")
mywindow.configure(bg="black")
canvas = Canvas(mywindow,width=1200, height=800, background='white')

main(mywindow,canvas)

