from PySide6.QtCore import QByteArray
from PySide6.QtWidgets import QWidget
from sprats.config.app_state import AppState


def set_geometry(
        app_state: AppState,
        widget: QWidget,
        screen_dim: tuple[int, int],
        win_size_fraction: float = 0.6,
        name: str | None = None
) -> None:
    """
    Sets geometry on widget by loading it from application state or setting it to the fraction of the screen
    dimensions at the center of the screen.

    :param widget: widget on which geometry will be set
    :param app_state: application state where geometry will be loaded from
    :param screen_dim: width x height in pixels on the screen
    :param win_size_fraction: fraction of the main screen which will be used for default geometry
    :param name: name under which geometry will be loaded; if None then widget.objectName() is used to load geometry
    """
    # Try loading geometry from saved app state
    loaded_geometry: QByteArray | None = app_state.get_geometry(
        widget.objectName() if name is None else name
    )
    if loaded_geometry is None:
        # Init main window size to be a fraction of the screen size
        widget.setGeometry(
            int(screen_dim[0] * (1 - win_size_fraction) / 2),
            int(screen_dim[1] * (1 - win_size_fraction) / 2),
            int(screen_dim[0] * win_size_fraction),
            int(screen_dim[1] * win_size_fraction)
        )
    else:
        widget.restoreGeometry(loaded_geometry)
