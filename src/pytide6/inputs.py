from PySide6.QtWidgets import QLabel, QLineEdit

from pytide6 import Panel, HBoxLayout


class LineTextInput(Panel[HBoxLayout]):
    def __init__(self, label: str, text: str = ""):
        super().__init__(HBoxLayout())

        self.addWidget(QLabel(label))

        self._input = QLineEdit(text)
        self.addWidget(self._input)

    def text(self) -> str:
        return self._input.text()
