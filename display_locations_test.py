import locations_api
from selenium import webdriver
from locations_po import LocationsPage
import pytest


@pytest.fixture
def page():
    driver = webdriver.Chrome()
    driver.maximize_window()
    page = LocationsPage(driver)
    page.go()
    return page


def test_one_location(page):
    locations_api.delete_all()
    locations_api.create("Budapest")

    page.name_in_first_row_is("Budapest")
