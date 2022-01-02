import numpy as np
import time
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import csv
import main
from tkinter import *


"""
This class will create a Frame for the 
"""

class Window(Frame):
    # The method attaches the frame to the Window class
    def __init__(self, master=None):
        # The particular frame gets attaches
        Frame.__init__(self, master)
        # Setting the self.master to master so it is apart of the window Frame.
        self.master = master
        # Setting the self.label to label that initializes the clock
        self.label = Label(text="", fg="Red", font=("Helvetica", 9))
        # Where the self.label will be placed on the GUI application
        self.label.place(x=400, y=400)
        # Call the function update clock and adds it to the Frame
        self.update_clock()
        # Setting the menu to attach to the GUI application
        menu = Menu(self.master)
        # Connecting the self.master to the menu so it works very good.
        self.master.config(menu=menu)
        # Self.BotButton and put it in the frame
        self.BotButton = Button(text="Click this button to start the 'Andel' trading bot.",
                                command=self.update_clock())

    """
    This function will set up a clock in the GUI and updates the said clock 
    """

    def update_clock(self):
        # Creating the now variable to set up the time configuration
        now = time.strftime("%H:%M:%S")
        # Connect the label to the GUI
        self.label.configure(text=now)
        # Connecting the delay to 1 second to the GUI so the time signature can be true
        self.after(1000, self.update_clock)

    """
    This method will create the file menu in the GUI , as well 
    as reading and writing text in the file explorer 
    """

    def FileReading(self, master=None):
        menu = Menu(self.master)
        # Connecting the self.master to the menu so it works very good.
        self.master.config(menu=menu)
        # Creates the file menu
        fileMenu = Menu(menu)
        # Creates the label for Item
        fileMenu.add_command(label="Item")
        # Creates the exit label and the command to exit the file menu
        fileMenu.add_command(label="Exit", command=self.exitProgram)
        # Creating the file label and the file menu
        menu.add_cascade(label="File", menu=fileMenu)
        # Adding the edit menu to the frame
        editMenu = Menu(menu)
        # Creating the undo label for the edit menu
        editMenu.add_command(label="Undo")
        # Creating the undo label for the edit menu
        editMenu.add_command(label="Redo")
        # Creating the edit label and adding the edit menu to the menu
        menu.add_cascade(label="Edit", menu=editMenu)

    # The function to exit the GUI
    def exitProgram(self):
        exit()


# Creating the GUI
top = Tk()

# The dimensions of the GUI
top.geometry('550x450+700+200')

# The Title of the GUI
top.wm_title("Crypto Graph")

# Creating the Window in the GUI
Window = top

# Making the GUI visible
top.mainloop()
