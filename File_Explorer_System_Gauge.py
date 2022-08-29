import psutil
from PySide2 import QtWidgets, QtCore
from PySide2.QtCore import Signal

class MainUiClass(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.progress = QtWidgets.QProgressBar()
        self.button = QtWidgets.QPushButton('Test')
        self.button.clicked.connect(self.handleButton)
        layout = QtWidgets.QHBoxLayout(self)
        layout.addWidget(self.progress)
        layout.addWidget(self.button)
        self.monitor = CpuMonitor()
        self.monitor.cpuPercent.connect(self.progress.setValue)
        self.monitor.start()
        self.simulator = Simulator()

    def handleButton(self):
        if not self.simulator.isRunning():
            self.simulator.start()

    def closeEvent(self, event):
        for thread in self.simulator, self.monitor:
            thread.stop()
            thread.quit()
            thread.wait()

class CpuMonitor(QtCore.QThread):
    cpuPercent = Signal(int)

    def run(self):
        self._stopped = False
        while not self._stopped:
            value = int(psutil.cpu_percent(interval=1))
            self.cpuPercent.emit(value)

    def stop(self):
        self._stopped = True

class Simulator(QtCore.QThread):
    def run(self):
        self._stopped = False
        random = QtCore.QRandomGenerator.system()
        timer1 = QtCore.QDeadlineTimer(20000)
        while not self._stopped and not timer1.hasExpired():
            duration = random.bounded(400, 800)
            self.msleep(duration)
            timer2 = QtCore.QDeadlineTimer(duration)
            while not self._stopped and not timer2.hasExpired():
                pass

    def stop(self):
        self._stopped = True

if __name__ == '__main__':

    app = QtWidgets.QApplication(['CPU Monitor'])
    a = MainUiClass()
    a.show()
    app.exec_()