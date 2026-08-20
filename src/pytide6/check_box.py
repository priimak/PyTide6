from collections.abc import Callable

from PySide6.QtWidgets import QCheckBox
from sprats.collections import Variable


class CheckBox(QCheckBox):
    def __init__(
        self,
        text: str | None = None,
        parent=None,
        *,
        checked: bool = False,
        on_change: Callable[[bool], None] = lambda _: None,
        enabled: bool = True,
        reactive_variable: Variable[bool] | None = None,
    ):
        super().__init__("" if text is None else text, parent)
        self.__on_change = on_change
        self.setChecked(checked)
        self.setEnabled(enabled)

        self.toggled.connect(on_change)

        if reactive_variable is not None:
            self.setChecked(reactive_variable.value)
            reactive_variable.register_value_change_callback(self.setChecked)
            self.toggled.connect(reactive_variable.set_value)
