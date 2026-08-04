from collections.abc import Callable

from PySide6.QtWidgets import QCheckBox


class CheckBox(QCheckBox):
    def __init__(self,
                 text: str | None = None,
                 parent=None,
                 *,
                 checked: bool = False,
                 on_change: Callable[[bool], None] = lambda _: None,
                 enabled: bool = True):
        super().__init__("" if text is None else text, parent)
        self.__on_change = on_change
        self.setChecked(checked)
        self.setEnabled(enabled)

        self.toggled.connect(on_change)
