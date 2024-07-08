#!/usr/bin/env python3
"""The  Shebnag for Python"""
import unittest
from parameterized import parameterized


def access_nested_map(nested_map, path):
    """ utils.access_nested_map function"""
    current_value = nested_map
    for key in path:
        current_value = current_value[key]
    return current_value


class TestAccessNestedMap(unittest.TestCase):
    """ Class for testing"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        """ This function assert eqauls  to
        check the nested_map , path aginst the result"""
        self.assertEqual(access_nested_map(nested_map, path), expected_result)


if __name__ == '__main__':
    unittest.main()
