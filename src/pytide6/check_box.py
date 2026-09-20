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
        css: str | None = None,
    ):
        super().__init__("" if text is None else text, parent)
        self.__on_change = on_change
        self.setChecked(checked)
        self.setEnabled(enabled)

        self.toggle_callbacks: list[Callable[[bool], None]] = [on_change]

        def handle_toggle(checked: bool):
            for callback in self.toggle_callbacks:
                callback(checked)

        self.toggled.connect(handle_toggle)

        if reactive_variable is not None:
            self.setChecked(reactive_variable.value)
            reactive_variable.register_value_change_callback(self.setChecked)
            self.toggle_callbacks.append(reactive_variable.set_value)

        if css is not None:
            self.setStyleSheet(css)
