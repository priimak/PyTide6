from collections.abc import Callable

from PySide6.QtGui import QFocusEvent
from PySide6.QtWidgets import QComboBox


class ComboBox(QComboBox):
    def __init__(self,
                 parent=None,
                 *,
                 min_width: int | None = None,
                 items: list[str] | None = None,
                 current_selection: int | str | None = None,
                 on_text_change: Callable[[str], None] | None = None,
                 on_focus: Callable[[QFocusEvent], None] = lambda _: None) -> None:
        super(ComboBox, self).__init__(parent)

        if min_width is not None:
            self.setMinimumWidth(min_width)

        if items is not None:
            self.addItems(items)

        match current_selection:
            case str():
                self.setCurrentText(current_selection)
            case int():
                self.setCurrentIndex(current_selection)

        self.on_focus = on_focus

        if on_text_change is not None:
            self.currentTextChanged.connect(on_text_change)

    def focusInEvent(self, e):
        super().focusInEvent(e)
        self.on_focus(e)
