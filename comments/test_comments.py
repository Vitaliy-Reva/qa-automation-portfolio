import pytest
import allure
import json
from models import Comments


def test_get_all_comments(api_session, base_url):
    response = api_session.get(f"{base_url}/comments")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_single_comment(api_session, base_url):
    response = api_session.get(f"{base_url}/comments/1")
    assert response.status_code == 200
    comment = Comments.model_validate(response.json())
    assert comment.id == 1


def test_create_comment(created_comment):
    with allure.step("Перевірка, що є id"):
        assert "id" in created_comment
    with allure.step("Перевірка тіла коментаря"):
        assert created_comment["body"] == "Test comment body"


@pytest.mark.parametrize("comment_id", [1, 4, 8])
def test_get_multiple_comments(api_session, base_url, comment_id):
    response = api_session.get(f"{base_url}/comments/{comment_id}")
    assert response.status_code == 200
    Comments.model_validate(response.json())