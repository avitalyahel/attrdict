from typing import Any


class AttrDict(dict):
    """
    Apply attribute interface for dictionary items.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for arg in args:
            assert isinstance(arg, dict)

            for k, v in arg.items():
                self[k] = self._value(v)

        for k, v in kwargs.items():
            self[k] = self._value(v)

    def _value(self, v) -> object:
        if isinstance(v, dict):
            return AttrDict(v)

        elif isinstance(v, list):
            return [self._value(o) for o in v]

        else:
            return v

    def __setattr__(self, key, value):
        self[key] = self._value(value)

    def __getattr__(self, key):
        return self[key]

    @property
    def __dict__(self) -> dict:
        return dict((k, v.__dict__ if isinstance(v, AttrDict) else (
            [(o.__dict__ if isinstance(o, dict) else o) for o in v] if isinstance(v, list) else v))
                    for k, v in self.items())

    def __repr__(self) -> str:
        return '<AttrDict ' + \
               ', '.join(f"{key}: {self.quote(val)}" for key, val in self.items() if val) + \
               '>'

    @staticmethod
    def quote(s: Any) -> str:
        return f"'{s}'" if isinstance(s, str) else str(s)

    def __getstate__(self) -> dict:
        return self.__dict__

    def __setstate__(self, state):
        self.__init__(**state)
