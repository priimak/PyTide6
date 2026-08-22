from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLabel


class Label(QLabel):
    def __init__(self, text: str, *, textFormat: Qt.TextFormat = Qt.TextFormat.PlainText, css: str | None = None):
        super().__init__(text)
        self.setTextFormat(textFormat)
        if css is not None:
            self.setStyleSheet(css)


class RichTextLabel(Label):
    def __init__(self, text: str, css: str | None = None):
        super().__init__(text, textFormat=Qt.TextFormat.RichText, css=css)
