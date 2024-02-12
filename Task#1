import time
import yaml
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# файл конфигурации теста
with open("./testdata.yaml") as f:
    testdata = yaml.safe_load(f)
    browser = testdata["browser"]

site = Site(testdata["addres"])

def test_step_1(site, path_login, path_passwd, button, element, result):
    # через фикстуры передаются данные о сайте пароле юзере и др
    input1 = site.find_element("xpath", path_login)
    input1.send_keys("test")
    input2 = site.find_element("xpath", path_passwd)
    input2.send_keys("test")
    btn = site.find_element("xpath", button)
    btn.click()
    err_label = site. find_element("xpath", element)
    assert err_label.text == result

