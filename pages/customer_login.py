from pages.base_page import BasePage
from pages.locators import login_locators as loc


class CustomerLogin(BasePage):
    page_url = '/customer/account/login/'

    def fill_login_form(self, login, password):
        email_field = self.find(loc.email_field_loc)
        password_field = self.find(loc.password_field_loc)
        button = self.find(loc.button_loc)
        email_field.send_keys(login)
        password_field.send_keys(password)
        button.click()

    def check_error_alert(self, text):
        error_alert = self.find(loc.error_locator)
        assert error_alert.text == text