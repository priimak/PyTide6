from typing import override

from PySide6.QtWidgets import QMainWindow, QMenuBar


class MainWindow(QMainWindow):
    def __init__(self, *, objectName: str | None = None, windowTitle: str | None = None):
        super().__init__()
        if objectName is not None:
            self.setObjectName(objectName)

        if windowTitle is not None:
            self.setWindowTitle(windowTitle)

    @override
    def setMenuBar[T: QMenuBar](self, menubar: T) -> T:
        super().setMenuBar(menubar)
        return menubar
