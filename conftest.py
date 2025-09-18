import pytest
from selenium import webdriver
from helper.urls import Urls
from pages.main_page import MainPage


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.get(Urls.BASE_URL)
    main_page = MainPage(driver)
    main_page.accept_cookies()
    yield driver
    driver.quit()


# Для корректного отображения аргументов в параметризированном тесте
def pytest_make_parametrize_id(val):
    return repr(val)