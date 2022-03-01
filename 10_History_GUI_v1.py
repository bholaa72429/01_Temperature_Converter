from tkinter import *
from functools import partial # to prevent unwanted windows

import random


class Converter:
    def __init__(self, parent):

        # formatting variable
        background_color = "light blue"

        # In actual program this is blank and is populated with user calculation
        self.all_calc_list = ['1 degrees C is -17.2 degrees F',
                              '2 degrees C is -16.7 degrees F',
                              '3 degrees C is -16.1 degrees F',
                              '4 degrees C is -15.6 degrees F',
                              '5 degrees C is -15 degrees F',
                              '6 degrees C is -14.4 degrees F',
                              '7 degrees C is -13.9 degrees F']


        # Converter Main screen GUI
        self.converter_frame = Frame(bg=background_color,
                                     pady=10)
        self.converter_frame.grid()

        # Temperature Converter heading (row 0)
        self.temp_heading_label = Label(self.converter_frame,
                                        text="Temperature Converter",
                                            font="Arial 19 bold",
                                            bg=background_color,
                                            padx=10, pady=10)
        self.temp_heading_label.grid(row=0)

        # Help Button (row 1)
        self.history_button = Button(self.converter_frame,
                                            text="History",
                                            font="Arial 14",
                                            padx=10, pady=10, command=self.history)
        self.history_button.grid(row=1)

    def history(self):
        get_history = history(self)
        get_history.history_text.configure(text="History text goes here")

class history:
    def __init__(self, parent):

        backgrond = "#a9ef99"  # Pale green

        # disable history button
        partner.history_button.config(state=DISABLED)



    def round_it(self, to_round):
        if to_round % 1 == 0:
            rounded = int(to_round)
        else:
            rounded = round(to_round, 1)
        return rounded

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    something = Converter(root)
    root.mainloop()