from PySide6.QtCore import QMargins, Qt
from PySide6.QtWidgets import QSplitter, QWidget


class Splitter(QSplitter):
    def __init__(
        self,
        orientation: Qt.Orientation,
        *,
        parent: QWidget | None = None,
        opaqueResize: bool | None = None,
        handleWidth: int | None = None,
        childrenCollapsible: bool | None = None,
        widgets: list[QWidget] | None = None,
        margins: QMargins | tuple[int, int, int, int] | int | None = None,
    ):
        super().__init__(
            orientation,
            parent=parent,
        )

        if opaqueResize is not None:
            self.setOpaqueResize(opaqueResize)

        if handleWidth is not None:
            self.setHandleWidth(handleWidth)

        if childrenCollapsible is not None:
            self.setChildrenCollapsible(childrenCollapsible)

        if margins is not None:
            if isinstance(margins, tuple):
                self.setContentsMargins(
                    QMargins(margins[0], margins[1], margins[2], margins[3])
                )
            elif isinstance(margins, int):
                self.setContentsMargins(QMargins(margins, margins, margins, margins))
            else:
                self.setContentsMargins(margins)

        if widgets is not None:
            for widget in widgets:
                self.addWidget(widget)
