from pathlib import Path

from PySide6.QtWidgets import QMenu
from sprats.config.app_persist import AppPersistence

from pytide6.open_file_protocol import FileOpener


def init_last_opened_menu(
        app_persistence: AppPersistence,
        recently_opened_menu: QMenu,
        file_opener: FileOpener
) -> None:
    recently_opened_menu.clear()
    for file in app_persistence.state.get_value("last_opened_files", []):
        def f(file_name: str):
            return lambda: file_opener.open_file(f"{file_name}")

        recently_opened_menu.addAction(file, f(file))


def update_last_opened_files_menu(
        app_persistence: AppPersistence,
        recently_opened_menu: QMenu,
        file_name: str,
        file_opener: FileOpener
) -> None:
    last_opened_files = app_persistence.state.get_value("last_opened_files", [])
    fname = f"{Path(file_name).absolute()}"

    # remove previously seen file as it will be placed at the top of this list
    last_opened_files = [f for f in last_opened_files if f != fname]

    # place it at the top
    last_opened_files.insert(0, fname)

    max_num_of_recorded_last_opened_files = app_persistence.config.get_value("max_last_opened_files", int)
    if len(last_opened_files) > max_num_of_recorded_last_opened_files:
        last_opened_files = last_opened_files[0:max_num_of_recorded_last_opened_files]
    app_persistence.state.set_value("last_opened_files", last_opened_files)

    # update sub-menu "Prev Opened"
    init_last_opened_menu(app_persistence, recently_opened_menu, file_opener)
