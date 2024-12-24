from typing import Callable

from PySide6.QtWidgets import QPushButton, QWidget


class PushButton(QPushButton):
    def __init__(self, text: str, parent: QWidget | None = None, on_clicked: Callable[[], None] | None = None):
        super().__init__(text, parent)
        if on_clicked is not None:
            self.clicked.connect(on_clicked)
