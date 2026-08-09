from collections.abc import Callable
from dataclasses import dataclass
from typing import Any

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QMenu, QWidget


@dataclass(frozen=True, slots=True)
class MenuSeparator:
    pass


class Menu(QMenu):
    Separator: MenuSeparator = MenuSeparator()

    def __init__(
        self,
        title: str | None = None,
        *,
        parent: QWidget | None = None,
        tearOffEnabled: bool | None = None,
        icon: QIcon | None = None,
        separatorsCollapsible: bool | None = None,
        toolTipsVisible: bool | None = None,
        actions: list[tuple[str, Callable[[], Any]] | MenuSeparator] | None = None,
    ):
        super().__init__(title, parent)

        if tearOffEnabled is not None:
            self.setTearOffEnabled(tearOffEnabled)

        if icon is not None:
            self.setIcon(icon)

        if separatorsCollapsible is not None:
            self.setSeparatorsCollapsible(separatorsCollapsible)

        if toolTipsVisible is not None:
            self.setToolTipsVisible(toolTipsVisible)

        if actions is not None:
            for action in actions:
                match action:
                    case MenuSeparator():
                        self.addSeparator()
                    case tuple():
                        self.addAction(action[0], action[1])
                    case _:
                        raise ValueError(f"Invalid action {action}")
