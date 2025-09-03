from selenium import webdriver
from selenium.webdriver.common.by import By
import random
import uuid
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located


def test_create_location():
    driver = webdriver.Chrome()
    driver.get("http://localhost:8080")

    no = random.randint(100_000, 250_000)
    my_uuid = uuid.uuid4()
    driver.find_element(By.ID, "create-location-link").click()
    driver.find_element(By.ID, "location-name").send_keys(f"Balaton {my_uuid}")
    driver.find_element(By.ID, "location-coords").send_keys("47.4979,19.0402")

    driver.find_element(
        By.CSS_SELECTOR, 'input[type="submit"][value="Create location"]'
    ).click()

    wait = WebDriverWait(driver, 3)
    # message_div = wait.until(presence_of_element_located((By.ID, "message-div")))

    # assert message_div.text == "Location has been created"

    wait.until(
        lambda _: driver.find_element(By.ID, "message-div").text
        == "Location has been created"
    )
