from PySide6.QtWidgets import QDialog


class Dialog(QDialog):
    def __init__(self, parent, *, windowTitle: str | None = None, modal: bool = False, css: str | None = None):
        super().__init__(parent)

        if windowTitle:
            self.setWindowTitle(windowTitle)

        self.setModal(modal)

        if css is not None:
            self.setStyleSheet(css)
