from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLabel


class Label(QLabel):
    def __init__(self, text: str, *, textFormat: Qt.TextFormat = Qt.TextFormat.PlainText):
        super().__init__(text)
        self.setTextFormat(textFormat)


class RichTextLabel(Label):
    def __init__(self, text: str):
        super().__init__(text, textFormat = Qt.TextFormat.RichText)
