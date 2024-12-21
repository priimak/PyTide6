from pathlib import Path
from typing import Protocol


class FileOpener(Protocol):
    def open_file(self, file: str | Path) -> None: ...
