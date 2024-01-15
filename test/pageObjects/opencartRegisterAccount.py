from selenium.webdriver.common.by import By



class OpenCartRegisterAccount:
    def __init__(self, driver):
        self.driver = driver

    firstName = (By.XPATH, "//input[@id='input-firstname']")
    lastName = (By.XPATH, "//input[@id='input-lastname']")
    email = (By.XPATH, "//input[@id='input-email']")
    password = (By.XPATH, "//input[@id='input-password']")
    subscribe_Yes = (By.XPATH, "//input[@id='input-newsletter-yes']")
    subscribe_No = (By.XPATH, "//input[@id='input-newsletter-no']")
    agree_PrivacyPolicy = (By.XPATH, "//input[@name='agree']")
    continue_RegisterAccount = (By.XPATH, "//button[normalize-space()='Continue']")


    def get_BaseURL(self):
        return self.driver.get("BASE_URL_DEMO")

    def get_firstName(self):
        #driver = webdriver.Chrome()
        return self.driver.find_elements(*OpenCartRegisterAccount.firstName)

    def get_lastName(self):
        #driver = webdriver.Chrome()
        return self.driver.find_elements(*OpenCartRegisterAccount.lastName)

    def get_email(self):
        #driver = webdriver.Chrome()
        return self.driver.find_elements(*OpenCartRegisterAccount.email)

    def get_Password(self):
        return self.driver.find_elements(*OpenCartRegisterAccount.password)

    def get_Subscribe_Yes(self):
        return self.driver.find_elements(*OpenCartRegisterAccount.subscribe_Yes)

    def get_Subscribe_No(self):
        return self.driver.find_elements(*OpenCartRegisterAccount.subscribe_No)

    def get_AgreePrivacyPolicy(self):
        return self.driver.find_elements(*OpenCartRegisterAccount.agree_PrivacyPolicy)

    def get_ContinueRegistorAccountButton(self):
        return self.driver.find_elements(*OpenCartRegisterAccount.continue_RegisterAccount)