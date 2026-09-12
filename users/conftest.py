import pytest


@pytest.fixture
def make_user(api_session, base_url):
    def _make_user(name="Test User", username="testuser", email="test@example.com"):
        payload = {"name": name, "username": username, "email": email}
        response = api_session.post(f"{base_url}/users", json=payload)
        response.raise_for_status()
        return response.json()
    return _make_user


@pytest.fixture
def created_user(make_user):
    return make_user()