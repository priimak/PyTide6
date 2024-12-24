from typing import Type, override

from PySide6.QtCore import QMargins, Qt
from PySide6.QtWidgets import QLayout, QWidget, QSpacerItem

from pytide6.layout import VBoxLayout, HBoxLayout


class Panel[T: QLayout](QWidget):
    def __init__(self, layout: T, widgets: list[QWidget | Type[QSpacerItem]] | None = None):
        super().__init__()
        self.setLayout(layout)

        if widgets is not None:
            for w in widgets:
                if w is QSpacerItem:
                    layout.addStretch(1)
                else:
                    layout.addWidget(w)

    @override
    def layout(self) -> T:
        return super().layout()


class VBoxPanel(Panel[VBoxLayout]):
    def __init__(
            self,
            widgets: list[QWidget | tuple[QWidget, int] | tuple[QWidget, Qt.AlignmentFlag] |
                          tuple[QWidget, int, Qt.AlignmentFlag] | Type[QSpacerItem]] | None = None,
            *,
            spacing: int | None = None,
            margins: QMargins | tuple[int, int, int, int] | int | None = None,
            sizeConstraint: QLayout.SizeConstraint | None = None,
            enabled: bool | None = None, ):
        super().__init__(VBoxLayout(
            widgets = widgets, spacing = spacing, margins = margins, sizeConstraint = sizeConstraint, enabled = enabled
        ))


class HBoxPanel(Panel[HBoxLayout]):
    def __init__(
            self,
            widgets: list[QWidget | tuple[QWidget, int] | tuple[QWidget, Qt.AlignmentFlag] |
                          tuple[QWidget, int, Qt.AlignmentFlag] | Type[QSpacerItem]] | None = None,
            *,
            spacing: int | None = None,
            margins: QMargins | tuple[int, int, int, int] | int | None = None,
            sizeConstraint: QLayout.SizeConstraint | None = None,
            enabled: bool | None = None, ):
        super().__init__(HBoxLayout(
            widgets = widgets, spacing = spacing, margins = margins, sizeConstraint = sizeConstraint, enabled = enabled
        ))
