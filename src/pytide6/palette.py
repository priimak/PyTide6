from typing import Any

import PySide6
from PySide6.QtGui import QPalette


class Palette(QPalette):
    def __init__(
            self,
            cr: PySide6.QtGui.QPalette.ColorRole | None = None,
            color: Any | None = None
    ):
        super().__init__()
        if cr is not None and color is not None:
            self.setColor(cr, color)
           