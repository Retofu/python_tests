from elements.alerts import Alerts as alerts
from elements.headers import Title_Headers as t_headers

def test_header_title(login_page):
    login_page.open_page()
    login_page.check_page_header_title(t_headers.Customer_Login.value)

def test_incorrect_login(login_page):
    login_page.open_page()
    login_page.fill_login_form('invalid_email@example.com', 'wrong_password')
    login_page.check_error_alert(alerts.Login_Error_Alert.value)