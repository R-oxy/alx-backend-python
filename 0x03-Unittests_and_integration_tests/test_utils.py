#!/usr/bin/env python3
"""Unit tests for utils.access_nested_map."""

import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """Test class for access_nested_map."""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, map, path, expected):
        """Test access_nested_map function."""
        self.assertEqual(access_nested_map(map, path), expected)


if __name__ == "__main__":
    unittest.main()
