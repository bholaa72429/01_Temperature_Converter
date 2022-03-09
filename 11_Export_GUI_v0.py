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

        # export Button (row 1)
        self.export_button = Button(self.converter_frame,
                                            text="Export",
                                            font="Arial 14",
                                            padx=10, pady=10, command=lambda:
                                            self.history(self.export))
        self.export_button.grid(row=1)

    def export(self):
        get_export = Export(self)

class Export:

    def __init__(self, partner):

        background = "#a9ef99"  # Pale green

        # disable history button
        partner.export_button.config(state=DISABLED)

        # sets up child window (ie. history box)
        self.export_box = Toplevel()

        #  If users press cross at top, close history and 'release' history
        self.export_box.protocol('WM_DELETE_WINDOW', partial(self.close_export, partner))

        # Set up GUI Frame
        self.export_frame = Frame(self.export_box, width=300, bg=background)
        self.export_frame.grid()

        # set up history heading (row 0)
        self.how_heading = Label(self.export_frame, text="Export / Instruction",
                                 font="arial 19 bold", bg=background)
        self.how_heading.grid(row=0)

        # history text (label, row 1 )
        self.export_text = Label(self.export_frame,
                                  text="Enter a filename "
                                       "in the box below"
                                       "and press the SAVE "
                                       "button to save your "
                                       "calculation history"
                                       "to the text file",
                                 wrap=250, font="arial 10 italic",
                                  justify=LEFT, width=40, bg=background)
        self.export_text.grid(row=1)

        # Warning text (label, row 2)
        self.export_text = Label(self.export_frame, text = "If the filename you "
                                                           "entered below"
                                                           "already exists,"
                                                           "its content will be "
                                                           "replaced with your calculation history",
                                 justify=LEFT,bg='#ffafaf', fg='maroon',
                                 font="Arial 10 italic",wrap=225, padx=10, pady=10)
        self.export_text.grid(row=2, pady=10)

        # Filename entry box (row 3)
        self.filename_entry = Entry(self.export_frame, width=20,
                                    font="Arial 14 bold", justify=CENTER)
        self.filename_entry.grid(row=3, pady=10)

        # Save \ Cancel Frame (row 4)
        self.save_cancel_frame = Frame(self.export_frame)
        self.save_cancel_frame .grid(row=5, pady=10)

        # Save \ Cancel BUTTON (row 0 of save_cancel_frame)
        self.save_button = Button(self.save_cancel_frame, text="save")
        self.save_button.grid(row=0, column=0)

        self.cancel_button = Button(self.save_cancel_frame, text="Cancel",
                                    command=partial(self.close_export, partner))
        self.cancel_button.grid(row=0, column=1)

    def close_export(self, partner):
        #Put export button back
        partner.export_button.config(state=NORMAL)
        self.export_box.destroy()



# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    something = Converter(root)
    root.mainloop()