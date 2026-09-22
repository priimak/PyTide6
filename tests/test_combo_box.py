import re

import pytest
from sprats.collections import Variable

from pytide6 import ComboBox


def test_combo_box_invalid_current_selection(qtbot):
    with pytest.raises(
        ValueError, match=re.escape("Current selection \"A\" is not in a list of valid values ['1', '3', '5', '11']")
    ):
        ComboBox(items=["1", "3", "5", "11"], current_selection="A")

    with pytest.raises(ValueError, match=re.escape("Invalid current selection index")):
        ComboBox(items=["1", "3", "5", "11"], current_selection=4)

    with pytest.raises(ValueError, match=re.escape("Invalid current selection index")):
        ComboBox(items=["1", "3", "5", "11"], current_selection=-1)

    # but check that current_selection= min and max values are Ok
    assert ComboBox(items=["1", "3", "5", "11"], current_selection=0).currentText() == "1"
    assert ComboBox(items=["1", "3", "5", "11"], current_selection=3).currentText() == "11"


def test_combo_box_no_valid_items(qtbot):
    with pytest.raises(
        ValueError,
        match=re.escape("ComboBox requires either items= argument of valid values in the reactive_variable="),
    ):
        ComboBox(current_selection="A")


def test_combo_box_three_current_selection_types(qtbot):
    combo_box = ComboBox(
        items=["1", "3", "5", "11"],
        current_selection="3",  # select to text
    )
    assert combo_box.currentText() == "3"
    combo_box = ComboBox(
        items=["1", "3", "5", "11"],
        current_selection=2,  # select by index
    )
    assert combo_box.currentText() == "5"

    current_variable = Variable(11)
    combo_box = ComboBox(
        items=["1", "3", "5", "11"],
        current_selection=current_variable,  # select to text serialized from current_variable value.
    )
    assert combo_box.currentText() == "11"


def test_combo_box_with_reactive_variable(qtbot):
    variable = Variable[str]("A", clazz=str)
    combo_box = ComboBox(
        items=["1", "3", "5", "11"],
        current_selection="3",
        reactive_variable=variable,
    )
    # Since `variable` does not have an array of valid values we use items= argument and in the constructor
    # value contained in current_selection= argument will be set in the `variable`
    assert variable.str_value() == "3"
    assert combo_box.currentText() == "3"

    # Setting value not in the list of valid vales should raise an error
    with pytest.raises(
        ValueError, match=re.escape("Current selection \"Foo\" is not in a list of valid values ['1', '3', '5', '11']")
    ):
        variable.set_value("Foo")

    # let's change selection in the combo box and see it reflected in the reactive variable
    qtbot.addWidget(combo_box)
    qtbot.keyClicks(combo_box, "11")
    assert variable.str_value() == "11"
    assert combo_box.currentText() == "11"

    # valid values in reactive_variable
    variable = Variable[str]("B", valid_values=["A", "B", "C", "D"])
    combo_box = ComboBox(
        reactive_variable=variable,
    )
    assert combo_box.valid_items == ["A", "B", "C", "D"]
    assert combo_box.currentText() == "B"
    qtbot.addWidget(combo_box)
    qtbot.keyClicks(combo_box, "D")
    assert variable.str_value() == "D"
    assert combo_box.currentText() == "D"

    # invalid current value
    with pytest.raises(
        ValueError, match=re.escape("Current selection \"Foo\" is not in a list of valid values ['A', 'B', 'C', 'D']")
    ):
        ComboBox(
            current_selection="Foo",
            reactive_variable=Variable[str]("B", valid_values=["A", "B", "C", "D"]),
        )

    # items= and valid_values= must match if present
    with pytest.raises(
        ValueError, match=re.escape("Possible values set is not compatible with valid_values in the reactive_variable")
    ):
        ComboBox(
            items=["1", "2"],
            reactive_variable=Variable[str]("B", valid_values=["A", "B", "C", "D"]),
        )

    # this should be fine
    rvar = Variable[str]("B", valid_values=["A", "B", "C", "D"])
    cvar = Variable[str](None, clazz=str)
    combo_box = ComboBox(items=["A", "B", "C", "D"], reactive_variable=rvar, on_text_change=cvar.set_from_str)

    # changing selection should update both rvar.value and cvar.value
    qtbot.addWidget(combo_box)
    qtbot.keyClicks(combo_box, "C")
    assert rvar.str_value() == "C"
    assert cvar.str_value() == "C"
