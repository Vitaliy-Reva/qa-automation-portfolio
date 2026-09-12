import pytest


@pytest.fixture
def make_comment(api_session, base_url):
    def _make_comment(post_id=1, name="Test Commenter", email="commenter@example.com", body="Test comment body"):
        payload = {"postId": post_id, "name": name, "email": email, "body": body}
        response = api_session.post(f"{base_url}/comments", json=payload)
        response.raise_for_status()
        return response.json()
    return _make_comment


@pytest.fixture
def created_comment(make_comment):
    return make_comment()