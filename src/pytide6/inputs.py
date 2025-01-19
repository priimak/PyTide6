from collections.abc import Callable

from PySide6.QtWidgets import QLabel, QLineEdit

from pytide6.layout import HBoxLayout
from pytide6.panel_widget import Panel


class LineTextInput(Panel[HBoxLayout]):
    def __init__(self, label: str | None, text: str = "", on_text_change: Callable[[str], None] | None = None):
        super().__init__(HBoxLayout())

        if label is not None:
            self.addWidget(QLabel(label))

        self._input = QLineEdit(text)

        if on_text_change is not None:
            self._input.textChanged.connect(on_text_change)

        self.addWidget(self._input)

    def text(self) -> str:
        return self._input.text()
