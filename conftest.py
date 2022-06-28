import pytest
from selene.support.shared import browser


@pytest.fixture()
def open_browser():
    return browser.open("https://duckduckgo.com/")


@pytest.fixture(autouse=True)
def quit_browser():
    yield
    browser.quit()


@pytest.fixture(autouse=True)
def full_size_browser(open_browser):
    browser.driver.maximize_window()
