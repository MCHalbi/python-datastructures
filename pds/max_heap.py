# Author: Lukas Halbritter <halbritl@informatik.uni-freiburg.de>
# Copyright 2021
from math import ceil
from typing import Tuple

class MaxHeap:
    def __init__(self):
        self._data = []

    @property
    def size(self) -> int:
        return len(self._data)

    @property
    def is_empty(self) -> bool:
        return not bool(self._data)

    @property
    def max(self) -> object:
        return self._data[0]

    def insert(self, obj: object) -> None:
        self._data.append(obj)
        self._up_heap()

    def extract(self) -> object:
        self._swap(0, -1)
        result = self._data.pop()
        if not self.is_empty:
            self._down_heap()

        return result

    def _up_heap(self) -> None:
        node_value = self._data[-1]
        child_index = -1
        parent_index = self._parent_index(child_index)

        while (self._data[parent_index] < node_value and child_index != 0):
            self._swap(parent_index, child_index)

            child_index = parent_index
            parent_index = self._parent_index(child_index)

    def _parent_index(self, index: int) -> int:
        while index < 0:
            index += self.size

        return ceil(index / 2) - 1

    def _swap(self, index1: int, index2: int) -> None:
        cache = self._data[index1]
        self._data[index1] = self._data[index2]
        self._data[index2] = cache

    def _down_heap(self) -> None:
        node_value = self._data[0]
        parent_index = 0
        child_indices = self._child_indices(parent_index)

        if (not child_indices):
            return

        child_values = tuple(self._data[index] for index in child_indices)
        larger_child_index = child_indices[child_values.index(max(child_values))]

        while (max(child_values) > node_value):
            self._swap(parent_index, larger_child_index)
            print(f"down_heap -> Data = {self._data}")

            parent_index = larger_child_index
            child_indices = self._child_indices(parent_index)

            if (not child_indices):
                return

            child_values = tuple(self._data[index] for index in child_indices)
            larger_child_index = child_indices[child_values.index(max(child_values))]

    def _child_indices(self, index: int) -> Tuple[int, int]:
        if self._is_leaf(index):
            return None

        if 2 * index + 2 >= self.size:
            return (2 * index + 1,)

        return (2 * index + 1, 2 * index + 2)

    def _is_leaf(self, index: int) -> bool:
        return 2 * index + 1 >= self.size
