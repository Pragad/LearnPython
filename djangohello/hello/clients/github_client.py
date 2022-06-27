import requests


class GithubClient():
    def get_downstream_key(self) -> str:
        return 'github'

    def get_git_url(self, username):
        url = 'https://api.github.com/users/{}'.format(username)
        try:
            response = requests.get(url, timeout=3)
            if response.status_code == 200:
                url = response.json().get('avatar_url')
                return url
        except Exception as e:
            print(
                'Exception occurred while fetching user github image'
            )
        return False
