from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.my_advertisements_page import MyAdvertisementsPage
from utils.constants import SITE_URL, USERNAME, PASSWORD


def test_update_advertisement(driver):
    driver.get(SITE_URL)
    login_page = LoginPage(driver)
    login_page.enter_username(username=USERNAME)
    login_page.enter_password(password=PASSWORD)
    login_page.click_login_button()
    home_page = HomePage(driver)
    home_page.close_cookie_bar()
    home_page.verify_user_profile_menu_box()
    my_advertisements_page = MyAdvertisementsPage(driver)
    my_advertisements_page.verify_adv_item()
    my_advertisements_page.skip_creative_if_exist()
    my_advertisements_page.up_adverts()
