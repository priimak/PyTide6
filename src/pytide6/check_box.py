from PySide6.QtWidgets import QCheckBox


class CheckBox(QCheckBox):
    def __init__(self, text: str, parent = None, *, checked: bool = False):
        super().__init__(text, parent)
        self.setChecked(checked)
