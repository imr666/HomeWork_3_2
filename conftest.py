import pytest
from selene.support.shared import browser

@pytest.fixture()
def open():
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.open('https://google.com/ncr')