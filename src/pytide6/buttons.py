from collections.abc import Callable
from typing import Any

from PySide6.QtCore import Qt
from PySide6.QtGui import QCursor, QKeyEvent, QPixmap
from PySide6.QtWidgets import QPushButton, QWidget


class PushButton(QPushButton):
    def __init__(
        self,
        text: str,
        parent: QWidget | None = None,
        *,
        on_clicked: Callable[[], Any] | None = None,
        auto_default: bool | None = None,
        style_sheet: str | None = None,
        cursor: QCursor | Qt.CursorShape | QPixmap | None = None,
        enabled: bool = True,
        tool_tip: str | None = None,
        respond_to_enter_and_return_keys: bool = True,
    ):
        super().__init__(text, parent)
        self.__respond_to_enter_and_return_keys = respond_to_enter_and_return_keys
        if on_clicked is not None:
            self.clicked.connect(on_clicked)

        if auto_default is not None:
            self.setAutoDefault(auto_default)

        if style_sheet is not None:
            self.setStyleSheet(style_sheet)

        if cursor is not None:
            self.setCursor(cursor)

        if tool_tip is not None:
            self.setToolTip(tool_tip)

        self.setEnabled(enabled)

    def keyPressEvent(self, event: QKeyEvent, /) -> None:
        super().keyPressEvent(event)
        if self.__respond_to_enter_and_return_keys and event.key() in [
            Qt.Key.Key_Enter,
            Qt.Key.Key_Return,
        ]:
            self.clicked.emit()
