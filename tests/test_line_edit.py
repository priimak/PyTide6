from PySide6.QtCore import Qt
from pytestqt.qtbot import QtBot
from sprats.collections import Variable

from pytide6.inputs import LineEdit


def test_combo_line_edit(qtbot: QtBot):
    cvar = Variable[str](None, clazz=str)
    line_edit = LineEdit("doo", on_text_change=cvar.set_from_str)
    assert line_edit.text() == "doo"
    assert cvar.value is None
    qtbot.keyPress(line_edit, Qt.Key.Key_M)
    assert line_edit.text() == "doom"
    assert cvar.value == "doom"

    cvar = Variable[str](None, clazz=str)
    rvar = Variable[str]("zoo", clazz=str)
    line_edit = LineEdit("foo", on_text_change=cvar.set_from_str, reactive_variable=rvar)
    assert line_edit.text() == "zoo"
    assert cvar.value is None
    qtbot.keyPress(line_edit, Qt.Key.Key_M)
    assert line_edit.text() == "zoom"
    assert cvar.value == "zoom"
