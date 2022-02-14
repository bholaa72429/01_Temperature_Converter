from tkinter import *
import random


class Converter:
    def __init__(self, parent):

        # Formatting variables..
        background_color = "light blue"

        # Converter Main Screen GUI..
        self.converter_frame = Frame(width=300, height=300, bg=background_color, pady=10)
        self.converter_frame.grid()

        # Temperature Conversion heading (row 0)
        self.temp_converter_label = Label(self.converter_frame, text="Temperature Converter",
                                          font=("Arial", "16", "bold"),
                                          bg=background_color,
                                          padx=10, pady=10)
        self.temp_converter_label.grid(row=0)

        # Help Button (rows 1)
        self.help_button = Button(self.converter_frame, text="Help",
                                  font=("Arial", "14"),
                                  padx=10, pady=10, command=self.help)
        self.help_button.grid(row=1)

    def help(self):
        print("You have asked for help.")
        get_help = Help(self)
        get_help.help_text.configure(text="Help text goes here ")

class Help:
    def __init__(self, partner):

        background = "orange"

        # disable help button
        partner.help_button.config(state=DISABLED)

        #Set up child window (ie. help box )
        self.help_box = Toplevel()

        # set up GUI Frame
        self.help_frame = Frame(self.help_box, bg=background)
        self.help_frame.grid()

        # set up Help heading (row 0)
        self.how_heading = Label(self.help_frame, text="Help / Instruction",
                                 font="arial 10 bold", bg=background)
        self.how_heading.grid(row=0)

        # Help text (label, row 1)
        self.how_text = Label(self.help_frame, text="",
                                 justify="arial 10 bold", bg=background, wrap=250)
        self.how_heading.grid(row=1)

        # Dismiss button (row 2)
        self.dismiss_btn = Label(self.help_frame, text="Dismiss", width=10,
                              justify="arial 10 bold", bg=background, wrap=250)
        self.dismiss_btn.grid(row=2)




# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    something = Converter(root)
    root.mainloop()