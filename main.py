from time import sleep
import os
import pathlib
from tkinter import *
from tkinter import messagebox
import tkinter.font as tkFont
from PIL import Image, ImageTk
from random import randint
from time import sleep

mywindow = Tk()




mywindow.resizable(False,False)
mywindow.wm_title("Pokémons")
mywindow.geometry("900x900")
mywindow.configure(bg="black")
canvas = Canvas(mywindow,width=1200, height=800, background='white')

