from collections.abc import Callable

from PySide6.QtGui import QDoubleValidator
from PySide6.QtWidgets import QLabel, QLineEdit

from pytide6.layout import HBoxLayout
from pytide6.panel_widget import Panel


class LineTextInput(Panel[HBoxLayout]):
    def __init__(self,
                 label: str | None,
                 text: str = "",
                 *,
                 on_text_change: Callable[[str], None] | None = None,
                 min_width: int | None = None):
        super().__init__(HBoxLayout())

        if label is not None:
            self.addWidget(QLabel(label))

        self._input = QLineEdit(text)

        if on_text_change is not None:
            self._input.textChanged.connect(on_text_change)

        if min_width is not None:
            self._input.setMinimumWidth(min_width)

        self.addWidget(self._input)

    def text(self) -> str:
        return self._input.text()

    def setText(self, text: str) -> None:
        self._input.setText(text)


class FloatTextInput(LineTextInput):
    def __init__(self, label: str | None, text: str = "", on_text_change: Callable[[str], None] | None = None):
        super().__init__(label, text, on_text_change)

        self._input.setValidator(QDoubleValidator())


class LineEdit(QLineEdit):
    def __init__(self, text: str = "", on_text_change: Callable[[str], None] | None = None):
        super().__init__(text)

        if on_text_change is not None:
            self.textChanged.connect(on_text_change)
