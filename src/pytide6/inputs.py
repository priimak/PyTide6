from PySide6.QtWidgets import QLabel, QLineEdit

from pytide6.layout import HBoxLayout
from pytide6.panel_widget import Panel


class LineTextInput(Panel[HBoxLayout]):
    def __init__(self, label: str | None, text: str = ""):
        super().__init__(HBoxLayout())

        if label is not None:
            self.addWidget(QLabel(label))

        self._input = QLineEdit(text)
        self.addWidget(self._input)

    def text(self) -> str:
        return self._input.text()
