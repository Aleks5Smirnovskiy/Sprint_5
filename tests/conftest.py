import pytest
from selenium import webdriver

from helpers import build_listing_payload, build_user_credentials
from page_objects.desk_page import DeskPage


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-search-engine-choice-screen")
    options.add_experimental_option("excludeSwitches", ["enable-logging"])

    chrome_driver = webdriver.Chrome(options=options)
    yield chrome_driver
    chrome_driver.quit()


@pytest.fixture
def desk_page(driver):
    return DeskPage(driver)


@pytest.fixture
def registered_user(desk_page):
    credentials = build_user_credentials()
    desk_page.register_user(credentials["email"], credentials["password"])
    return credentials


@pytest.fixture
def logged_out_registered_user(desk_page):
    credentials = build_user_credentials()
    desk_page.register_user(credentials["email"], credentials["password"])
    desk_page.logout()
    return credentials


@pytest.fixture
def listing_data():
    return build_listing_payload()