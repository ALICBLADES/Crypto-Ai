import matplotlib.pyplot as plt
import numpy as np
import sys
import coinbase
import configparser
import pandas
import requests
import os
import time
import psutil
from threading import Timer

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

"""
This class will create what things will go into the app window
"""


class Window(QMainWindow):
    # The method attaches the QMainWindow to the Window class
    def __init__(self):
        super().__init__()

        # Setting the window title
        self.setWindowTitle("Andel Trading Bot")
        # Setting the geometry of the window
        self.setGeometry(750, 750, 750, 750)

        # Creating a label object
        self.label = QLabel()

        # Resizing the label
        self.label.resize(400, 350)

        self.label.setText("hi")

        # Setting the font on the label
        self.label.setFont(QFont("Helvetica", 12))

        # Calling the file reading method
        self.FileReading()

        # Calling the Creating Tabs method
        self.Creating_Tabs()

        # Showing the GUI window
        self.show()

    """
    This method will create the file menu in the GUI, as well
    as reading and writing text in the file explorer
    """

    def FileReading(self):
        # Creating the main menu and adding it to the window via self
        mainMenu = self.menuBar()

        # Creating the file menu and adds to the main menu with the name "File"
        fileMenu = mainMenu.addMenu('File')

        # Adding the new subsection
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

    """
    This method will create a time stamp 
    """

    def ReadingCurrent(self):
        # Creating this variable to get the Current Time
        current_time = QDateTime.currentDateTime()

        # Setting the current time to the window
        self.time = current_time

        # Setting the time to a String and to the Window
        self.timeString = QDateTime.toString(self.time)

        # Formats the time in seconds, minutes and hours
        label_time = current_time.toString('hh:mm:ss')

        # Setting the label and puts the time on the gui
        self.label.setText(label_time)

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
               The formula is FLOPS = sockets *(cores per socket) *(number of clock cycles per second)
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

    """
     This function will create tabs for the gui
    """

    def Creating_Tabs(self):
        # Initializing the self tabs to the QTabWidget
        self.tabs = QTabWidget()

        # Add the first tab to the tabs with the name and tab
        self.tabs.addTab(InFirstTab(), "Simulation")

        # Add the tab widget to the set central widget, so it is below the menu bar
        self.setCentralWidget(self.tabs)


class WhileThread(QThread):

    signal = pyqtSignal(QLabel)

    def __init__(self, parent=None):
        super(WhileThread, self).__init__(parent)



"""
A class for the first tab which is the simulation, this tab will have a graph on the right side, taking up
most of the tab space on the middle to left side of the tab which will have the all the simulation 
information, such as the portfolio information, current balance, hourly lost/gain etc. And there will 
be a label that will tell the cpu usage on the bottom left hand side of the app gui. On the 
far left side there will be  
"""


class InFirstTab(QWidget):
    def __init__(self):
        super().__init__()

        # Calling the simulation method
        self.Simulation()

        #self.thread = WhileThread()







    def RunCpuUsage(self):

            cpu_time = psutil.cpu_percent(interval=None)

            cpuString = "".join(str(cpu_time))

            self.labelCpu = QLabel(cpuString)





    """
    This function will run the cpu usage in a while loop so it can update it's self 
    """

    def Cpu_Usage(self):
        cpu_time = psutil.cpu_percent(interval=1, percpu=False)
        for x in range(map(str(cpu_time))):


        for rows in range(num_cores // NUM_COLS + 1):
            # for cols in range(min(num_cores-rows*NUM_COLS, NUM_COLS)):
            layout += [[GraphColumn('CPU ' + str(rows * NUM_COLS + cols), (rows, cols)) for cols in
                        range(min(num_cores - rows * NUM_COLS, NUM_COLS))]]

            cpu_time = psutil.cpu_percent(interval=1, percpu=False)
            cpuString = "".join(str(cpu_time))
            self.cpuTime = QLabel("Cpu Usage is " + cpuString + "%")
            return self.cpuTime

    """
    This method will create the simulation information, and the portfolio information, which is the 
    net total, Loss, gains and percentage 
    """

    def Simulation(self):

        # Creating the portfolio label
        self.portfolio = QLabel("Portfolio Information")

        # Creating the net total label
        self.net_total = QLabel("Net Total:")

        # Creating the loss label
        self.Loss = QLabel("Loss:")

        # Creating the Gain label
        self.Gain = QLabel("Gains:")

        # Creating the percentage label
        self.percentage = QLabel("Percentage:")

        # Setting the font and the size of the text of the portfolio text
        self.portfolio.setFont(QFont("Arial", 10))

        # Setting the font and the size of the text of the net total text
        self.net_total.setFont(QFont("Arial", 10))

        # Creating the QFormlayout on the simulation tab
        self.Sim_Layout = QFormLayout()

        # Adding the portfolio label to the form layout
        self.Sim_Layout.addWidget(self.portfolio)

        # Adding the net total label to the form layout
        self.Sim_Layout.addWidget(self.net_total)

        # Adding the Loss label to the form layout
        self.Sim_Layout.addWidget(self.Loss)

        # Adding the gains label to the form layout
        self.Sim_Layout.addWidget(self.Gain)

        # Adding the percentage label to the form layout
        self.Sim_Layout.addWidget(self.percentage)

        while True:
            self.Sim_Layout.addWidget(self.Cpu_Usage())


        # Adding the sim layout to the set layout, so it can be in the simulation tab
        self.setLayout(self.Sim_Layout)


app = QApplication([])

window = Window()

app.exec()
