from collections.abc import Callable
from typing import Self

from PySide6.QtCore import Qt
from PySide6.QtGui import QDoubleValidator, QKeyEvent, QValidator
from PySide6.QtWidgets import QLabel, QLineEdit, QStyle
from sprats.collections import Variable

from pytide6.layout import HBoxLayout
from pytide6.panel_widget import Panel


class LineEdit(QLineEdit):
    def __init__(
        self,
        text: str = "",
        *,
        on_text_change: Callable[[str], None] | None = None,
        min_width: int | None = None,
        max_width: int | None = None,
        validator: QValidator | None = None,
        tooltip: str | None = None,
        alignment: Qt.AlignmentFlag | None = None,
        on_key_enter: Callable[[str], None] | None = None,
        with_fixed_width_for_text: str | None = None,
        reactive_variable: Variable[str] | None = None,
    ):
        super().__init__(text)

        if on_text_change is not None:
            self.textChanged.connect(on_text_change)

        if min_width is not None:
            self.setMinimumWidth(min_width)

        if max_width is not None:
            self.setMaximumWidth(max_width)

        if validator is not None:
            self.setValidator(validator)

        if tooltip is not None:
            self.setToolTip(tooltip)

        if alignment is not None:
            self.setAlignment(alignment)

        self.__on_key_enter = on_key_enter
        if self.__on_key_enter is not None:
            self.keyPressEvent = self.__altKeyPressEvent

        if with_fixed_width_for_text is not None:
            char_width = self.fontMetrics().horizontalAdvance(with_fixed_width_for_text)
            frame_width = self.style().pixelMetric(
                QStyle.PixelMetric.PM_DefaultFrameWidth, None, self
            )
            total_width = char_width + (frame_width * 4) + 6
            self.setFixedWidth(total_width)

        if reactive_variable is not None:
            self.setText(reactive_variable.value)
            reactive_variable.register_value_change_callback(self.setText)
            self.textChanged.connect(lambda txt: reactive_variable.set_value(txt))

    def __altKeyPressEvent(self, event: QKeyEvent):
        if event.key() in [Qt.Key.Key_Return, Qt.Key.Key_Enter]:
            self.__on_key_enter(self.text())
        else:
            super().keyPressEvent(event)

    def withAlignment(self, flag: Qt.AlignmentFlag) -> Self:
        self.setAlignment(flag)
        return self

    def withOnTextChange(self, f: Callable[[str], None]) -> Self:
        self.textChanged.connect(f)
        return self

    def withMinWidth(self, min_width: int) -> Self:
        self.setMinimumWidth(min_width)
        return self

    def withMaxWidth(self, max_width: int) -> Self:
        self.setMaximumWidth(max_width)
        return self

    def withValidator(self, validator: QValidator) -> Self:
        self.setValidator(validator)
        return self

    def withToolTip(self, tooltip: str) -> Self:
        self.setToolTip(tooltip)
        return self


class LineTextInput(Panel[HBoxLayout]):
    def __init__(
        self,
        label: str | None,
        text: str = "",
        *,
        on_text_change: Callable[[str], None] | None = None,
        min_width: int | None = None,
        max_width: int | None = None,
        validator: QValidator | None = None,
        tooltip: str | None = None,
        alignment: Qt.AlignmentFlag | None = None,
        on_key_enter: Callable[[str], None] | None = None,
        with_fixed_width_for_text: str | None = None,
        reactive_variable: Variable[str] | None = None,
    ):
        super().__init__(HBoxLayout())

        if label is not None:
            self.addWidget(QLabel(label))

        self._input = self.addWidget(
            LineEdit(
                text,
                on_text_change=on_text_change,
                min_width=min_width,
                max_width=max_width,
                validator=validator,
                tooltip=tooltip,
                alignment=alignment,
                on_key_enter=on_key_enter,
                with_fixed_width_for_text=with_fixed_width_for_text,
                reactive_variable=reactive_variable,
            )
        )

    def text(self) -> str:
        return self._input.text()

    def setText(self, text: str) -> None:
        self._input.setText(text)


class FloatTextInput(LineTextInput):
    def __init__(
        self,
        label: str | None,
        text: str = "",
        *,
        on_text_change: Callable[[str], None] | None = None,
        min_width: int | None = None,
        max_width: int | None = None,
        tooltip: str | None = None,
        alignment: Qt.AlignmentFlag | None = None,
        on_key_enter: Callable[[str], None] | None = None,
        with_fixed_width_for_text: str | None = None,
        reactive_variable: Variable[str] | None = None,
    ):
        super().__init__(
            label,
            text,
            on_text_change=on_text_change,
            min_width=min_width,
            max_width=max_width,
            validator=QDoubleValidator(),
            tooltip=tooltip,
            alignment=alignment,
            on_key_enter=on_key_enter,
            with_fixed_width_for_text=with_fixed_width_for_text,
            reactive_variable=reactive_variable,
        )
