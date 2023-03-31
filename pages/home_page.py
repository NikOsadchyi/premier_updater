from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.user_profile_menu_box = (By.ID, "UserProfileMenuBox")
        self.my_advertisements = (By.XPATH, '//*[@href="/myadvertisements.aspx"]')
        self.cookie_bar_close = (By.ID, "cookieBarCloseRef")

    def verify_user_profile_menu_box(self, timeout: int = 10):
        WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(self.user_profile_menu_box))

    def click_my_advertisements(self):
        self.driver.find_element(*self.my_advertisements).click()

    def close_cookie_bar(self, timeout: int = 10):
        WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(self.cookie_bar_close)).click()
