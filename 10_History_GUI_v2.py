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
                              '6 degrees C is -14.4 degrees F',
                              '7 degrees C is -13.9 degrees F']

        #self.all_calc_list = []
        # Converter Main screen GUI
        self.converter_frame = Frame(width=300, height=300, bg=background_color,
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
                                            padx=10, pady=10, command=lambda:
                                            self.history(self.all_calc_list))
        self.history_button.grid(row=1)

        #if len(self.all_calc_list) == 0:
            #self.history_button.config(state=DISABLED)

    def history(self, calc_history):
        History(self, calc_history)


class History:

    def __init__(self, partner, calc_history):

        print(calc_history)

        background = "#a9ef99"  # Pale green

        # disable history button
        partner.history_button.config(state=DISABLED)

        # sets up child window (ie. history box)
        self.history_box = Toplevel()

        #  If users press cross at top, close history and 'release' history
        self.history_box.protocol('WM_DELETE_WINDOW', partial(self.close_history, partner))

        # Set up GUI Frame
        self.history_frame = Frame(self.history_box, width=300, bg=background)
        self.history_frame.grid()

        # set up history heading (row 0)
        self.how_heading = Label(self.history_frame, text="Calculation History",
                                 font="arial 19 bold", bg=background)
        self.how_heading.grid(row=0)

        # history text (label, row 1 )
        self.history_text = Label(self.history_frame,
                                  text="Here are your most recent"
                                  "calculations. Please use the "
                                  "export button to create a text"
                                  "file of all your calculation for"
                                  "this session", wrap=250, font="arial 10 italic",
                                  justify=LEFT, width=40, bg=background)
        self.history_text.grid(row=1)

        # History Output goes here (row 2)

        # Generate string from list of calculation
        history_string = ""

        if len(calc_history) >= 7:
            for item in range(0,7):
                history_string += calc_history[len(calc_history)-item -1]+"\n"

        else:
            for item in calc_history:
                history_string += calc_history[len(calc_history) -
                                             calc_history.index(item) - 1] + "\n"
                self.history_text.config(text="here is your calculation "
                                              "history. You can use the "
                                              "export button to save this "
                                              "data to text file if desired!!")

        # Label to display calculation history to user
        self.calc_label = Label(self.history_frame, text=history_string,
                                bg=background,font="Arial 12", justify=LEFT)

        self.calc_label.grid(row=2)


        # Export / Dismiss Button Frame (row 3)
        self.export_dismiss_frame = Frame(self.history_frame)
        self.export_dismiss_frame.grid(row=3, pady=10)

        # Export Button
        self.export_button = Button(self.export_dismiss_frame, text="Export",
                                    font="Arial 12 bold")
        self.export_button.grid(row=0, column=0)

        # Dismiss Button
        self.dismiss_button = Button(self.export_dismiss_frame, text="Dismiss",
                                     font="Arial 12 bold", command=partial(self.close_history, partner))
        self.dismiss_button.grid(row=0, column=1)


    def close_history(self, partner):
        # Put history button back to normal...
        partner.history_button.config(state=NORMAL)
        self.history_box.destroy()

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    something = Converter(root)
    root.mainloop()