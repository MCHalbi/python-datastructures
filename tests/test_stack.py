# Author: Lukas Halbritter <halbritl@informatik.uni-freiburg.de>
# Copyright 2021
# pylint: disable=missing-docstring
import unittest
from pds import Stack

class StackTests(unittest.TestCase):
    def setUp(self):
        self._stack = Stack()

    def test_new_stack_is_empty(self):
        self.assertEqual(0, self._stack.count)

    def test_stack_has_one_element_more_after_push(self):
        self._stack.push('foo')

        self.assertEqual(1, self._stack.count)

    def test_stack_has_last_pushed_element_on_top(self):
        self._stack.push('foo')
        self._stack.push('bar')

        self.assertEqual('bar', self._stack.peek())

    def test_peek_does_not_remove_element(self):
        self._stack.push('foo')
        self._stack.peek()

        self.assertEqual(1, self._stack.count)

    def test_pop_returns_element_on_top(self):
        self._stack.push('foo')
        self._stack.push('bar')

        self.assertEqual('bar', self._stack.pop())

    def test_pop_removes_element_on_top(self):
        self._stack.push('foo')
        self._stack.push('bar')
        self._stack.pop()

        self.assertEqual(1, self._stack.count)

    def test_clear_removes_all_objects_from_list(self):
        self._stack.push('foo')
        self._stack.push('bar')
        self._stack.clear()

        self.assertEqual(0, self._stack.count)

