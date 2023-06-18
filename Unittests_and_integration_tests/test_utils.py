#!/usr/bin/env python3
"""Ce fichier contient les tests unitaires pour le module utils"""
import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from unittest.mock import Mock, patch


class TestAccessNestedMap(unittest.TestCase):
    """Classe de tests pour la fonction access_nested_map"""

    @parameterized.expand([
        ({"a": 1}, ["a"], 1),  # Cas simple avec une clé existante
        ({"a": {"b": 2}}, ["a"], {"b": 2}),  # Cas avec un dictionnaire imbriqué
        ({"a": {"b": 2}}, ["a", "b"], 2),  # Cas avec un chemin profond dans le dictionnaire
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Teste la fonction access_nested_map"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),  # Cas avec un chemin invalide
        ({"a": 1}, ("a", "b"))  # Cas avec une clé manquante dans le chemin
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """Teste l'exception levée par access_nested_map"""
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """Classe de tests pour la fonction get_json"""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),  # Cas avec une URL valide et une réponse JSON
        ("http://holberton.io", {"payload": False})  # Cas avec une autre URL et une réponse JSON différente
    ])
    def test_get_json(self, test_url, test_payload):
        """Teste la fonction get_json"""
        class Mocked(Mock):
            """Classe mock pour simuler la réponse de requests.get"""

            def json(self):
                """Méthode mock pour retourner les données JSON"""
                return test_payload

        with patch('requests.get') as MockClass:
            MockClass.return_value = Mocked()
            self.assertEqual(get_json(test_url), test_payload)


class TestMemoize(unittest.TestCase):
    """Classe de tests pour le décorateur memoize"""

    def test_memoize(self):
        """Teste le fonctionnement du décorateur memoize"""

        class TestClass:
            """Classe de test pour la démonstration du décorateur memoize"""

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, 'a_method') as mocked:
            spec = TestClass()
            spec.a_property
            spec.a_property
            mocked.assert_called_once()


if __name__ == '__main__':
    unittest.main()
