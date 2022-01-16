import numpy as np
import time
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import csv
import main
import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

"""
This class will create what will go into the app window, like the 
"""


class Window(QMainWindow):
    # The method attaches the QMainWindow to the Window class
    def __init__(self):
        super().__init__()

        Layout = Window.QVBoxLayout()

        Layout.addWidget(self.GraphWindow())

        # Creating a label object
        self.label = QLabel()

        # Resizing the label
        self.label.resize(400, 350)

        # Getting the time by creating it. boom magic
        self.time = QDateTime

        # Setting the layout of GUI
        self.setLayout(QVBoxLayout())

        # Setting the text to a label
        text = self.label.text()
        self.label.setText(text)

        # Setting the font on the label
        self.label.setFont(QFont("Helvetica", 12))

        # Adding the widget to the layout
        self.layout().addWidget(self.label)

        # Calling the flop Calculate function.
        self.FlopsCalculate()

        self.ReadingCurrent()

        # Setting the window title
        self.setWindowTitle("Andel Trading Bot")
        # Setting the geometry of the window
        self.setGeometry(750, 750, 750, 750)

        # Calling the File Reading function
        self.FileReading()

        self.show()

    """
    This method will create the file menu in the GUI , as well 
    as reading and writing text in the file explorer 
    """

    def FileReading(self, master=None):
        # Creating the main menu and adding it to the window via self
        mainMenu = self.menuBar()
        # Creating the file menu and adds to the main menu with the name "File"
        fileMenu = mainMenu.addMenu('File')
        # Adding the new sub section
        fileMenu.addMenu("New")
        # Creating the edit menu and adds to the main menu with the name "Edit"
        editMenu = mainMenu.addMenu('Edit')
        # Creating the view menu and adds to the main menu with the name "View"
        viewMenu = mainMenu.addMenu('View')
        # Creating the search menu and adds to the main menu with the name "search"
        searchMenu = mainMenu.addMenu('Search')
        # Creating the tools menu and adds to the main menu with the name "Tools"
        toolsMenu = mainMenu.addMenu('Tools')
        # Creating the help menu and adds to the main menu with the name "Help"
        helpMenu = mainMenu.addMenu('Help')

    def ReadingCurrent(self):
        current_time = QDateTime.currentDateTime()
        self.time = current_time
        self.timeString = QDateTime.toString(self.time)
        label_time = current_time.toString('hh:mm:ss')
        self.label.setText(label_time)

    """   
    This function will create the frame that houses the graphs           
    """

    def GraphWindow(self):
        self.GraphFrame = QFrame()
        self.GraphFrame.resize(500, 500)

    """
    This function will exit the file menu in the GUI
    """

    def exitProgram(self):
        exit()

    """
    This function will calculate the FLOPS of this computer
    """

    def FlopsCalculate(self):
        # The number of sockets of a Ryzen 5 2600 cpu
        sockets = 1

        """
               The formula is FLOPS = sockets *(cores per socket) *(number of clock cycles per seecond)
               *(number of floating point operations per cycles)
        """

        # The number of core sockets in the 2600
        core_sockets = 6

        # The number of clock cycles that the 2600 can do as a base
        num_clock_cycles = 3400000

        # The number of floating point operations
        num_floating_point_operations = 8

        # The calculation to find the total number of FLOPS
        FLOPS_formula = (sockets * core_sockets) * (num_clock_cycles * num_floating_point_operations)

        # Divides the computation by a million
        FLops_num = FLOPS_formula / 1000000

        # IF Flops exceeds 100
        if FLops_num > 100:
            # converts the Flops to a String
            converted = str(FLops_num)
            # Adds 'Glops' to the String
            cpu_power = converted + " Glops"
            # Setting the cpu to a QLabel
            self.cpu_power = QLabel(cpu_power)
            # Setting the font on the label
            self.cpu_power.setFont(QFont("Arial", 12))
            # Changing the location of the Cpu power label to the GUI
            self.cpu_power.move(400, 200)
            # Adding to the layout
            self.layout().addWidget(self.cpu_power)


app = QApplication([])

window = Window()

app.exec()

sys.exit(app.exec())
