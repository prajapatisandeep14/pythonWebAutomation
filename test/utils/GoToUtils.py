from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from test.utils.inputDataUtils import InputDataFromFaker

class GotoPage:
    def __init__(self, driver):
        self.driver = driver

    MyAccount = (By.XPATH, "//span[normalize-space()='My Account']")
    Register = (By.XPATH, "//a[normalize-space()='Register']")
    Login = (By.XPATH, "//a[normalize-space()='Login']")


    def get_MyAccount(self):
        return self.driver.find_element(*GotoPage.MyAccount)

    def get_Register(self):
        return self.driver.find_element(*GotoPage.Register)

    def get_Login(self):
        return self.driver.find_element(*GotoPage.Login)

    def waitForElement(self, driver, waitInSeconds):
        wait = WebDriverWait(driver, waitInSeconds)
        return wait

    def goToMyAccount(self, driver, waitInSeconds):
        driver = webdriver.Chrome()
        driver.get("BASE_URL_DEMO")
        wait = self.waitForElement(driver, waitInSeconds)
        isAmyAccountPresent = wait.until(
            EC.text_to_be_present_in_element((By.XPATH, "//span[normalize-space()='My Account']"), "My Account"))
        try:
            if isAmyAccountPresent == True:
                self.get_MyAccount().click()
        except Exception as exception:
            raise f"My Account Not visible even after waiting {waitInSeconds}"


    def goToRegisterPage(self, driver, waitInSeconds):
        self.goToMyAccount(driver, waitInSeconds)
        self.get_Register().click()

    def goToLoginPage(self, driver, waitInSeconds):
        self.goToMyAccount(driver, waitInSeconds)
        self.get_Login().click()