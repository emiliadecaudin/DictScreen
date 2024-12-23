""""""

# --- Imports ------------------------------------------------------------------------ #

from collections.abc import ItemsView, Iterator, KeysView, MutableMapping, ValuesView
from typing import overload

# --- CLasses ------------------------------------------------------------------------ #

class DictScreen[_V](MutableMapping):
    _dict: dict[str, _V]

    def __init__(self, screened_dict: dict[str, _V]) -> None:
        super().__setattr__("_dict", screened_dict)

    def __getattr__(self, key: str) -> _V:
        return self._dict.__getitem__(key)

    def __setattr__(self, key: str, value: _V) -> None:
        self._dict.__setitem__(key, value)

    def __delattr__(self, key: str) -> None:
        self._dict.__delitem__(key)

    def __getitem__(self, key: str) -> _V:
        return self._dict.__getitem__(key)

    def __setitem__(self, key: str, value: _V) -> None:
        self._dict.__setitem__(key, value)

    def __delitem__(self, key: str) -> None:
        self._dict.__delitem__(key)

    def __contains__(self, key: object) -> bool:
        return self._dict.__contains__(key)

    def __iter__(self) -> Iterator[str]:
        return self._dict.__iter__()

    def __len__(self) -> int:
        return self._dict.__len__()

    def __str__(self) -> str:
        return self._dict.__str__()

    def __repr__(self) -> str:
        return self._dict.__repr__()

    def __reversed__(self) -> Iterator[str]:
        return self._dict.__reversed__()

    def clear(self) -> None:
        self._dict.clear()

    @overload
    def get(self, key: str, /) -> _V | None: ...

    @overload
    def get[_T](self, key: str, /, default: _T) -> _V | _T: ...

    def get[_T](self, key: str, /, default: _T | None = None) -> _V | _T | None:
        return self._dict.get(key, default)

    def items(self) -> ItemsView[str, _V]:
        return self._dict.items()

    def keys(self) -> KeysView[str]:
        return self._dict.keys()

    def values(self) -> ValuesView[_V]:
        return self._dict.values()

    @overload
    def pop(self, key: str, /) -> _V: ...

    @overload
    def pop[_T](self, key: str, /, default: _T) -> _V | _T | None: ...

    def pop[_T](self, key: str, /, default: _T | None = None) -> _V | _T | None:
        return self._dict.pop(key, default)


class TestScreen(DictScreen):
    id: int
    name: str

y: dict[str, str | int] = {"first_name": "John", "last_name": "Doe", "id": 10598}
x = TestScreen(y)
z = x["id"]

class X:

    def __call__(self, cls):
        return cls

@X
class Y:
    pass
