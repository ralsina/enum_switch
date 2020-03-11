# Enum-based Switch for Python

This is an attempt at creating a way to do a reliable, not-bug-prone 
implementation, for Python, of a `switch` thing like other languages 
have.

## How it works

Suppose you have an enum, like this:

```python
class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3
```

And you want to implement logic which branches based on a value which is of type `Color`.
You can do it by subclassing the `Switch` class. The syntax should be obvious, but:

* Inherit from Switch
* Implement a method for each value of the Enum
* If you are not implementing them all: add a `default` method.
* If you leave any Enum value unaccounted for: it will raise an exception when you
  instantiate your class.

Then:

* Instantiate your class
* Call it as a function passing it a value from the Enum
* The respective method will be executed and its return value returned

```python
from enum_switch import Switch

class MySwitch(Switch):
    def RED(self):
        return "Apple"

    def GREEN(self):
        return "Kiwi"

    def BLUE(self):
        return "Sky"

switch = MySwitch(Color)

print(switch(Color.RED))

Apple
```

And that's it.

Some additional notes:

* Passing it something that is not a value of the correct Enum type will raise ValueError
* `default` is optional

Hope someone finds it useful!
