from unittest import mock

from django.test import TestCase

from hello.clients.github_client import GithubClient


# Create your tests here.
class GithubClientTests(TestCase):
    def setUp(self):
        self.github_client = GithubClient()
    
    @mock.patch('requests.get')
    def test_get_git_url(self, mock_get):
        # Arrange
        username = "hello"
        expected_response = "https://git.githubusercontent.com/u/hello"
        self.mock_response = mock.Mock()
        self.mock_response.json.return_value = {'git_url': expected_response}
        self.mock_response.status_code = 200
        mock_get.return_value = self.mock_response

        # Act
        actual_response = self.github_client.get_git_url(username)

        # Assert
        self.assertEqual(mock_get.called, True)
        self.assertEqual(expected_response, actual_response)
