import functools
from datetime import timedelta, date

import pytest
import time
import yaml
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# библиотеки для скачивания драйверов браузеров


class Site:
    # проверка на то какой браузер используется в тесте
    def __init__(self, browser, address):
        print(1)
        self.address = address
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(3)
        self.driver.maximize_window()
        self.driver.get(address)
        self.browser = browser
        time.sleep(testdata["sleep_time"])

    def find_element(self, mode, path):
        if mode == "css":
            element = self.driver.find_element(By.CSS_SELECTOR, path)
        elif mode == "xpath":
            element = self.driver.find_element(By.XPATH, path)
        else:
            element = None
        return element

    def get_element_property(self, mode, path, property):
        element = self.find_element(mode, path)
        return element.value_of_css_property(property)

    def go_to_site(self):
        return self.driver.get(self.address)

    def close(self):
        self.driver.close()


# файл конфигурации теста
with open("./testdata.yaml") as f:
    testdata = yaml.safe_load(f)
    browser = testdata["browser"]
    username = testdata['user_name']
    passwd = testdata['passwd']
    addres = testdata['addres']
    site = Site(testdata["browser"],testdata['addres'])


def registration_on_the_website():
    x_selector1 = """//*[@id="login"]/div[1]/label/input"""  # вводим Username
    input1 = site.find_element("xpath", x_selector1)
    input1.send_keys(username)

    x_selector2 = """//*[@id="login"]/div[2]/label/input"""  # вводим passwd
    input2 = site.find_element("xpath", x_selector2)
    input2.send_keys(passwd)

    btn_selector = "button"
    btn = site.find_element("css", btn_selector)
    btn.click()

def test_step1():
    # Тест при не правильном вводе данных пользователя
    x_selector1 = """//*[@id="login"]/div[1]/label/input"""  # вводим Username
    input1 = site.find_element("xpath", x_selector1)
    input1.send_keys("test")

    x_selector2 = """//*[@id="login"]/div[2]/label/input"""  # вводим passwd
    input2 = site.find_element("xpath", x_selector2)
    input2.send_keys("test")

    btn_selector = "button"
    btn = site.find_element("css", btn_selector)
    btn.click()

    x_selector3 = """//*[@id="app"]/main/div/div/div[2]/h2"""  # Поиск сообщения об ошибке после неверного ввода
    err_label = site.find_element("xpath", x_selector3)
    assert err_label.text == "401"


def test_step2():
    # Тест при правильном вводе данных пользователя
    registration_on_the_website()
    time.sleep(1)

    # Ищу слово Blog, которое высвечивается после успешной регистрации
    x_selector3 = """//*[@id="app"]/main/div/div[1]/h1"""
    flag_text_blog = site.find_element("xpath", x_selector3)
    assert flag_text_blog.text == "Blog"


def test_step3():
    # Тест создание нового поста

    # Нажимаю на кнопку Нового поста
    btn_selector = """//*[@id="create-btn"]"""
    btn = site.find_element("xpath", btn_selector)
    btn.click()

    # Создание тайтла у поста
    x_titel = """//*[@id="create-item"]/div/div/div[1]/div/label/input"""
    input_titel = site.find_element("xpath", x_titel)
    input_titel.send_keys("test_titel")

    # Создание дискрипшена
    x_discription = """//*[@id="create-item"]/div/div/div[2]/div/label/span/textarea"""
    input_discription = site.find_element("xpath", x_discription)
    input_discription.send_keys("test_discription")

    # Создание контента
    x_content = """//*[@id="create-item"]/div/div/div[3]/div/label/span/textarea"""
    input_content = site.find_element("xpath", x_content)
    input_content.send_keys("test_content")

    # # Создание колендаря
    # ddd1 = date.today()  # создание даты для ввода
    # ddd1 = ddd1 - timedelta(days=1)
    # i = int(ddd1.day) + 1  # вводим дату на "завтра"
    # 
    # x_calendar = """//*[@id="create-item"]/div/div/div[5]/div/div/label"""
    # input_calendar = site.find_element("xpath", x_calendar)
    # input_calendar[i].click()

    #Кликаю на кнопку Save
    x_btm_save = """/html/body/div/main/div/div/form/div/div/div[7]/div/button/span"""
    btn_save = site.find_element("xpath", x_btm_save)
    btn_save.click()
    print("click save")

    # Ищу название нового поста, если посту успешно будет создан то название поста будет верное

    x_name_post = """//*[@id="app"]/main/div/div[1]/h1"""
    flag_name_post = site.find_element("xpath", x_name_post)

    site.close()
    time.sleep(5)

    assert flag_name_post == "test_titel"
