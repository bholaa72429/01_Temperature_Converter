from tkinter import *
from functools import partial # to prevent unwanted windows

import random

class Converter:
    def __init__(self, parent):
        print("hello world")


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    something = Converter(root)
    root.mainloop()