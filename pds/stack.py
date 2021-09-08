# Author: Lukas Halbritter <halbritl@informatik.uni-freiburg.de>
# Copyright 2021
import typing

class Stack:
    def __init__(self):
        self._data = []

    @property
    def count(self) -> int:
        return len(self._data)

    def push(self, obj: object) -> None:
        self._data.append(obj)

    def peek(self) -> object:
        return self._data[-1]

    def pop(self) -> object:
        return self._data.pop()

    def clear(self) -> None:
        self._data.clear()
