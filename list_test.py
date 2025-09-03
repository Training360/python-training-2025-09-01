from selenium import webdriver
from selenium.webdriver.common.by import By


def test_list():
    chrome = webdriver.Chrome()
    chrome.get("http://localhost/components/")

    # list_item = chrome.find_element(
    #     By.CSS_SELECTOR, "#list-test > ul > li:nth-child(2)"
    # )
    # assert list_item.text == "Two"

    list_items = chrome.find_elements(By.CSS_SELECTOR, "#list-test > ul > li")
    print(type(list_items))
    assert len(list_items) == 4
    assert list_items[0].text == "One"

    # for item in list_items:
    #     print(item.text)

    list_texts = []
    for item in list_items:
        list_texts.append(item.text)

    # print(list_texts)

    assert list_texts == ["One", "Two", "Three", "Four"]
