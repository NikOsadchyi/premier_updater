from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.remote.webelement import WebElement


class PageActions:
    def __init__(self, driver):
        self.driver = driver

    def move_to_element(self, element: WebElement):
        actions = ActionChains(self.driver)
        actions.move_to_element(element)
        actions.perform()
