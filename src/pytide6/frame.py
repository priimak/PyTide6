from PySide6.QtWidgets import QFrame


class HorizonalLine(QFrame):
    def __init__(
        self,
        parent=None,
        *,
        shadow: QFrame.Shadow = QFrame.Shadow.Sunken,
        lineWidth: int = 1,
    ):
        super().__init__(
            parent,
            frameShadow=shadow,
            frameShape=QFrame.Shape.HLine,
            lineWidth=lineWidth,
        )


class VerticalLine(QFrame):
    def __init__(
        self,
        parent=None,
        *,
        shadow: QFrame.Shadow = QFrame.Shadow.Sunken,
        lineWidth: int = 1,
    ):
        super().__init__(
            parent,
            frameShadow=shadow,
            frameShape=QFrame.Shape.VLine,
            lineWidth=lineWidth,
        )
