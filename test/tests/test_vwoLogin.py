import pytest
from selenium import webdriver
from dotenv import load_dotenv

import allure
from test.pageObjects.loginPage import LoginPage


@pytest.fixture()
def setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    return driver


@allure.epic("VWO Login Test")
@allure.feature("TC#1 - VWO App Positive Test")
def test_vwoLogin():
    driver = setup()
    driver = LoginPage(driver)
    driver.get_BaseURL("BASE_URL_VWO")
    userName = driver.get_userName()

    # driver =


def tearDown():
    pass
