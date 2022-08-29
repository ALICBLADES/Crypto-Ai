import os
import sys
import time
from pathlib import Path

from PySide2.QtGui import QGuiApplication
from PySide2.QtQml import QQmlApplicationEngine
from PySide2.QtCore import QObject, Slot, Signal, QTimer, QUrl, QThread


class Backend(QObject):
    progress_changed = Signal(float, name="progressChanged")

    def __init__(self, parent=None):
        super().__init__(parent)

        self.worker = Worker()
        self.worker.progress_changed.connect(self.progress_changed)
        self.worker_thread = QThread()
        self.worker.moveToThread(self.worker_thread)
        self.worker_thread.start()

    @Slot()
    def start_worker(self):
        QTimer.singleShot(0, self.worker.run)


class Worker(QObject):
    progress_changed = Signal(float)

    @Slot()
    def run(self):
        self.progress = 0
        self.total = 100
        for i in range(0, self.total):
            self.update_progress()

    def update_progress(self):
        print(f"{self.progress} / {self.total}")
        self.progress += 1
        self.progress_changed.emit(self.progress)
        time.sleep(1)


if __name__ == "__main__":
    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()

    backend = Backend()
    engine.rootContext().setContextProperty("backend", backend)

    engine.load(os.fspath(Path(__file__).resolve().parent / "main.qml"))
    if not engine.rootObjects():
        sys.exit(-1)
    ret = app.exec_()
    # backend.worker_thread.quit()
    # backend.worker_thread.wait()
    sys.exit(ret)