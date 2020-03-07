from enum import Enum

import pytest
from enum_switch import Switch


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

class Animal(Enum):
    DOG = 1
    CAT = 2

def test_no_default_missing_branch():
    class MySwitch(Switch):
        def RED(self):
            return "Apple"

        def GREEN(self):
            return "Kiwi"

    with pytest.raises(AttributeError) as exc:
        MySwitch(Color)
    assert "Unhandled switch branch: BLUE" in str(exc)


def test_with_default():
    class MySwitch(Switch):
        def default(self):
            return "foo"

    s = MySwitch(Color)
    assert s(Color.RED) == "foo"
    assert s(Color.GREEN) == "foo"
    assert s(Color.BLUE) == "foo"


def test_no_default_all_branches():
    class MySwitch(Switch):
        def RED(self):
            return "Apple"

        def GREEN(self):
            return "Kiwi"

        def BLUE(self):
            return "Sky"

    s = MySwitch(Color)
    assert s(Color.RED) == "Apple"
    assert s(Color.GREEN) == "Kiwi"
    assert s(Color.BLUE) == "Sky"


def test_default_and_all_branches():
    class MySwitch(Switch):
        def RED(self):
            return "Apple"

        def GREEN(self):
            return "Kiwi"

        def BLUE(self):
            return "Sky"

        def default(self):
            return "Banana"

    s = MySwitch(Color)
    # No call should return Banana from default
    assert s(Color.RED) == "Apple"
    assert s(Color.GREEN) == "Kiwi"
    assert s(Color.BLUE) == "Sky"

def test_called_with_wrong_value():
    class MySwitch(Switch):
        def default(self):
            return "foo"

    s = MySwitch(Color)
    with pytest.raises(ValueError) as exc:
        s(Animal.CAT)
    assert "Invalid value: Animal.CAT" in str(exc)