from collections.abc import Callable

from PySide6.QtWidgets import QCheckBox


class CheckBox(QCheckBox):
    def __init__(self,
                 text: str,
                 parent = None,
                 *,
                 checked: bool = False,
                 on_change: Callable[[bool], None] = lambda _: None):
        super().__init__(text, parent)
        self.__on_change = on_change
        self.setChecked(checked)

        self.clicked.connect(self._dispatch)

    def _dispatch(self):
        self.__on_change(self.isChecked())
