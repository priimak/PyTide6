from PySide6.QtCore import Qt
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

        if widgets is not None:
            for widget in widgets:
                self.addWidget(widget)
