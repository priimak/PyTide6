from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget


class W:
    def __init__(self, widget: QWidget, stretch: int = 0, alignment: Qt.AlignmentFlag = 0):
        self.widget = widget
        self.stretch = stretch
        self.alignment = alignment
