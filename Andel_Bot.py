import numpy as np
import time
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import csv
import main
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow


"""
This class will create what will go into the app window, like the 
"""

class Window:
    # The method attaches the frame to the Window class
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle("Crypto App")


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
       bob = 7




    """
    This function will exit the file menu 
    """
    def exitProgram(self):
        exit()


app = QApplication(sys.argv)

w = Window

w.show()

app.exec()

