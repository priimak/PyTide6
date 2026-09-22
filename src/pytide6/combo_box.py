from collections.abc import Callable
from typing import override

from PySide6.QtGui import QFocusEvent
from PySide6.QtWidgets import QComboBox
from sprats.collections import Variable


class ComboBox[T](QComboBox):
    def __init__(
        self,
        parent=None,
        *,
        min_width: int | None = None,
        items: list[str] | None = None,
        current_selection: int | str | Variable[T] | None = None,
        on_text_change: Callable[[str], None] = lambda _: None,
        on_focus: Callable[[QFocusEvent], None] = lambda _: None,
        reactive_variable: Variable[T] | None = None,
    ) -> None:
        """
        Extension of QComboBox. Examples of usage:

        .. code-block:: python

            ComboBox(items = ["A", "B", "C", "D"], current_selection = "B")

        .. code-block:: python

            variable = Variable("B", valid_values = ["A", "B", "C", "D"])
            ComboBox(reactive_variable = variable)

        .. code-block:: python

            variable = Variable(7, valid_values = list(range(10)))
            ComboBox(reactive_variable = variable)

        :param parent:
        :param min_width: value to be set to `QComboBox::setMinimumWidth(...)`
        :param items: list of items available for selection in QComboBox. This field is optional
            if reactive_variable with valid_values list is provided. If `items` and `reactive_variable` are both
            provided and reactive_variable has valid_values list, then they (`items` and
            `reactive_variable.valid_values_str()`) must match exactly or ValueError will be raised.
        :param current_selection: Item to be shown initially selected. If integer, then that refers to the
            index (starting from 0) withing list of items. If it is string, then that refers to the actual text
            to be selected. If it is an instance of `Variable`, then `current_selection.str_value()` is used to
            select text item. If current_selection does not exist (either by index or by text value) in the list of
            items, then ValueError is raised. If `reactive_variable` is also given then, value of `current_selection`
            will be used for initially selected item and if that value is different from value in `reactive_variable`,
            then value in `reactive_variable` will set immediately when this constructor is called.
        :param on_text_change: callback function called when selection is changed.
        :param on_focus: function called when this widget receives focus after passing focus event to the
            parent (QComboBox) class.
        :param reactive_variable: linked reactive variable. If given, then current selection will be picked from
            initial value of the contained variable unless `current_selection` argument is also passed (see
            documentation above). If `reactive_variable` contains list of valid values, then that will be used in
            instead `items` argument. See above wrt conflict between `reactive_variable.valid_values_str()` and `items`
            argument. Value contained within `reactive_variable` will be automatically serialized and de-serialized
            to and from strings before used inside ComboBox. Changes to the selected_items will automatically propagate
            into the linked `reactive_variable`.
        """
        super().__init__(parent)

        self.change_callbacks: list[Callable[[str], None]] = [on_text_change]

        if min_width is not None:
            self.setMinimumWidth(min_width)

        valid_items = (
            items if (items is not None or reactive_variable is None) else reactive_variable.valid_values_str()
        )

        if valid_items is None:
            raise ValueError("ComboBox requires either items= argument of valid values in the reactive_variable=")

        self.addItems(valid_items)

        match current_selection:
            case str():
                if current_selection not in valid_items:
                    raise ValueError(
                        f'Current selection "{current_selection}" is not in a list of valid values {valid_items}'
                    )
                self.setCurrentText(current_selection)
            case int():
                self.setCurrentIndex(current_selection)
            case Variable():
                current_selection = current_selection.str_value()
                if current_selection not in valid_items:
                    raise ValueError(
                        f'Current selection "{current_selection}" is not in a list of valid values {valid_items}'
                    )
                self.setCurrentText(current_selection)

        if reactive_variable is not None:
            reactive_variable.register_value_change_callback(
                lambda v: self.setCurrentText(reactive_variable.serializer(v))
            )
            if reactive_variable.valid_values_str() is not None and valid_items != reactive_variable.valid_values_str():
                raise ValueError("Possible values set is not compatible with valid_values in the reactive_variable")
            elif current_selection is None:
                reactive_variable_value = reactive_variable.str_value()
                if reactive_variable_value in valid_items:
                    self.setCurrentText(reactive_variable_value)
                else:
                    raise ValueError(
                        f'Current selection "{reactive_variable_value}" is not in a list of valid values {valid_items}'
                    )

            if self.currentText() != reactive_variable.str_value():
                reactive_variable.set_from_str(self.currentText())

            self.change_callbacks.append(reactive_variable.set_from_str)

        if (
            current_selection is not None
            and isinstance(current_selection, int)
            and (current_selection < 0 or current_selection >= len(valid_items))
        ):
            raise ValueError("Invalid current selection index")

        self.on_focus = on_focus

        def handle_text_change(text: str):
            for callback in self.change_callbacks:
                callback(text)

        self.currentTextChanged.connect(handle_text_change)

    @property
    def textItems(self) -> list[str]:
        return [self.itemText(i) for i in range(self.count())]

    @override
    def setCurrentText(self, text: str, /) -> None:
        if text in self.textItems:
            super().setCurrentText(text)
        else:
            raise ValueError(f'Current selection "{text}" is not in a list of valid values {self.textItems}')

    @override
    def focusInEvent(self, e):
        super().focusInEvent(e)
        self.on_focus(e)
