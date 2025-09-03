from selenium import webdriver


def test_print_hello():
    chrome = webdriver.Chrome()
    chrome.get("http://localhost/welcome/")

    chrome.find_element(value="name-input").send_keys("John")
    chrome.find_element(value="welcome-button").click()
    result = chrome.find_element(value="welcome-div").text
    assert result == "Hello John!"
