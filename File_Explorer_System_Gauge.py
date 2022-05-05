import time
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import Signal, Slot, QObject
import psutil

"This class will create the Signal and slot in order to connect the method " \
"cpu_Updating and to connect it with the class InFirstTab"


class Communicate(QObject):
    # Initializing the text update to the Signal that includes a string
    textUpdate = Signal(str)

    def __init__(self, CpuString):
        super(Communicate, self).__init__()
        # Setting up the CpuString
        self.CpuString = CpuString

    def exitProgram(self):
        pass

    @Slot(str)
    def cpu_Updating(self, CpuString):
        # Getting the cpu percent
        cpu_time = psutil.cpu_percent(interval=1)
        # WHILE cpu time is not 0
        while cpu_time != 0:
            # Set the cpu time again so the while can still be active
            cpu_time = psutil.cpu_percent(interval=1)
            # Creating a list
            cpu_List = list()
            # Insert each cpu percent into the list
            cpu_List.insert(0, cpu_time)
            # For x in cpu list
            for x in cpu_List:
                # Turning the cpu percent into a str
                CpuString = "Cpu usage is " + str(x) + " %"
                # Returning the CpuString
                return CpuString

    def update(self, CpuString):
        # Setting up the CpuString
        CpuString = ""

        # Emitting the Signal to the Cpu Updating function
        self.textUpdate.emit(Communicate.cpu_Updating(self, CpuString))
