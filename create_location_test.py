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


def test_create_location(page):
    page.create_location()
    page.assert_message_is("Location has been created")


def test_create_location_with_empty_name(page):
    page.create_location("")
    page.name_validation_message_is("Can not be empty name!")
