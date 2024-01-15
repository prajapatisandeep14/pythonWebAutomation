# class
# Page Locators
# Page Actions
# Webdriver Init
# Custom Functions
# No Assertions in this


from selenium.webdriver.common.by import By
from selenium import webdriver

class LoginPage():

    def __init__(self, driver):
        self.driver = driver

    username = (By.XPATH,"//input[@id='login-username']") #pass as tupple
    password = (By.XPATH, "//input[@id='login-password']")
    submit_button = (By.XPATH, "//button[@id='js-login-btn']")
    #error_message = ()


    def get_BaseURL(self):
        return self.driver.get("BASE_URL_VWO")
    def get_userName(self):
        #driver = webdriver.Chrome()
        return self.driver.find_element(*LoginPage.username)

    def get_Password(self):
        return self.driver.find_element(*LoginPage.password)

    def get_LoginSubmitButton(self):
        return self.driver.find_element(*LoginPage.submit_button)


