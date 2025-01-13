from typing import Callable, Any

import PySide6
from PySide6.QtWidgets import QPushButton, QWidget


class PushButton(QPushButton):
    def __init__(self,
                 text: str,
                 parent: QWidget | None = None,
                 *,
                 on_clicked: Callable[[], Any] | None = None,
                 auto_default: bool | None = None,
                 style_sheet: str | None = None,
                 cursor: PySide6.QtGui.QCursor | PySide6.QtCore.Qt.CursorShape | PySide6.QtGui.QPixmap | None = None,
                 enabled: bool = True):
        super().__init__(text, parent)
        if on_clicked is not None:
            self.clicked.connect(on_clicked)

        if auto_default is not None:
            self.setAutoDefault(auto_default)

        if style_sheet is not None:
            self.setStyleSheet(style_sheet)

        if cursor is not None:
            self.setCursor(cursor)

        self.setEnabled(enabled)
