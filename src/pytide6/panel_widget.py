from typing import Self, override

import PySide6
from PySide6.QtCore import QMargins, Qt
from PySide6.QtGui import QColor, QPalette, QRgba64
from PySide6.QtWidgets import QBoxLayout, QLayout, QWidget

from pytide6.layout import BoxLayoutWidget, HBoxLayout, VBoxLayout, addWidgets


class Panel[T: QLayout](QWidget):
    def __init__(
        self,
        layout: T,
        background_color: QColor | str | QRgba64 | None = None,
        name: str | None = None,
    ):
        super().__init__()
        assert layout is not None
        self.__layout = layout
        self.setLayout(layout)

        if background_color is not None:
            self.setBackgroundColor(background_color)

        if name is not None:
            self.setObjectName(name)

    def addWidget[X: QWidget](self, widget: X) -> X:
        self.layout().addWidget(widget)
        return widget

    @override
    def layout(self) -> T:
        return self.__layout

    def setBackgroundColor(self, color: QColor | str | QRgba64) -> None:
        palette = QPalette()
        palette.setColor(QPalette.ColorRole.Window, color)
        self.setAutoFillBackground(True)
        self.setPalette(palette)


class QBoxLayoutPanelRoot[T: QBoxLayout](Panel[T]):
    def addWidgets(self, *widgets: BoxLayoutWidget) -> Self:
        """
        Adds several widgets at the same time. Passed argument can be an instance of
        QWidget or a widget wrapper W(...) which allows to pass values of stretch and alignment
        """
        addWidgets(self.layout(), list(widgets))
        return self

    withWidgets = addWidgets

    def addWidget[X: QWidget](
        self, widget: X, stretch: int = 0, alignment: Qt.AlignmentFlag | None = None
    ) -> X:
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
        Adds a stretchable space with zero minimum size and stretch factor `stretch` to the end of this box layout.
        """
        self.layout().addStretch(stretch)
        return self


class VBoxPanel(QBoxLayoutPanelRoot[VBoxLayout]):
    def __init__(
        self,
        widgets: list[BoxLayoutWidget] | None = None,
        *,
        spacing: int | None = None,
        margins: QMargins | tuple[int, int, int, int] | int | None = None,
        sizeConstraint: QLayout.SizeConstraint | None = None,
        enabled: bool | None = None,
        background_color: PySide6.QtGui.QColor
        | str
        | PySide6.QtGui.QRgba64
        | None = None,
        name: str | None = None,
    ):
        super().__init__(
            VBoxLayout(
                widgets=widgets,
                spacing=spacing,
                margins=margins,
                sizeConstraint=sizeConstraint,
                enabled=enabled,
            ),
            background_color=background_color,
            name=name,
        )


class HBoxPanel(QBoxLayoutPanelRoot[HBoxLayout]):
    def __init__(
        self,
        widgets: list[BoxLayoutWidget] | None = None,
        *,
        spacing: int | None = None,
        margins: QMargins | tuple[int, int, int, int] | int | None = None,
        sizeConstraint: QLayout.SizeConstraint | None = None,
        enabled: bool | None = None,
        background_color: PySide6.QtGui.QColor
        | str
        | PySide6.QtGui.QRgba64
        | None = None,
        name: str | None = None,
    ):
        super().__init__(
            HBoxLayout(
                widgets=widgets,
                spacing=spacing,
                margins=margins,
                sizeConstraint=sizeConstraint,
                enabled=enabled,
            ),
            background_color=background_color,
            name=name,
        )
