import pytest
import allure
import json
from models import Posts

def test_get_all_posts(api_session, base_url):
    response = api_session.get(f"{base_url}/posts")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_single_post(api_session, base_url):
    with allure.step("Перевірка чи повертається код 200"):
        response = api_session.get(f"{base_url}/posts/1")
        assert response.status_code == 200
    with allure.step("Перевірка чи айді нашого посту 1"):
        post = Posts.model_validate(response.json())
        assert post.id == 1


def test_create_post(created_post):
    with allure.step("Перевірка, що є id"):
        assert "id" in created_post
    with allure.step("Перевірка заголовка"):
        assert created_post["title"] == "Test title"


@pytest.mark.parametrize("post_id", [1, 5, 10])
def test_get_multiple_posts(api_session, base_url, post_id):
    response = api_session.get(f"{base_url}/posts/{post_id}")
    assert response.status_code == 200
    Posts.model_validate(response.json())