from collections.abc import Callable

from PySide6.QtGui import QFocusEvent
from PySide6.QtWidgets import QComboBox
from sprats.collections import Variable


class ComboBox[T](QComboBox):
    def __init__(
        self,
        parent=None,
        *,
        min_width: int | None = None,
        items: list[str] | None = None,
        current_selection: int | str | Variable[T] | None = None,
        on_text_change: Callable[[str], None] | None = None,
        on_focus: Callable[[QFocusEvent], None] = lambda _: None,
        reactive_variable: Variable[T] | None = None,
    ) -> None:
        super().__init__(parent)

        if min_width is not None:
            self.setMinimumWidth(min_width)

        if items is not None:
            self.addItems(items)

        match current_selection:
            case str():
                self.setCurrentText(current_selection)
            case int():
                self.setCurrentIndex(current_selection)
            case Variable():
                self.setCurrentText(f"{current_selection.value}")

        if reactive_variable is not None:
            reactive_variable.register_value_change_callback(
                lambda v: self.setCurrentText(reactive_variable.serializer(v))
            )
            if items is None and reactive_variable.valid_values is not None:
                # below calling reactive_variable.valid_values_str() will always return non-null list
                # noinspection bad-argument-type
                self.addItems(reactive_variable.valid_values_str())
            if current_selection is None:
                self.setCurrentText(reactive_variable.serializer(reactive_variable.value))
            self.currentTextChanged.connect(reactive_variable.set_from_str)

        self.on_focus = on_focus

        if on_text_change is not None:
            self.currentTextChanged.connect(on_text_change)

    def focusInEvent(self, e):
        super().focusInEvent(e)
        self.on_focus(e)
