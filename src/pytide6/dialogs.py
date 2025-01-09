from PySide6.QtWidgets import QDialog


class Dialog(QDialog):
    def __init__(self, parent, *, windowTitle: str | None = None, modal: bool = False):
        super().__init__(parent)

        if windowTitle:
            self.setWindowTitle(windowTitle)

        self.setModal(modal)
