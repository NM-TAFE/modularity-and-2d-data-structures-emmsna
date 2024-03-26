from unittest import TestCase

from board import Board


class TestBoard(TestCase):
    def test_is_position_invalid(self):
        testboard = Board()
        self.size = 3
        actual = testboard.is_position_invalid(5, 5)
        expected = True
        self.assertEqual(actual, expected)
