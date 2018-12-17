import requests

GITHUB_URL = 'https://api.github.com'


def get_followers(user_login, limit=None):
    url = '%s/users/%s/followers' % (GITHUB_URL, user_login)
    resp = requests.get(url)
    resp.raise_for_status()
    data = resp.json()
    if limit and len(data) > limit:
        return resp.json()[:limit]
    return resp.json()
