from selenium import webdriver
from time import sleep

# Ez elindít egy Chrome-ot
chrome = webdriver.Chrome()  # WebDriver

# Ez elvisz a megfelelő címre
chrome.get("http://localhost/welcome/")

# Ez lekéri a beviteli mezőt
name_input_field = chrome.find_element(value="name-input")  # WebElement

name_input_field.send_keys("John Doe")

ok_button = chrome.find_element(value="welcome-button")
ok_button.click()

# result_div = chrome.find_element(value="welcome-div")
# result_text = result_div.text

result_text = chrome.find_element(value="welcome-div").text.upper()

print(result_text)


sleep(3)
