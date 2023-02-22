#!/usr/bin/env python3

"""
Test client
"""

import unittest
from parameterized import parameterized, parameterized_class
from unittest.mock import Mock, patch, PropertyMock
from fixtures import TEST_PAYLOAD
import client


class TestGithubOrgClient(unittest.TestCase):
    """ Test GithubOrgClient class
    """
    @parameterized.expand([
        ('google'),
        ('abc')
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """ Test org method
        """
        test_url = f'https://api.github.com/orgs/{org_name}'
        test_payload = {'payload': True}

        with patch('client.get_json') as mock_class:
            mock_class.return_value = test_payload
            self.assertEqual(client.GithubOrgClient(org_name).org,
                             test_payload)
            mock_class.assert_called_once_with(test_url)

    def test_public_repos_url(self):
        """ Test public_repos_url method
        """
        with patch(
            'client.GithubOrgClient.org', new_callable=PropertyMock
        ) as mock_class:
            mock_class.return_value = {'repos_url': 'test.io'}
            org_client = client
            org_client = org_client.GithubOrgClient('test_org')
            self.assertEqual(
                org_client.org['repos_url'], org_client._public_repos_url
            )

    @patch('client.get_json')
    def test_public_repos(self, mocked_method):
        """ Test public_repos method
        """
        mocked_response = [{"name": "Google"}, {"name": "TT"}]
        mocked_method.return_value = mocked_response

        with patch(
            'client.GithubOrgClient._public_repos_url',
            new_callable=PropertyMock
        ) as mocked_public:
            mocked_public.return_value = "world"
            response = client.GithubOrgClient('test').public_repos()

            self.assertEqual(response, ["Google", "TT"])

            mocked_public.assert_called_once()
            mocked_method.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expectation):
        """ Test has_license method
        """
        result = client.GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(result, expectation)


@parameterized_class(
    ("org_payload", "repos_payload", "expected_repos", "apache2_repos"),
    TEST_PAYLOAD
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """
    Integration test for GithubOrgClient
    """
    @classmethod
    def setUpClass(cls):
        """
        Set up class
        """
        requests_json = unittest.mock.Mock()
        requests_json.json.side_effect = [
            cls.org_payload, cls.repos_payload,
            cls.org_payload, cls.repos_payload,
        ]
        cls.get_patcher = patch('requests.get', return_value=requests_json)
        cls.get_patcher.start()

    def test_public_repos(self):
        """
        Test public_repos method
        """
        org = "google"
        github_org_client = client.GithubOrgClient(org)
        self.assertEqual(github_org_client.public_repos(), self.expected_repos)

    def test_public_repos_with_license(self):
        """
        Test public_repos method with license
        """
        org = "google"
        github_org_client = client.GithubOrgClient(org)
        self.assertEqual(
            github_org_client.public_repos("apache-2.0"), self.apache2_repos
        )

    @classmethod
    def tearDownClass(cls):
        """
        Tear down class
        """
        cls.get_patcher.stop()


if __name__ == '__main__':
    unittest.main()
