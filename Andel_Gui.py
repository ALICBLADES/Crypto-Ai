import psutil
import File_Explorer_System_Gauge as FESG
import sys

from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *

"""
This class will create what things will go into the app window
"""


class Window(QMainWindow):
    # The method attaches the QMainWindow to the Window class
    def __init__(self, CpuString):
        super(Window, self).__init__()

        # Setting the window title
        self.setWindowTitle("Andel Trading Bot")
        # Setting the geometry of the window
        self.setGeometry(750, 750, 750, 750)

        # Initialing the QWidget
        fileWidget = QWidget()

        # Adding the fileReading function to the file Widget
        fileWidget.setLayout(self.FileReading())

        self.setCentralWidget(fileWidget)

        self.Creating_Tabs(CpuString)

        # Showing the GUI window
        self.show()

    """
    This function will exit the file menu in the GUI
    """

    def exitProgram(self):
        exit()

    def FileReading(self):
        # Calling the status bar
        self.statusBar()

        # Initializing the menu bar
        menubar = self.menuBar()

        # Creating the file menu and adds to the main menu with the name "File"
        self.fileMenu = menubar.addMenu("File")

        # Adding the new subsection
        self.fileMenu.addMenu("New")

        # Creating the edit menu and add it to the main menu with the name "Edit"
        self.editMenu = menubar.addMenu('Edit')

        # Creating the view menu and adds it to the main menu with the name "View"
        self.viewMenu = menubar.addMenu("View")

        # Creating the view menu and adds it to the main menu with the name "search"
        self.seachMenu = menubar.addMenu("Search")

        # Creating the tool menu and adds it to the main menu with the name "Tools"
        self.toolsMenu = menubar.addMenu("Tools")

        # Creating the help menu and adds to the main menu with the name "Help"
        self.helpMenu = menubar.addMenu("Help")

    """
     This function will create tabs for the gui
    """

    def Creating_Tabs(self, CpuString):
        # Initializing the self tabs to the QTabWidget
        self.tabs = QTabWidget()

        # Add the first tab to the tabs with the name and tab
        self.tabs.addTab(InFirstTab(CpuString), "Simulation")

        self.tabs.addTab(SettingWidget(), "Settings")

        # Add the tab widget to the set central widget, so it is below the menu bar
        self.setCentralWidget(self.tabs)


"""
A class for the first tab which is the simulation, this tab will have a graph on the right side, taking up
most of the tab space on the middle to left side of the tab which will have the all the simulation 
information, such as the portfolio information, current balance, hourly lost/gain etc. And there will 
be a label that will tell the cpu usage on the bottom left hand side of the app gui. On the 
far left side there will be  
"""


class InFirstTab(QWidget):
    def __init__(self, CpuString):
        super().__init__()

        # Setting up the CpuString
        self.CpuString = CpuString

        # Calling the simulation method
        self.Simulation(CpuString)

    """
    This method will create the simulation information, and the portfolio information, which is the 
    net total, Loss, gains and percentage 
    """

    def Simulation(self, CpuString):
        # Creating the portfolio label
        portfolio = QLabel("Portfolio Information")

        # Creating the net total label
        net_total = QLabel("Net Total:")

        # Creating the loss label
        Loss = QLabel("Loss:")

        # Creating the Gain label
        Gain = QLabel("Gains:")

        # Creating the percentage label
        percentage = QLabel("Percentage:")

        # Setting the font and the size of the text of the portfolio text
        portfolio.setFont(QFont("Arial", 10))

        # Setting the font and the size of the text of the net total text
        net_total.setFont(QFont("Arial", 10))

        # Creating the QFormlayout on the simulation tab
        Sim_Layout = QFormLayout()

        # Adding the portfolio label to the form layout
        Sim_Layout.addWidget(portfolio)

        # Adding the net total label to the form layout
        Sim_Layout.addWidget(net_total)

        # Adding the Loss label to the form layout
        Sim_Layout.addWidget(Loss)

        # Adding the gains label to the form layout
        Sim_Layout.addWidget(Gain)

        label = QLabel

        con = InFirstTab.Continuing_Cpu_Update(self, label)

        Sim_Layout.addWidget(con)

        # Adding the percentage label to the form layout
        Sim_Layout.addWidget(percentage)

        # Adding the sim layout to the set layout, so it can be in the simulation tab
        self.setLayout(Sim_Layout)

    def Continuing_Cpu_Update (self, CpuString):

        self.sim_Form = InFirstTab.Simulation(self, CpuString)

        theCommunicate = FESG.Communicate(CpuString)

        self.fuck = FESG.Communicate.textUpdate

        theCommunicate.update(CpuString)

        while True:
           # Creating QLabel
            CpuLabel = QLabel()

            cpuMethod = theCommunicate.cpu_Updating(CpuString)

           # Setting the text to be the cpu percent as a str
            CpuLabel.setText(cpuMethod)

            return CpuLabel

class SettingWidget(QWidget):
    def __init__(self):
        super().__init__()

        # Calling the setting tab function
        self.SettingTab()

    def SettingTab(self):
        # Creating the Form layout
        self.layout = QFormLayout()

        # Calling the setting tab function
        self.checkLabel = QLabel()

        self.checkLabel.setText("If you want to see the cpu percent that "
                                + "this a computer is running at to determine how Andel bot's "
                                + "neural network affect on the current computer's cpu, " +
                                "click the box below.")

        # Creating the checkbox widget
        self.checkBox = QCheckBox()

        # Creating the button widget
        self.button = QPushButton()

        # Adding the check label to the layout
        self.layout.addWidget(self.checkLabel)

        # Add the checkbox to the layout
        self.layout.addWidget(self.checkBox)

        # Add the layout to the function, which adds it to the setting tab
        self.setLayout(self.layout)


app = QApplication()

CpuString = ""

window = Window(CpuString)

app.exec()
