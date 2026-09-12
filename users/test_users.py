import pytest


def test_get_all_users(api_session, base_url):
    response = api_session.get(f"{base_url}/users")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_single_user(api_session, base_url):
    response = api_session.get(f"{base_url}/users/1")
    assert response.status_code == 200
    user = response.json()
    assert user["id"] == 1
    assert "email" in user


def test_create_user(created_user):
    assert "id" in created_user
    assert created_user["name"] == "Test User"


@pytest.mark.parametrize("user_id", [1, 3, 7])
def test_get_multiple_users(api_session, base_url, user_id):
    response = api_session.get(f"{base_url}/users/{user_id}")
    assert response.status_code == 200