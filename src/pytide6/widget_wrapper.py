from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget


class W:
    __match_args__ = ("widget", "stretch", "alignment")

    def __init__(
        self,
        widget: QWidget | None = None,
        stretch: int = 0,
        alignment: Qt.AlignmentFlag | None = None,
    ):
        self.widget = QWidget() if widget is None else widget
        self.stretch = stretch
        self.alignment = alignment
