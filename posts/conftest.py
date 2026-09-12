import pytest


@pytest.fixture
def make_post(api_session, base_url):
    def _make_post(title="Test title", body="Test body", user_id=1):
        payload = {"title": title, "body": body, "userId": user_id}
        response = api_session.post(f"{base_url}/posts", json=payload)
        response.raise_for_status()
        return response.json()
    return _make_post


@pytest.fixture
def created_post(make_post):
    return make_post()