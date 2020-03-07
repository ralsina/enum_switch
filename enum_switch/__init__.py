class Switch:
    def __init__(self, enum):
        self.__enum = enum
        # Check if we have a default handler
        if hasattr(self, "default"):
            return
        # If not, we need handlers for all cases
        for e in enum:
            if not hasattr(self, e.name):
                raise AttributeError(f"Unhandled switch branch: {e.name}")

    def __call__(self, value):
        if not isinstance(value, self.__enum):
            raise ValueError(f"Invalid value: {value}")
        if hasattr(self, value.name):
            return getattr(self, value.name)()
        else:
            return self.default()  # NOQA
