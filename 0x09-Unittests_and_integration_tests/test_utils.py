#!/usr/bin/env python3
"""Unittests and Integration Tests module
"""
import unittest
from unittest.mock import patch
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """TestAccessNestedMap class"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, result):
        """Test access_nested_map function"""
        self.assertEqual(access_nested_map(nested_map, path), result)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """Test access_nested_map function raising a KeyError"""
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """TestGetJson class"""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch('requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        """Test get_json function"""
        mock_get.return_value.json.return_value = test_payload
        self.assertEqual(get_json(test_url), test_payload)
        mock_get.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """TestMemoize class"""

    def test_memoize(self):
        """Test memoize decorator"""

        class TestClass:
            """Test class"""

            def a_method(self):
                """Method returning 42"""
                return 42

            @memoize
            def a_property(self):
                """Property decorated by memoize"""
                return self.a_method()

        with patch.object(TestClass, 'a_method') as mock_a_method:
            t = TestClass()
            result = t.a_property
            result2 = t.a_property
            self.assertEqual(result, 42)
            self.assertEqual(result2, 42)
            mock_a_method.assert_called_once()

if __name__ == '__main__':
    unittest.main()
