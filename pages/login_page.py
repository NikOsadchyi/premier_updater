from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_field = (By.ID, "username")
        self.password_field = (By.ID, "current-password")
        self.login_button = (By.ID, "LoginPageContent__2268_btnLogin")

    def enter_username(self, username: str, timeout: int = 10):
        self.driver.find_element(*self.username_field).send_keys(username)

    def enter_password(self, password: str):
        self.driver.find_element(*self.password_field).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(*self.login_button).click()
