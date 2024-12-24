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

        self.addWidget = layout.addWidget

    def addWidget(self, widget: QWidget) -> "Panel":
        self.layout().addWidget(widget)
        return self

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

        self.addStretch = self.layout().addStretch

    def addWidget(
            self,
            widget: QWidget,
            stretch: int = 0,
            alignment: Qt.AlignmentFlag = Qt.Alignment()
    ) -> "VBoxPanel":
        self.layout().addWidget(widget, stretch, alignment)
        return self

    def addStretch(self, stretch: int = 0) -> "VBoxPanel":
        self.layout().addStretch(stretch)
        return self


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

    def addWidget(
            self,
            widget: QWidget,
            stretch: int = 0,
            alignment: Qt.AlignmentFlag = Qt.Alignment()
    ) -> "HBoxPanel":
        self.layout().addWidget(widget, stretch, alignment)
        return self

    def addStretch(self, stretch: int = 0) -> "HBoxPanel":
        self.layout().addStretch(stretch)
        return self
