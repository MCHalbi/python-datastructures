# Author: Lukas Halbritter <halbritl@informatik.uni-freiburg.de>
# Copyright 2021
# pylint: disable=missing-docstring
import unittest
from pds import MaxHeap

class MaxHeapTests(unittest.TestCase):
    def setUp(self):
        self._heap = MaxHeap()

    def test_new_heap_has_no_elements(self):
        self.assertEqual(0, self._heap.size)

    def test_new_heap_is_empty(self):
        self.assertTrue(self._heap.is_empty)

    def test_inserting_an_element_increases_the_size(self):
        self._heap.insert(42)

        self.assertEqual(1, self._heap.size)

    def test_max_element_is_found_1(self):
        self._heap.insert(23)
        self._heap.insert(42)

        self.assertEqual(42, self._heap.max)

    def test_max_element_is_found_2(self):
        self._heap.insert(23)
        self._heap.insert(42)
        self._heap.insert(13)
        self._heap.insert(123)

        self.assertEqual(123, self._heap.max)

    def test_max_element_is_found_3(self):
        self._heap.insert(23)
        self.assertEqual(23, self._heap.max)

        self._heap.insert(42)
        self.assertEqual(42, self._heap.max)

        self._heap.insert(13)
        self.assertEqual(42, self._heap.max)

        self._heap.insert(123)
        self.assertEqual(123, self._heap.max)

        self.assertEqual(123, self._heap.extract())
        self.assertEqual(42, self._heap.extract())
        self.assertEqual(23, self._heap.extract())
        self.assertEqual(13, self._heap.extract())
