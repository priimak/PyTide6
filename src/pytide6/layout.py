from typing import Type

from PySide6.QtCore import QMargins
from PySide6.QtWidgets import QLayout, QWidget


def asList[T](src: list[T] | None) -> list[T]:
    return [] if src is None else src


def Layout[T: QLayout](
        layout_class: Type[T],
        widgets: list[QWidget] | None = None,
        *,
        spacing: int | None = None,
        margins: QMargins | tuple[int, int, int, int] | int | None = None,
        sizeConstraint: QLayout.SizeConstraint | None = None,
        enabled: bool | None = None,
) -> T:
    """
    :param layout_class: Layout class to instantiate
    :param widgets: List of widgets to be added by calling `::addWidget(...)` to this layout
    :param spacing: This property holds the spacing between widgets inside the layout. If no value is
            explicitly set, the layout’s spacing is inherited from the parent layout, or from the style
            settings for the parent widget. For `QGridLayout` and `QFormLayout`, it is possible to set different
            horizontal and vertical spacings using `setHorizontalSpacing()` and `setVerticalSpacing()`. In that
            case, `spacing()` returns -1.
    :param margins: Sets the margins to use around the layout. By default, `QLayout` uses the values provided
            by the style. On most platforms, the margin is 11 pixels in all directions. If passed argument is
            an int then it corresponds to `QMargins` on all sides with this value.
    :param sizeConstraint: Resize mode of the layout
    :param enabled: Enables this layout if enable is true, otherwise disables it. An enabled layout
            adjusts dynamically to changes; a disabled layout acts as if it did not exist. By default,
            all layouts are enabled.
    :return:
    """
    layout = layout_class()

    if spacing is not None:
        layout.setSpacing(spacing)

    if margins is not None:
        if isinstance(margins, tuple):
            layout.setContentsMargins(QMargins(margins[0], margins[1], margins[2], margins[3]))
        elif isinstance(margins, int):
            layout.setContentsMargins(QMargins(margins, margins, margins, margins))
        else:
            layout.setContentsMargins(margins)

    if sizeConstraint is not None:
        layout.setSizeConstraint(sizeConstraint)

    if enabled is not None:
        layout.setEnabled(enabled)

    for widget in asList(widgets):
        layout.addWidget(widget)

    return layout
