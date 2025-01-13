from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget


class W:
    __match_args__ = ("widget", "stretch", "alignment")

    def __init__(self, widget: QWidget, stretch: int = 0, alignment: Qt.AlignmentFlag | None = None):
        self.widget = widget
        self.stretch = stretch
        self.alignment = alignment
