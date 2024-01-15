from selenium.webdriver.common.by import By

class Dashboard :
    def __init__(self, driver):
        self.driver = driver

    user_loggedIn = (By.XPATH, "")

    def get_UserLoggeIn(self):
        pass