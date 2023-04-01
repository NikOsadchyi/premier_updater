from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.my_advertisements_page import MyAdvertisementsPage
from utils.constants import SITE_URL, USERNAME, PASSWORD
from utils.log_utils import log_step


def test_update_advertisement(driver):
    """
    Verify updating advertisement
    Steps:
        1. Login
        2. Close cookie bar
        3. Veryfi list of advertisements is appeared
        4. Skip targeting advertising if appeared
        5. Up all existing advertisements on the current page
    """
    log_step("Login")
    login_page = LoginPage(driver)
    login_page.login(SITE_URL, USERNAME, PASSWORD)

    log_step("Close cookie bar")
    home_page = HomePage(driver)
    home_page.close_cookie_bar()

    log_step("Veryfi list of advertisements is appeared")
    my_advertisements_page = MyAdvertisementsPage(driver)
    my_advertisements_page.verify_adv_item()

    log_step("Skip targeting advertising if appeared")
    my_advertisements_page.skip_creative_if_exist()

    log_step("Up all existing advertisements on the current page")
    my_advertisements_page.up_adverts()
