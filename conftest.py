import pytest
import requests
import allure
import json
import os
from config import Settings
from requests.adapters import HTTPAdapter

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")
        if page:
            screenshot = page.screenshot()
            allure.attach(
                screenshot,
                name="screenshot_on_failure",
                attachment_type=allure.attachment_type.PNG
            )

settings = Settings()

class AllureSession(requests.Session):
    def request(self, method, url, *args, **kwargs):
        response = super().request(method, url, *args, **kwargs)

        allure.attach(
            f"{method} {url}",
            name="Request",
            attachment_type=allure.attachment_type.TEXT
        )
        try:
            body = json.dumps(response.json(), indent=2, ensure_ascii=False)
            attach_type = allure.attachment_type.JSON
        except ValueError:
            body = response.text
            attach_type = allure.attachment_type.TEXT

        allure.attach(
            body,
            name=f"Response ({response.status_code})",
            attachment_type=attach_type
        )
        return response

@pytest.fixture(scope="session")
def base_url():
    return settings.base_url

@pytest.fixture(scope="session")
def api_session():
    session = AllureSession()
    adapter = HTTPAdapter()
    session.mount("https://", adapter)
    session.headers.update({
        "Content-Type": "application/json",
        "Authorization": f"Bearer {settings.api_token}",
    })
    yield session
    session.close()