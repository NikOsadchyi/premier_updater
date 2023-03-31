from selenium.common import TimeoutException, NoSuchElementException, ElementNotInteractableException, \
    ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from utils.page_actions import PageActions


class MyAdvertisementsPage:
    def __init__(self, driver):
        self.driver = driver
        self.my_advertisements_block = (By.ID, "my-advertisements-block")
        self.sorting_block = (By.XPATH, 'class="sorting-block"')
        self.up_advert_buttons_list = (By.XPATH, '//*[@data-bind="visible: showUpBtn()"]/td[2]/a')
        self.wait_dialog_widget = (By.ID, "ui-id-1")
        self.creative_iframe = (By.ID, "aswift_7")
        self.creative_widget = (By.ID, "creative")  # targeting advertising
        self.creative_dismiss_button = (By.ID, "dismiss-button")
        self.ad_iframe = (By.ID, "ad_iframe")
        self.adv_items = (By.XPATH, '//div[@class="adv-item"]')

    def verify_adv_item(self, timeout: int = 10):
        WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(self.adv_items))

    def up_adverts(self, timeout: int = 10):
        """
        up all adverts presented on current page
        """
        up_advert_buttons = self.driver.find_elements(*self.up_advert_buttons_list)
        for button in up_advert_buttons:
            # omit buttons where грн is present because the limit for updating is exceeded or if empty string
            if "грн" in button.text or not button.text:
                continue
            page_actions = PageActions(self.driver)
            page_actions.move_to_element(button)
            ignored_exceptions = [ElementClickInterceptedException]
            WebDriverWait(self.driver,
                          timeout,
                          ignored_exceptions=ignored_exceptions).until(EC.element_to_be_clickable(button)).click()
            self.wait_dialog()

    def skip_creative_if_exist(self, timeout: int = 3):
        """
        skip targeting advertising from side resources if exist
        there are 2 types of adverts with different iframe location, 1st is located in one iframe, 2nd in two iframes
        """
        try:
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(self.creative_iframe))
            # creative is located in iframe
            iframe = self.driver.find_element(*self.creative_iframe)
            self.driver.switch_to.frame(iframe)
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(self.creative_widget))
            try:
                # for adverts which are not in another iframe
                self.driver.find_element(*self.creative_dismiss_button).click()
            except NoSuchElementException:
                # switch to another target advert
                iframe = self.driver.find_element(*self.ad_iframe)
                self.driver.switch_to.frame(iframe)
                self.driver.find_element(*self.creative_dismiss_button).click()
        except (TimeoutException, NoSuchElementException, ElementNotInteractableException):
            pass
        self.driver.switch_to.default_content()

    def wait_dialog(self, timeout: int = 5):
        # wait until wait dialog appear and disappear
        WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(self.wait_dialog_widget))
        WebDriverWait(self.driver, timeout).until(EC.invisibility_of_element_located(self.wait_dialog_widget))
        print()
