from PIL import Image, ImageTk

#Class qui gère le pacman
class pacman:
    def __init__(self, window, x, y):
        self.x = x
        self.y = y
        window.