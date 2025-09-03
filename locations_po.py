from selenium import webdriver
from selenium.webdriver.common.by import By
import random
import uuid
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located


class LocationsPage:
    def __init__(self, driver):
        self.driver = driver

    def go(self):
        self.driver.get("http://localhost:8080")

    def create_location(self, name, coords):
        self.driver.find_element(By.ID, "create-location-link").click()
        self.driver.find_element(By.ID, "location-name").send_keys(name)
        self.driver.find_element(By.ID, "location-coords").send_keys(coords)
        self.driver.find_element(
            By.CSS_SELECTOR, 'input[type="submit"][value="Create location"]'
        ).click()

    def assert_message_is(self, message):
        wait = WebDriverWait(self.driver, 3)
        wait.until(
            lambda _: self.driver.find_element(By.ID, "message-div").text == message
        )

    def name_validation_message_is(self, message):
        wait = WebDriverWait(self.driver, 3)
        wait.until(
            lambda _: self.driver.find_element(By.ID, "location-name-feedback").text
            == message
        )
