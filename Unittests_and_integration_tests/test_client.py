#!/usr/bin/env python3
"""Test client"""
import unittest
from parameterized import parameterized, parameterized_class
import client
from client import GithubOrgClient
from unittest.mock import Mock, patch, PropertyMock
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """Classe de tests pour la classe GithubOrgClient"""

    @parameterized.expand([
        ('google'),  # Cas avec un nom d'organisation valide
        ('abc')  # Cas avec un nom d'organisation invalide
    ])
    @patch('client.get_json')
    def test_org(self, org, mock_get_json):
        """Teste la méthode org"""
        test_url = 'https://api.github.com/orgs/' + org
        test_payload = {'payload': True}
        with patch('client.get_json') as MockClass:
            MockClass.return_value = test_payload
            self.assertEqual(GithubOrgClient(org).org, test_payload)
            MockClass.assert_called_once_with(test_url)

    def test_public_repos_url(self):
        """Teste la propriété public_repos_url"""
        with patch(
            'client.GithubOrgClient.org', new_callable=PropertyMock
                ) as mc:
            mc.return_value = {'repos_url': 'test.io'}
            org_client = client
            org_client = org_client.GithubOrgClient('test_org')
            self.assertEqual(
                org_client.org['repos_url'], org_client._public_repos_url
                    )

    @patch('client.get_json')
    def test_public_repos(self, mocked_method):
        """Teste la méthode public_repos"""
        payload = [{"name": "Google"}, {"name": "TT"}]
        mocked_method.return_value = payload

        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mocked_public:

            mocked_public.return_value = "world"
            response = GithubOrgClient('test').public_repos()

            self.assertEqual(response, ["Google", "TT"])

            mocked_public.assert_called_once()
            mocked_method.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}},
         "my_license", True),  # Cas avec une licence correspondante
        ({"license": {"key": "other_license"}},
         "my_license", False)  # Cas avec une licence non correspondante
    ])
    def test_has_license(self, repo, key, expectation):
        """Teste la méthode has_license"""
        result = GithubOrgClient.has_license(repo, key)
        self.assertEqual(result, expectation)


@parameterized_class(
    ("org_payload", "repos_payload", "expected_repos", "apache2_repos"),
    TEST_PAYLOAD
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Classe de tests d'intégration pour la classe GithubOrgClient"""

    @classmethod
    def setUpClass(cls):
        """Méthode de configuration avant les tests de la classe"""
        requests_json = unittest.mock.Mock()
        requests_json.json.side_effect = [
            cls.org_payload, cls.repos_payload,
            cls.org_payload, cls.repos_payload,
        ]

        cls.get_patcher = patch('requests.get', return_value=requests_json)
        cls.get_patcher.start()

    def test_public_repos(self):
        """Teste la méthode public_repos"""
        org = "google"
        github_org_client = GithubOrgClient(org)

        self.assertEqual(github_org_client.public_repos(), self.expected_repos)

    def test_public_repos_with_license(self):
        """Teste la méthode public_repos_with_license"""
        org = "google"
        github_org_client = GithubOrgClient(org)

        self.assertEqual(
            github_org_client.public_repos("apache-2.0"),
            self.apache2_repos
        )

    @classmethod
    def tearDownClass(cls):
        """Méthode de nettoyage après les tests de la classe"""
        cls.get_patcher.stop()


if __name__ == '__main__':
    unittest.main()
