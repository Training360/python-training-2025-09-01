from selenium import webdriver


def open_page():
    chrome = webdriver.Chrome()
    chrome.get("http://localhost/calculator/")
    return chrome


def fill_operands(chrome, a, b):
    chrome.find_element(value="a-input").send_keys(a)
    chrome.find_element(value="b-input").send_keys(b)


def add(chrome):
    chrome.find_element(value="submit-button").click()


def read_result(chrome):
    result = chrome.find_element(value="result-input").get_attribute("value")
    return result


def test_add():
    chrome = open_page()
    print(type(chrome))
    # Given
    fill_operands(chrome, "5", "6")
    # When
    add(chrome)
    # Then
    result = read_result(chrome)
    print(type(result))
    assert result == "11"


def test_add_negatives():
    chrome = open_page()
    fill_operands(chrome, "-5", "-6")
    add(chrome)
    result = read_result(chrome)
    assert result == "-11"
