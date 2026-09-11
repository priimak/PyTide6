from typing import Self

from PySide6.QtWidgets import QDialog


class Dialog(QDialog):
    def __init__(self, parent, *, windowTitle: str | None = None, modal: bool = False, css: str | None = None):
        super().__init__(parent)

        if windowTitle:
            self.setWindowTitle(windowTitle)

        self.setModal(modal)

        if css is not None:
            self.setStyleSheet(css)

    def execute(self) -> Self:
        self.exec()
        return self


class Prompt[T](Dialog):
    def __init__(
        self,
        parent,
        *,
        windowTitle: str | None = None,
        modal: bool = True,
        css: str | None = None,
        default_value: T | None = None,
    ):
        super().__init__(parent, windowTitle=windowTitle, modal=modal, css=css)

        self.retval: T | None = default_value

    def prompt(self) -> T | None:
        return self.execute().retval
