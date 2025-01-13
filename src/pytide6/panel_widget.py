from typing import Type, override, Self

from PySide6.QtCore import QMargins, Qt
from PySide6.QtWidgets import QLayout, QWidget, QSpacerItem, QBoxLayout

from pytide6.layout import VBoxLayout, HBoxLayout, addWidgets
from pytide6.widget_wrapper import W


class Panel[T: QLayout](QWidget):
    def __init__(self, layout: T, widgets: list[QWidget | W | Type[QSpacerItem]] | None = None):
        super().__init__()
        self.setLayout(layout)

        if widgets is not None:
            for w in widgets:
                if w is QSpacerItem:
                    layout.addStretch(1)
                else:
                    layout.addWidget(w)

    def addWidget(self, widget: QWidget) -> "Panel":
        self.layout().addWidget(widget)
        return self

    @override
    def layout(self) -> T:
        return super().layout()


class QBoxLayoutPanelRoot[T: QBoxLayout](Panel[T]):
    def addWidgets(self, *widgets: QWidget | W | Type[QSpacerItem]) -> Self:
        """
        Adds several widgets at the same time. Passed argument can be an instance of
        QWidget or a widget wrapper W(...) which allows to pass values of stretch and alignment
        """
        addWidgets(self.layout(), list(widgets))
        return self

    withWidgets = addWidgets

    def addWidget[T: QWidget](
            self,
            widget: T,
            stretch: int = 0,
            alignment: Qt.AlignmentFlag | None = None
    ) -> T:
        """
        Adds widget to the end of this box layout, with a stretch factor of `stretch` and alignment `alignment`.
        The stretch factor applies only in the direction of the `QBoxLayout`, and is relative to the other boxes
        and widgets in this QBoxLayout . Widgets and boxes with higher stretch factors grow more.

        If the stretch factor is 0 and nothing else in the `QBoxLayout` has a stretch factor greater than zero,
        the space is distributed according to the `QWidget::sizePolicy()` of each widget that’s involved.

        The alignment is specified by alignment. The default alignment is 0, which means that the widget
        fills the entire cell.
        """
        if alignment is None:
            self.layout().addWidget(widget, stretch)
        else:
            self.layout().addWidget(widget, stretch, alignment)
        return widget

    def addStretch(self, stretch: int = 0) -> Self:
        """
        Adds a stretchable space (a QSpacerItem ) with zero minimum size and stretch
        factor `stretch` to the end of this box layout.
        """
        self.layout().addStretch(stretch)
        return self


class VBoxPanel(QBoxLayoutPanelRoot[VBoxLayout]):
    def __init__(
            self,
            widgets: list[QWidget | W | Type[QSpacerItem]] | None = None,
            *,
            spacing: int | None = None,
            margins: QMargins | tuple[int, int, int, int] | int | None = None,
            sizeConstraint: QLayout.SizeConstraint | None = None,
            enabled: bool | None = None, ):
        super().__init__(VBoxLayout(
            widgets = widgets, spacing = spacing, margins = margins, sizeConstraint = sizeConstraint, enabled = enabled
        ))


class HBoxPanel(QBoxLayoutPanelRoot[HBoxLayout]):
    def __init__(
            self,
            widgets: list[QWidget | W | Type[QSpacerItem]] | None = None,
            *,
            spacing: int | None = None,
            margins: QMargins | tuple[int, int, int, int] | int | None = None,
            sizeConstraint: QLayout.SizeConstraint | None = None,
            enabled: bool | None = None, ):
        super().__init__(HBoxLayout(
            widgets = widgets, spacing = spacing, margins = margins, sizeConstraint = sizeConstraint, enabled = enabled
        ))
