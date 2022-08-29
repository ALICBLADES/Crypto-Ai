import time
import threading
import psutil
import traceback
import functools

from PySide2.QtQml import QQmlApplicationEngine

import File_Explorer_System_Gauge as FESG
import multiprocessing
import sys

from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import Slot, Signal, QThread, QObject, QRunnable, QProcess, QThreadPool, QTimer


class WorkerSignals(QObject):
    '''
    Defines the signals available from a running worker thread.

    Supported signals are:

    finished
        No data

    error
        tuple (exctype, value, traceback.format_exc() )

    result
        object data returned from processing, anything

    progress
        int indicating % progress

    '''
    finished = Signal()
    error = Signal(tuple)
    result = Signal(object)
    progress = Signal(int)
    Returned = Signal(str)


class Worker(QRunnable):
    """
    Worker thread

    Inherits from QRunnable to handle worker thread setup, signals and wrap-up
    :param callback: The function callback to run on this worker thread. Supplied args
    and kwargs will be passed through to the runner.

    :type callback: function
    :param args: Arguments to pass to the callback function
    :param kwargs: Keywords to pass to the callback function
    """

    def __init__(self, fn, *args, **kwargs):
        super(Worker, self).__init__()

        self.fn = fn
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()

        # Add the callback to our kwargs
        self.kwargs["progress_callback"] = self.signals.progress

    @Slot()
    def run(self):
        '''
        Initialize the runner function with passed args, kwargs.
        '''
        try:
            result = self.fn(*self.args, **self.kwargs)
        except:
            traceback.print_exc()
            exctype, value = sys.exc_info()[:2]
            self.signals.error.emit((exctype, value, traceback.format_exc()))
        else:
            self.signals.result.emit(result)
        finally:
            self.signals.finished.emit()


class AnotherOne(QThread):
    def __init__(self, *args, **kwargs):
        super(AnotherOne, self).__init__()
        self.signal = fuck()

    def run(self):

        while True:
            self.signal.goddamn.emit(self.progress())
            self.signal.fucks.emit(self.cpu_Updating())



    @Slot(object)
    def progress(self):
        cpu_object = self.cpu_Updating()
        while True:

            self.label = QLabel()

            self.label.setText(cpu_object + "l")

            print(self.label.text())

            return self.label

    @Slot(str)
    def cpu_Updating(self):

        global cpu_time

        while True:
            cpu_time = psutil.cpu_percent(interval=1)

            to_String = "Cpu Usage is " + str(cpu_time) + " %"

            return to_String

class Layout_thread(QThread):
    def __init__(self):
        super(Layout_thread, self).__init__()
        self.signal = fuck()

    def run(self):
        while True:
            self.signal.goddamn.emit(self.window.adding_Percents())



"""
This class will create what things will go into the app window
"""


class Window(QMainWindow, AnotherOne, Layout_thread):
    Sim_layout = None
    # The method attaches the QMainWindow to the Window class
    def __init__(self):
        super(Window, self).__init__()

        bitch = Signal(object)

        # Setting the window title
        self.setWindowTitle("Andel Trading Bot")
        # Setting the geometry of the window
        self.setGeometry(750, 750, 750, 750)

        # Initialing the QWidget
        fileWidget = QWidget()

        # Adding the fileReading function to the file Widget
        fileWidget.setLayout(self.FileReading())

        self.setCentralWidget(fileWidget)

        self.threadpool = QThreadPool()

        # Creating the portfolio label
        portfolio = QLabel("Portfolio Information")

        # Setting the font and the size of the text of the portfolio text
        portfolio.setFont(QFont("Arial", 10))

        # Creating the net total label
        graph_data = QLabel("Net Total:\nLoss:\nGains:\nPercentage")

        # Creating the button
        button = QPushButton()

        # Setting the button's text
        button.setText("Click me")

        # Setting the size of the button
        button.setFixedSize(50, 50)

        self.checkbox = QCheckBox()

        self.checkbox.connect(self.adding_Percents(), QFormLayout)

        self.Sim_layout.addWidget(self.checkbox)

        self.Sim_layout.addWidget(button)

        self.cpu_thread = AnotherOne()

        self.cpu_thread.start()

        self.psutil_thread()

        self.Checking()

        # Showing the GUI window
        self.show()


    def Checking(self):
        if self.checkbox.isChecked():
           self.checkbox.connect(self.adding_Percents(), QFormLayout)
        self.upate_timer = QTimer(self)
        self.upate_timer.setInterval(100)  # milliseconds i believe
        self.upate_timer.setSingleShot(False)
        self.upate_timer.timeout.connect(self.adding_Percents())

    @Slot(object)
    def adding_Percents(self):
        self.Sim_layout = QFormLayout(self)

        self.Sim_frame = QFrame(self)

        while True:
            if self.Sim_layout.isEmpty():
               self.Sim_layout.addWidget(AnotherOne.progress(self))
               self.Sim_frame.setLayout(self.Sim_layout)
               return self.setCentralWidget(self.Sim_frame)
            elif self.Sim_layout.isEmpty() == False:
               self.Sim_layout.removeWidget(AnotherOne.progress(self))
               self.Sim_frame.setLayout(self.Sim_layout)
               return self.setCentralWidget(self.Sim_frame)

    def Label_Return(self):
        self.cpu_label = QLabel()
        return self.cpu_label.setText(AnotherOne.cpu_Updating(self))

        # CREATE PSUTIL THREAD FUNCTION
    def psutil_thread(self):
            worker = Worker(self.adding_Percents)

            # START WORKER
            worker.signals.result.connect(self.print_output)
            worker.signals.finished.connect(self.thread_complete)
            worker.signals.progress.connect(self.progress)

            # Execute
            self.threadpool.start(worker)

    """
    This function will exit the file menu in the GUI
    """

    def exitProgram(self):
        exit()

    def doing(self):
        cpu_object = AnotherOne.cpu_Updating(self)
        cpu_threading = multiprocessing.Process(target=self.adding_Percents())
        cpu_threading.start()

    def execute_this_fn(self, progress_callback):
        for n in range(0, 5):
            time.sleep(1)
            progress_callback.emit(n * 100 / 4)

        return "Done."

    def print_output(self, s):
        print(s)

    def thread_complete(self):
        print("THREAD COMPLETE!")


    def Locking_Threading(self):
        lock = threading.Lock()
        lock.acquire()
        cpu_threading = threading.Thread(target=AnotherOne.cpu_Updating(self))
        cpu_threading.start()


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

class FrameTab(QFrame):
    def __init__(self, cpu_number):
        super(FrameTab, self).__init__()

        self.call = Window.CallingFrame(self)

        self.tabs = QTabWidget()

        self.tabs.setParent(FrameTab())

        self.tabs.addTab(self.CallFrame(), "First Tab")


class fuck(QObject):
    fucks = Signal(str)
    goddamn = Signal(object)
    damn = Signal(object)
    def __init__(self):
       super().__init__(None)
       self.thread = QThread()
       self.moveToThread(self.thread)



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

        # Adding the check label to the layout
        self.layout.addWidget(self.checkLabel)

        # Add the checkbox to the layout
        self.layout.addWidget(self.checkBox)

        # Add the layout to the function, which adds it to the setting tab
        self.setLayout(self.layout)


app = QApplication([])

window = Window()

window.show()

app.exec_()
